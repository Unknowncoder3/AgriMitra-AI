def register(client,phone='+919876543210'):
 return client.post('/api/v1/auth/register',json={'full_name':'Test Farmer','phone_e164':phone,'password':'StrongPass123','preferred_language':'en'})
def test_health_and_readiness(client):
 assert client.get('/health').status_code==200; assert client.get('/ready').json()['status']=='ready'
def test_register_login_and_me(client):
 response=register(client); assert response.status_code==201; token=response.json()['access_token']; headers={'Authorization':f'Bearer {token}'}
 assert client.get('/api/v1/users/me',headers=headers).status_code==200
 assert client.post('/api/v1/auth/login',json={'phone_e164':'+919876543210','password':'StrongPass123'}).status_code==200
 assert client.post('/api/v1/auth/login',json={'phone_e164':'+919876543210','password':'wrong-password'}).status_code==401
def test_farm_crud_and_owner_isolation(client):
 first=register(client).json()['access_token']; second=register(client,'+919876543211').json()['access_token']; h1={'Authorization':f'Bearer {first}'}; h2={'Authorization':f'Bearer {second}'}
 created=client.post('/api/v1/farms',headers=h1,json={'name':'North Field','district':'Nadia','total_area':2.5,'area_unit':'acre'}); assert created.status_code==201; farm_id=created.json()['id']
 assert len(client.get('/api/v1/farms',headers=h1).json())==1; assert client.get(f'/api/v1/farms/{farm_id}',headers=h2).status_code==404
 assert client.patch(f'/api/v1/farms/{farm_id}',headers=h2,json={'name':'Intrusion'}).status_code==404; assert client.delete(f'/api/v1/farms/{farm_id}',headers=h1).status_code==204
def test_soil_sample_rejects_unowned_farm(client):
 token=register(client).json()['access_token']; headers={'Authorization':f'Bearer {token}'}
 response=client.post('/api/v1/soil/samples',headers=headers,json={'farm_id':'00000000-0000-0000-0000-000000000000','collected_at':'2026-10-31T10:00:00Z','source_type':'lab','results':[{'parameter_code':'ph','numeric_value':6.5,'unit':'pH'}]}); assert response.status_code==404
