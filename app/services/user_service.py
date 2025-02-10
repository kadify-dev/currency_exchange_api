from app.api.schemas.user import UserCreate, UserFromDB
from app.utils.uow import IUnitOfWork


class UserService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def get_user_by_id(self, user_id: int):
        async with self.uow:
            user = await self.uow.user.get_by_id(user_id)
            return UserFromDB.model_validate(user)

    async def add_user(self, user_data: UserCreate):
        async with self.uow:
            stmt = await self.uow.user.add_one(user_data.model_dump())
            res = UserFromDB.model_validate(stmt)
            await self.uow.commit()
            return res
