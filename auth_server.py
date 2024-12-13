# JWT 인증을 위한 서버
from fastapi import FastAPI
from modules.routers import auth,apikey
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="🔒 Auth Center Server")
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (필요에 따라 수정)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router,tags=['Auth'])
app.include_router(apikey.router,tags=['APIKey'])


if __name__ == "__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=7777)