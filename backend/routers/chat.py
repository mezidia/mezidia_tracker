from typing import List

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status, Body
from fastapi.responses import HTMLResponse

from models import ChatModel, MessageModel
from database import Client
from config import DB_PASSWORD


router = APIRouter(
    prefix='/chat',
    tags=['Chat']
)

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>Chat: <span id="chat-id"></span></h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            var chat_id = 1
            document.querySelector("#ws-id").textContent = client_id;
            document.querySelector("#chat-id").textContent = chat_id;
            var ws = new WebSocket(`ws://localhost:8000/${chat_id}/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


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


@router.get("/")
async def get() -> HTMLResponse:
    return HTMLResponse(html)


@router.post('', response_description='Add new chat', response_model=ChatModel,
             status_code=status.HTTP_201_CREATED)
async def create_chat(chat: ChatModel = Body(...)):
    """
    Create a chat:
    - **chat_id**: chat id
    - **name**: chat name
    - **messages**: chat messages
    """
    client = Client(DB_PASSWORD, 'chats')
    result = await client.create_document(chat)
    return result


@router.get('s', response_description='List all chats', response_model=List[ChatModel],
            status_code=status.HTTP_200_OK)
async def list_chats():
    """
    Get all chats
    """
    client = Client(DB_PASSWORD, 'chats')
    chats = await client.get_all_objects()
    return chats


@router.websocket("/{id}/{client_id}")
async def websocket_endpoint(id: int, websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{client_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{client_id} left the chat")