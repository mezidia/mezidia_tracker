from fastapi import APIRouter, status, Body, HTTPException

from database import Client
from models import UserModel, UpdateUserModel
from hashing import Hash
from config import DB_PASSWORD

from typing import List, Optional
import os

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('', response_description='Add new user', response_model=UserModel,
             status_code=status.HTTP_201_CREATED)
async def create_user(player: UserModel = Body(...)):
    """
    Create a user:
    - **name**: user's first name
    - **surname**: user's second name
    - **email**: user's email
    - **github_nickname**: user's github nickname
    - **gitlab_nickname**: user's github nickname
    - **team**: user's team name
    - **password**: user's password
    """
    client = Client(DB_PASSWORD, 'users')
    player.password = Hash.bcrypt(player.password)
    result = await client.create_document(player)
    return result


@router.get('s', response_description='List all users', response_model=List[UserModel],
            status_code=status.HTTP_200_OK)
async def list_users():
    """
    Get all users
    """
    client = Client(DB_PASSWORD, 'users')
    users = await client.get_all_objects()
    return users


@router.get('', response_description='Get a single user', response_model=UserModel,
            status_code=status.HTTP_200_OK)
async def show_user(identifier: Optional[str] = None, email: Optional[str] = None):
    """
    Get a user by email:
    - **email**: user's email
    """
    client = Client(DB_PASSWORD, 'users')
    variables = locals()
    options = {'identifier': '_id', 'email': 'email'}
    for key in variables.keys():
        if variables[key] is not None:
            return await client.get_object({options[key]: variables[key]})
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('', response_description='Update a user', response_model=UpdateUserModel,
            status_code=status.HTTP_200_OK)
async def update_user(identifier: Optional[str] = None, email: Optional[str] = None,
                      city: UpdateUserModel = Body(...)):
    """
    Update a user by email:
    - **email**: user's email
    """
    client = Client(DB_PASSWORD, 'users')
    variables = locals()
    options = {'identifier': '_id', 'email': 'email'}
    for key in variables.keys():
        if variables[key] is not None:
            return await client.update_object({options[key]: variables[key]}, city)
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('', response_description='Delete a user',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(identifier: Optional[str] = None, email: Optional[str] = None):
    """
    Delete a user by email:
    - **email**: user's email
    """
    client = Client(DB_PASSWORD, 'users')
    variables = locals()
    options = {'identifier': '_id', 'email': 'email'}
    for key in variables.keys():
        if variables[key] is not None:
            return await client.delete_object({options[key]: variables[key]})
    raise HTTPException(status_code=404, detail='Set some parameters')
