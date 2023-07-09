from fastapi import APIRouter
from app.user.services.createUser import createUser
from app.user.dto.createUserDTO import CreateUserDTO

router = APIRouter(
    prefix="/auth",
    tags=['Auth']
)

@router.post("/signup")
async def signup(data: CreateUserDTO):
    user = await createUser(data)
    return user
