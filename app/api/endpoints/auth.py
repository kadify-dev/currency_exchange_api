from fastapi import APIRouter, Depends

from app.api.schemas.user import UserCreate
from app.services.user_service import UserService
from app.utils.uow import IUnitOfWork, UnitOfWork

user_router = APIRouter(prefix="/auth", tags=["Auth"])


async def get_user_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> UserService:
    return UserService(uow)


@user_router.post("/register")
async def create_new_user(
    user_data: UserCreate, user_service: UserService = Depends(get_user_service)
):
    return await user_service.add_user(user_data)
