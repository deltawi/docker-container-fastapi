from pydantic import BaseModel
from fastapi import Form

class ChatInput(BaseModel):
    userprompt: str = Form(...)