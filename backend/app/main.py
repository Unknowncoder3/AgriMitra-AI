from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import api_router
app=FastAPI(title=settings.app_name,version='0.3.0',description='AgriMitra AI modular backend API')
app.add_middleware(CORSMiddleware,allow_origins=settings.cors_origin_list,allow_credentials=True,allow_methods=['GET','POST','PATCH','DELETE','OPTIONS'],allow_headers=['Authorization','Content-Type','X-Request-ID'])
app.include_router(api_router,prefix=settings.api_v1_prefix)
@app.get('/health',tags=['operations'])
def health(): return {'status':'ok','service':'agrimitra-api'}
@app.get('/ready',tags=['operations'])
def ready():
 from sqlalchemy import text
 from app.db.session import engine
 with engine.connect() as connection: connection.execute(text('SELECT 1'))
 return {'status':'ready','database':'reachable'}
