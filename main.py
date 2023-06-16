from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.router import chat_router

# Fast api
app = FastAPI()

# add the authentication routes
app.include_router(chat_router)

# add cors 
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add any additional routes
@app.get("/")
async def root():
    return {"message": "Hello, app is running!"}
