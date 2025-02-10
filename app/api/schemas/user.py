from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str


class UserCreate(UserBase):
    password: str


class UserFromDB(UserBase):
    id: int
