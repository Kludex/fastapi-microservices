from users.crud.base import CRUDBase
from users.models.users import User
from users.schemas.user import UserInDB, UserUpdateDB

CRUDUser = CRUDBase[User, UserInDB, UserUpdateDB]
crud_user = CRUDBase(User)
