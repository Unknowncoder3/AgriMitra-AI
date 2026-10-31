from uuid import UUID
from datetime import datetime
from fastapi import APIRouter,Depends,HTTPException,status
from pydantic import BaseModel,Field
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.farm import Farm
from app.models.soil import SoilSample,SoilTestResult
from app.models.user import User
router=APIRouter()
class SoilResultInput(BaseModel):
 parameter_code:str=Field(min_length=1,max_length=40); numeric_value:float; unit:str=Field(min_length=1,max_length=40); method:str|None=None
class SoilSampleCreate(BaseModel):
 farm_id:UUID; collected_at:datetime; source_type:str=Field(default='manual',pattern='^(manual|lab)$'); lab_name:str|None=None; notes:str|None=None; results:list[SoilResultInput]=Field(default_factory=list)
@router.post('/samples',status_code=status.HTTP_201_CREATED)
def create_sample(payload:SoilSampleCreate,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
 farm=db.scalar(select(Farm).where(Farm.id==payload.farm_id,Farm.owner_user_id==user.id))
 if not farm: raise HTTPException(status_code=404,detail='Farm not found')
 if len({r.parameter_code for r in payload.results})!=len(payload.results): raise HTTPException(status_code=422,detail='Each soil parameter may appear only once per sample')
 sample=SoilSample(farm_id=farm.id,collected_at=payload.collected_at,source_type=payload.source_type,lab_name=payload.lab_name,notes=payload.notes); sample.results=[SoilTestResult(**r.model_dump()) for r in payload.results]
 db.add(sample); db.commit(); db.refresh(sample)
 return {'id':sample.id,'farm_id':sample.farm_id,'collected_at':sample.collected_at,'source_type':sample.source_type,'lab_name':sample.lab_name,'notes':sample.notes,'results':[{'parameter_code':r.parameter_code,'numeric_value':float(r.numeric_value),'unit':r.unit,'method':r.method} for r in sample.results]}
@router.get('/farms/{farm_id}/history')
def soil_history(farm_id:UUID,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
 farm=db.scalar(select(Farm).where(Farm.id==farm_id,Farm.owner_user_id==user.id))
 if not farm: raise HTTPException(status_code=404,detail='Farm not found')
 samples=db.scalars(select(SoilSample).where(SoilSample.farm_id==farm.id).order_by(SoilSample.collected_at.desc())).all()
 return [{'id':s.id,'collected_at':s.collected_at,'source_type':s.source_type,'lab_name':s.lab_name,'results':[{'parameter_code':r.parameter_code,'numeric_value':float(r.numeric_value),'unit':r.unit,'method':r.method} for r in s.results]} for s in samples]
