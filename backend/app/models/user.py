import uuid
from datetime import datetime
from sqlalchemy import DateTime,String,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy.types import Uuid
from app.db.base import Base
class User(Base):
 __tablename__='users'
 id:Mapped[uuid.UUID]=mapped_column(Uuid(as_uuid=True),primary_key=True,default=uuid.uuid4)
 full_name:Mapped[str]=mapped_column(String(120),nullable=False)
 phone_e164:Mapped[str]=mapped_column(String(20),unique=True,index=True,nullable=False)
 email:Mapped[str|None]=mapped_column(String(255),unique=True)
 password_hash:Mapped[str]=mapped_column(String(255),nullable=False)
 preferred_language:Mapped[str]=mapped_column(String(8),default='bn',nullable=False)
 account_status:Mapped[str]=mapped_column(String(20),default='active',nullable=False)
 created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),nullable=False)
 farms=relationship('Farm',back_populates='owner',cascade='all, delete-orphan')
