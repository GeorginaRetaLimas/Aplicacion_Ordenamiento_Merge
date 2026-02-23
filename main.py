import asgiref
import uvicorn

async def app(scope, receive, send):
    with open("index.html", "rb") as f:
        html = f.read()

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
        'body': html,
    })

if __name__ == "__main__":
    uvicorn.run(app, port=5000, log_level="info")