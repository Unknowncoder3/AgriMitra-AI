from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.security import create_access_token,hash_password,verify_password
from app.db.session import get_db
from app.models.user import User
from app.schemas.auth import RegisterRequest,LoginRequest,TokenResponse,UserRead
router=APIRouter()
def make_token(user): return TokenResponse(access_token=create_access_token(str(user.id)),expires_in=settings.access_token_expire_minutes*60,user=UserRead.model_validate(user))
@router.post('/register',response_model=TokenResponse,status_code=status.HTTP_201_CREATED)
def register(payload:RegisterRequest,db:Session=Depends(get_db)):
 if db.scalar(select(User).where(User.phone_e164==payload.phone_e164)): raise HTTPException(status_code=409,detail='A user with this phone number already exists')
 if payload.email and db.scalar(select(User).where(User.email==payload.email)): raise HTTPException(status_code=409,detail='A user with this email already exists')
 user=User(full_name=payload.full_name.strip(),phone_e164=payload.phone_e164,email=payload.email,password_hash=hash_password(payload.password),preferred_language=payload.preferred_language)
 db.add(user); db.commit(); db.refresh(user); return make_token(user)
@router.post('/login',response_model=TokenResponse)
def login(payload:LoginRequest,db:Session=Depends(get_db)):
 user=db.scalar(select(User).where(User.phone_e164==payload.phone_e164))
 if not user or not verify_password(payload.password,user.password_hash): raise HTTPException(status_code=401,detail='Incorrect phone number or password')
 if user.account_status!='active': raise HTTPException(status_code=403,detail='This account is not active')
 return make_token(user)
