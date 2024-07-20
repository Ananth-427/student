import uvicorn

from router import create_app

app = create_app()

if __name__ == "_main_":
    uvicorn.run(app, host="localhost", port=5000)