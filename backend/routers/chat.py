from fastapi import APIRouter, status, Body, HTTPException

from config import DB_PASSWORD


router = APIRouter(
    prefix='/chat',
    tags=['Chat']
)
