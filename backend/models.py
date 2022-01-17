from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List


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
    github_nickname: Optional[str] = Field(...)
    gitlab_nickname: Optional[str] = Field(...)
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
                'teams': ['mezidia'],
                'password': 'hello',
            }
        }


class ProjectModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    github_url: Optional[str] = Field(...)
    gitlab_url: Optional[str] = Field(...)
    members: List[str] = Field(...)
    tasks: List[str] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "mezgoodle/mezidia_tracker",
                'github_url': 'https://github.com/mezgoodle/mezidia_tracker',
                "gitlab_url": "https://gitlab.com/mezgoodle/mezidia_tracker",
                'members': ['mezgoodle'],
                'tasks': ['do a readme'],
            }
        }
