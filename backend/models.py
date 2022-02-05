from datetime import datetime
from typing import Optional, List
from bson import ObjectId

from pydantic import BaseModel, Field, EmailStr, HttpUrl


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    surname: str = Field(...)
    email: EmailStr = Field(...)
    github_nickname: Optional[str]
    gitlab_nickname: Optional[str]
    bitbucket_nickname: Optional[str]
    teams: List[str] = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane",
                'surname': 'Doe',
                "email": "jdoe@example.com",
                'github_nickname': 'mez',
                'gitlab_nickname': 'mez',
                'bitbucket_nickname': 'mez',
                'teams': ['mezidia'],
                'password': 'hello',
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[EmailStr]
    github_nickname: Optional[str]
    gitlab_nickname: Optional[str]
    bitbucket_nickname: Optional[str]
    teams: Optional[List[str]]
    password: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane",
                'surname': 'Doe',
                "email": "jdoe@example.com",
                'github_nickname': 'mez',
                'gitlab_nickname': 'mez',
                'bitbucket_nickname': 'mez',
                'teams': ['mezidia'],
                'password': 'hello',
            }
        }


class ProjectModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    author: str = Field(...)
    github_url: HttpUrl = Field(...)
    gitlab_url: Optional[HttpUrl]
    bitbucket_url: Optional[HttpUrl]
    members: List[str] = Field(...)
    tasks: List[str] = Field(...)
    chat: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "mezidia_tracker",
                'author': 'mezgoodle',
                'github_url': 'https://github.com/mezgoodle/mezidia_tracker',
                "gitlab_url": "https://gitlab.com/mezgoodle/mezidia_tracker",
                "bitbucket_url": "https://bitbucket.com/mezgoodle/mezidia_tracker",
                'members': ['mezgoodle'],
                'tasks': ['do a readme'],
            }
        }


class UpdateProjectModel(BaseModel):
    pass


class TaskModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    author: str = Field(...)
    workers: List[str] = Field(...)
    until_date: datetime = Field(...)
    github_link: Optional[HttpUrl]
    gitlab_link: Optional[HttpUrl]
    bitbucket_link: Optional[HttpUrl]
    desc: str = Field(...)


class UpdateTaskModel(BaseModel):
    pass


class ChatModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    chat_name: str = Field(...)
    messages: List[dict] = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "chat_id": "1",
                'messages': [{}],
            }
        }
