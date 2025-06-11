import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import OAuth2AuthorizationCodeBearer
from router import sale

API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

app = FastAPI()

app.get("/health") 
lambda: {"status": "ok"}

app.include_router(sale.router, prefix=API_PREFIX, tags=["sales"])

@app.on_event("startup")
def startup():
    # TODO: Add startup logic to clear/populate database
    pass

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
    )