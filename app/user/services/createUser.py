from app.user.dto.createUserDTO import CreateUserDTO
from app.db import db

async def createUser(createUser:CreateUserDTO):
    user_collection = db['users']
    user=await user_collection.insert_one(user)
    return user