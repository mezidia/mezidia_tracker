import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from routers import users, chat

app = FastAPI()
origins = ["http://localhost", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', status_code=status.HTTP_200_OK)
async def start_page():
    return {'Information': 'Too see all available methods visit /docs page'}


app.include_router(users.router)
app.include_router(chat.router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
