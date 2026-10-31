import uuid
from datetime import datetime
from sqlalchemy import DateTime,ForeignKey,Numeric,String,Text,UniqueConstraint,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy.types import Uuid
from app.db.base import Base
class SoilSample(Base):
 __tablename__='soil_samples'
 id:Mapped[uuid.UUID]=mapped_column(Uuid(as_uuid=True),primary_key=True,default=uuid.uuid4); farm_id:Mapped[uuid.UUID]=mapped_column(Uuid(as_uuid=True),ForeignKey('farms.id',ondelete='CASCADE'),index=True,nullable=False)
 collected_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),nullable=False); source_type:Mapped[str]=mapped_column(String(20),default='manual',nullable=False); lab_name:Mapped[str|None]=mapped_column(String(160)); notes:Mapped[str|None]=mapped_column(Text); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),nullable=False)
 farm=relationship('Farm',back_populates='soil_samples'); results=relationship('SoilTestResult',back_populates='sample',cascade='all, delete-orphan')
class SoilTestResult(Base):
 __tablename__='soil_test_results'; __table_args__=(UniqueConstraint('soil_sample_id','parameter_code',name='uq_soil_sample_parameter'),)
 id:Mapped[uuid.UUID]=mapped_column(Uuid(as_uuid=True),primary_key=True,default=uuid.uuid4); soil_sample_id:Mapped[uuid.UUID]=mapped_column(Uuid(as_uuid=True),ForeignKey('soil_samples.id',ondelete='CASCADE'),index=True,nullable=False)
 parameter_code:Mapped[str]=mapped_column(String(40),nullable=False); numeric_value:Mapped[float]=mapped_column(Numeric(14,5),nullable=False); unit:Mapped[str]=mapped_column(String(40),nullable=False); method:Mapped[str|None]=mapped_column(String(120)); sample=relationship('SoilSample',back_populates='results')
