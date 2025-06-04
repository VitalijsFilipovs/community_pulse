from pydantic import BaseModel

class ResponseCreate(BaseModel):
    question_id: int
    is_agree: bool

class ResponseStats(BaseModel):
    question_id: int
    agree_count: int
    disagree_count: int
