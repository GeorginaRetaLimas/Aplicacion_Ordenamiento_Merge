import asgiref
import uvicorn
import urllib.parse

from merge_sort import merge_sort

async def app(scope, receive, send):
    
    if scope["type"] == "http":
        if scope["method"] == "GET":
            with open("index.html", "r", encoding="utf-8") as f:
                html = f.read()

            # Como es get no procesamos y no hacemos nada
            html = html.replace("{{resultado}}", "")
        
        elif scope["method"] == "POST":

            # Creamos una variable vacia tipo bits
            body = b""

            # Y con eso recibimos el body en cachitos
            while True:
                event = await receive()
                body += event.get("body", b"")

                # Si ya no hay mas body paramos
                if not event.get("more_body"):
                    break

            # De bytes pasamos los datos a string para tener la lista
            datos = body.decode()

            # Dividimos la lista entre el "=" y tomamos la posición uno con los numeros
            datos_numeros = datos.split("=")[1]

            # Decodificamos la URL para convertir los + en espacios
            datos_numeros = urllib.parse.unquote_plus(datos_numeros)

            # Lista para los numeros en float
            lista = []

            # Recorremos separando cada elemento por la coma
            for x in datos_numeros.split(","):
                # Quitamos los espacios antes y después
                numero = x.strip()

                # Si el numero no es null 
                if numero != "":
                    # Lo convertimos a float
                    lista.append(float(numero))

                
            # Si hay elementos en la lista la mandamos al merge_sort
            if len(lista) > 0:
                await merge_sort(lista, 0, len(lista)-1)

            # Convertimos el resultado a string
            resultado = ", ".join(str(x) for x in lista)

            with open("index.html", "r", encoding="utf-8") as f:
                html = f.read()

            html_resultado = f"<h2>Resultado:</h2><p>{resultado}</p>"
            html = html.replace("{{resultado}}", html_resultado)

            
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            # La b representa que es una cadena de bits
            [b'content-type', b'text/html'],
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': html.encode("utf-8"),
    })

if __name__ == "__main__":
    uvicorn.run(app, port=5000, log_level="info")