from pydantic import BaseModel

# setting up schema for post creation with title and content as required fields
class PostCreate(BaseModel):
    title: str
    content: str