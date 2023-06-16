from fastapi import APIRouter
from .schemas import ChatInput

chat_router = APIRouter()

@chat_router.post("/")
def chat_input(chatInput: ChatInput):
    return {"result" : chatInput.userprompt}