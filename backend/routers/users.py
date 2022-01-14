from fastapi import APIRouter, status, Body

from database import Client
from models import UserModel

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('', response_description='Add new player', response_model=UserModel,
             status_code=status.HTTP_201_CREATED)
async def create_player(player: UserModel = Body(...)):
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
