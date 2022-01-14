import uvicorn
from fastapi import FastAPI, status

from routers import users

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
async def start_page():
    return {'Information': 'Too see all available methods visit /docs page'}


app.include_router(users.router)

if __name__ == '__main__':
    uvicorn.run('main:app')
