from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId


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
    github_nickname: str = Field(...)
    gitlab_nickname: str = Field(...)
    team: str = Field(...)
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
                'team': 'mezidia',
                'password': 'hello',
            }
        }
