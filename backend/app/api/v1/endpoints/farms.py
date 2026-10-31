from uuid import UUID
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.farm import Farm
from app.models.user import User
from app.schemas.farm import FarmCreate,FarmRead,FarmUpdate
router=APIRouter()
@router.get('',response_model=list[FarmRead])
def list_farms(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
 return list(db.scalars(select(Farm).where(Farm.owner_user_id==current_user.id).order_by(Farm.created_at.desc())))
@router.post('',response_model=FarmRead,status_code=status.HTTP_201_CREATED)
def create_farm(payload:FarmCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
 farm=Farm(**payload.model_dump(),owner_user_id=current_user.id); db.add(farm); db.commit(); db.refresh(farm); return farm
def owned_farm(farm_id:UUID,db:Session,user:User):
 farm=db.scalar(select(Farm).where(Farm.id==farm_id,Farm.owner_user_id==user.id))
 if not farm: raise HTTPException(status_code=404,detail='Farm not found')
 return farm
@router.get('/{farm_id}',response_model=FarmRead)
def get_farm(farm_id:UUID,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)): return owned_farm(farm_id,db,current_user)
@router.patch('/{farm_id}',response_model=FarmRead)
def update_farm(farm_id:UUID,payload:FarmUpdate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
 farm=owned_farm(farm_id,db,current_user)
 for key,value in payload.model_dump(exclude_unset=True).items(): setattr(farm,key,value)
 db.commit(); db.refresh(farm); return farm
@router.delete('/{farm_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_farm(farm_id:UUID,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
 db.delete(owned_farm(farm_id,db,current_user)); db.commit()
