from app.db.models import User

from .base_repositories import Repository


class UserRepository(Repository):
    model = User
