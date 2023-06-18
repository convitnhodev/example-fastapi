from sqlalchemy.orm import Session

from schemas.uses import UserCreate
from db.models.users import User
from core.hashing import Hashser

def create_new_user(user: UserCreate, db: Session):
    user = User(username=user.username, 
                email=user.email,
                hashed_password = Hashser.get_password_hash(user.password), 
                is_active=True, 
                is_supperuser=False, 
                )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user 