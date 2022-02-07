from fastapi import status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import motor.motor_asyncio


class Client:
    def __init__(self, password, collection_name: str, db_name='Mezidia_Tracker'):
        """
        Initializing client object with access to database
        :param password: password to account
        :param db_name: name of database in current cluster
        :param collection_name: name of collection in current database
        """
        cluster = motor.motor_asyncio.AsyncIOMotorClient(
            f'mongodb+srv://mezidia:{password}@mezidiatracker.'
            f'sqnpg.mongodb.net/mezidia_tracker?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')
        db = cluster[db_name]
        self.collection = db[collection_name]

    async def create_document(self, data: BaseModel) -> JSONResponse:
        data = jsonable_encoder(data)
        new_object = await self.collection.insert_one(data)
        created_object = await self.collection.find_one({'_id': new_object.inserted_id})
        if not created_object:
            raise HTTPException(status_code=404, detail='Object has not created')
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_object)

    async def get_all_objects(self) -> list:
        objects = await self.collection.find().to_list(1000)
        if not objects:
            raise HTTPException(status_code=404, detail='Objects have not found')
        return objects

    async def get_object(self, query: dict) -> dict:
        if (founded_object := await self.collection.find_one(query)) is not None:
            return founded_object
        raise HTTPException(status_code=404, detail='Object has not found')

    async def update_object(self, query: dict, requested_object: BaseModel) -> dict:
        requested_object = {k: v for k, v in requested_object.dict().items() if v is not None}

        if len(requested_object) >= 1:
            update_result = await self.collection.update_one(query, {'$set': requested_object})

            if update_result.modified_count == 1:
                if (updated_object := await self.collection.find_one(query)) is not None:
                    return updated_object

        if (existing_object := await self.collection.find_one(query)) is not None:
            return existing_object

        raise HTTPException(status_code=404, detail='Object has not found')

    async def delete_object(self, query: dict) -> JSONResponse:
        delete_result = await self.collection.delete_one(query)

        if delete_result.deleted_count == 1:
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

        raise HTTPException(status_code=404, detail='Object has not found')
