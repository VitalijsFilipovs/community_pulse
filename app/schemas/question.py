from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    category_id: int               # указываем категорию при создании вопроса

class QuestionResponse(QuestionBase):
    id: int
    category: CategoryBase         # возвращаем полную информацию о категории

    class Config:
        orm_mode = True
