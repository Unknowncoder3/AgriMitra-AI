import uuid
from datetime import datetime
from sqlalchemy import DateTime,ForeignKey,Numeric,String,Text,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy.types import Uuid
from app.db.base import Base
class Farm(Base):
 __tablename__='farms'
 id:Mapped[uuid.UUID]=mapped_column(Uuid(as_uuid=True),primary_key=True,default=uuid.uuid4)
 owner_user_id:Mapped[uuid.UUID]=mapped_column(Uuid(as_uuid=True),ForeignKey('users.id',ondelete='CASCADE'),index=True,nullable=False)
 name:Mapped[str]=mapped_column(String(120),nullable=False); district:Mapped[str]=mapped_column(String(100),nullable=False)
 block:Mapped[str|None]=mapped_column(String(100)); village:Mapped[str|None]=mapped_column(String(100)); address_text:Mapped[str|None]=mapped_column(Text)
 total_area:Mapped[float]=mapped_column(Numeric(12,3),nullable=False); area_unit:Mapped[str]=mapped_column(String(20),nullable=False)
 soil_texture:Mapped[str|None]=mapped_column(String(50)); irrigation_type:Mapped[str|None]=mapped_column(String(50)); verification_status:Mapped[str]=mapped_column(String(24),default='unverified',nullable=False)
 created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),nullable=False); updated_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now(),nullable=False)
 owner=relationship('User',back_populates='farms'); soil_samples=relationship('SoilSample',back_populates='farm',cascade='all, delete-orphan')
