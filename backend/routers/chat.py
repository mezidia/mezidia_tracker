from typing import List

from fastapi import (
    APIRouter,
    WebSocket,
    HTTPException,
    WebSocketDisconnect,
    status,
    Body,
)
from fastapi.responses import HTMLResponse

from models import ChatModel
from database import Client
from config import DB_PASSWORD


router = APIRouter(prefix='/chat', tags=['Chat'])


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.get('')
async def get() -> HTMLResponse:
    pass


@router.post(
    '/create',
    response_description='Add new chat',
    response_model=ChatModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_chat(chat: ChatModel = Body(...)):
    """
    Create a chat:
    - **chat_name**: chat name
    - **messages**: chat messages
    """
    client = Client(DB_PASSWORD, 'chats')
    result = await client.create_document(chat)
    return result


@router.get(
    '/{name}',
    response_description='Get a single chat',
    response_model=ChatModel,
    status_code=status.HTTP_200_OK,
)
async def get_chat_by_name(name: str):
    """
    Get a chat by name:
    - **name**: chat name
    """
    client = Client(DB_PASSWORD, 'chats')

    try:
        data = await client.get_object({'chat_name': name})
    except:
        raise HTTPException(status_code=404, detail='Set some parameters')

    return data


@router.get(
    '/all',
    response_description='List all chats',
    response_model=List[ChatModel],
    status_code=status.HTTP_200_OK,
)
async def list_chats():
    """
    Get all chats
    """
    client = Client(DB_PASSWORD, 'chats')
    chats = await client.get_all_objects()
    return chats


# TO DO: update and delete messages


@router.websocket('/{name}/{client_id}')
async def websocket_endpoint(name: str, websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            # TO DO: datetime

            client = Client(DB_PASSWORD, 'chats')
            chat = await client.get_object({'chat_name': name})
            messages = chat['messages']
            messages.append(
                {
                    'user_id': client_id,
                    'content': data['content'],
                    'created_at': data['created_at'],
                }
            )

            _ = await client.collection.update_one(
                {'chat_name': name}, {'$set': {'messages': messages}}
            )

            await manager.broadcast(data['content'])
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f'{client_id} left the chat')
