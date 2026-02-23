import asgiref
import uvicorn

async def app(scope, receive, send):
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
        'body': b'<h2>Hello World! App on SGI Server</h2>',
    })

if __name__ == "__main__":
    uvicorn.run(app, port=5000, log_level="info")