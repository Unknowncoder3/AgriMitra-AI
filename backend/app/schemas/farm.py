from datetime import datetime
from uuid import UUID
from pydantic import BaseModel,ConfigDict,Field
class FarmCreate(BaseModel):
 name:str=Field(min_length=2,max_length=120); district:str=Field(min_length=2,max_length=100); block:str|None=None; village:str|None=None; address_text:str|None=None; total_area:float=Field(gt=0,le=1000000); area_unit:str=Field(pattern='^(acre|hectare|bigha|katha)$'); soil_texture:str|None=None; irrigation_type:str|None=None
class FarmUpdate(BaseModel):
 name:str|None=Field(default=None,min_length=2,max_length=120); district:str|None=Field(default=None,min_length=2,max_length=100); block:str|None=None; village:str|None=None; address_text:str|None=None; total_area:float|None=Field(default=None,gt=0,le=1000000); area_unit:str|None=Field(default=None,pattern='^(acre|hectare|bigha|katha)$'); soil_texture:str|None=None; irrigation_type:str|None=None
class FarmRead(BaseModel):
 model_config=ConfigDict(from_attributes=True)
 id:UUID; name:str; district:str; block:str|None; village:str|None; address_text:str|None; total_area:float; area_unit:str; soil_texture:str|None; irrigation_type:str|None; verification_status:str; created_at:datetime
