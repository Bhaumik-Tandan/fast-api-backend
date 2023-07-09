from app.user.dto.createUserDTO import CreateUserDTO
from app.db import db

async def createUser(createUser:CreateUserDTO):
    user_collection = db['users']
    user=user_collection.insert_one(createUser.dict())
    user=createUser
    return user