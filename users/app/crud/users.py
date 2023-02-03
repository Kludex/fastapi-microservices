from app.crud.base import CRUDBase
from app.models.users import User
from app.schemas.user import UserInDB, UserUpdateDB

class CRUDUser(CRUDBase[User, UserInDB, UserUpdateDB]):
    pass

crud_user = CRUDUser(User)
