import re
from uuid import UUID
from pydantic import BaseModel,ConfigDict,Field,field_validator
class RegisterRequest(BaseModel):
 full_name:str=Field(min_length=2,max_length=120); phone_e164:str=Field(min_length=8,max_length=20); email:str|None=Field(default=None,max_length=255); password:str=Field(min_length=10,max_length=128); preferred_language:str=Field(default='bn',pattern='^(bn|en|hi)$')
 @field_validator('phone_e164')
 @classmethod
 def validate_phone(cls,value):
  if not re.fullmatch(r'\+[1-9]\d{7,14}',value): raise ValueError('Use international E.164 format, e.g. +919876543210')
  return value
class LoginRequest(BaseModel): phone_e164:str; password:str
class UserRead(BaseModel):
 model_config=ConfigDict(from_attributes=True)
 id:UUID; full_name:str; phone_e164:str; email:str|None; preferred_language:str; account_status:str
class TokenResponse(BaseModel): access_token:str; token_type:str='bearer'; expires_in:int; user:UserRead
