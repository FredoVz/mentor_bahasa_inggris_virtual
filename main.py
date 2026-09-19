from loguru import logger
from fastapi import FastAPI, Request, Response, status

app = FastAPI()

# /
@app.get("/")
async def root():
    return {"status": "ini dari root"} # json

@app.get("/get")
async def endpoint_get():
    return {"http_method": "get"}

# http request -> get and post
@app.post("/post")
async def endpoint_post():
    return {"http_method": "post"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    req_body = await request.json()
    logger.debug(req_body)
    return Response(status_code=status.HTTP_200_OK)

# terminal cara jalankan API
# uv run fastapi dev

# http://127.0.0.1:8000/
# localhost:8000

# terminal untuk coba post
# curl -X POST http://127.0.0.1:8000/post / localhost:8000/post
# curl.exe -X POST localhost:8000/post

# Invoke-WebRequest -Method POST -Uri http://127.0.0.1:8000/post

# webhook
# curl.exe -X POST localhost:8000/webhook \
# -H "Content-Type: application/json" \
# -d '{"data": "ini contoh data dari server telegram"}'

# webhook for powershell windows
# curl.exe -X POST http://localhost:8000/webhook -H "Content-Type: application/json" -d "{\`"data\`": \`"ini contoh data dari server telegram\`"}"