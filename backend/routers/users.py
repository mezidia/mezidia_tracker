from fastapi import APIRouter, status, Body, HTTPException

from database import Client
from models import UserModel, UpdateUserModel

from typing import List, Optional
import os

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
password = os.getenv('DB_PASSWORD', 'password')


@router.post('', response_description='Add new user', response_model=UserModel,
             status_code=status.HTTP_201_CREATED)
async def create_player(player: UserModel = Body(...)):
    client = Client(password, 'users')
    """
    Create a user:
    - **current user** should be admin
    - **user_id**: user id from Telegram
    - **telegram_name**: the user nickname in Telegram
    - **name**: game name
    - **level**: player level
    - **experience**: current player experience
    - **health**: current player health
    - **energy**: current player energy
    - **strength**: current player strength
    - **agility**: current player agility
    - **intuition**: current player intuition
    - **intelligence**: current player intelligence
    - **hero_class**: player hero class
    - **nation**: name of the country where player was born
    - **money**: current player money
    - **items**: list of items that player has
    - **mount**: description of the mount
    - **current_state**: place where player is at this time
    """
    result = await client.create_document(player)
    return result


@router.get('s', response_description='List all users', response_model=List[UserModel],
            status_code=status.HTTP_200_OK)
async def list_users():
    """
    Get all users
    """
    client = Client(password, 'users')
    cities = await client.get_all_objects()
    return cities


@router.get('', response_description='Get a single user', response_model=UserModel,
            status_code=status.HTTP_200_OK)
async def show_user(identifier: Optional[str] = None, email: Optional[str] = None):
    """
    Get a user by email:
    - **email**: user's email
    """
    client = Client(password, 'users')
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
    client = Client(password, 'users')
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
    client = Client(password, 'users')
    variables = locals()
    options = {'identifier': '_id', 'email': 'email'}
    for key in variables.keys():
        if variables[key] is not None:
            return await client.delete_object({options[key]: variables[key]})
    raise HTTPException(status_code=404, detail='Set some parameters')
