from uuid import UUID
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import decode_access_token
from app.models.user import User
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db))->User:
 subject=decode_access_token(token)
 if not subject: raise HTTPException(status_code=401,detail='Invalid or expired access token',headers={'WWW-Authenticate':'Bearer'})
 try: user=db.get(User,UUID(subject))
 except (ValueError,TypeError): user=None
 if not user or user.account_status!='active': raise HTTPException(status_code=401,detail='User account is unavailable')
 return user
