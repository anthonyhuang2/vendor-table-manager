import json
import os
from connect.eaas.extension import Extension, WebAppExtension
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates

# Setup templates directory
templates = Jinja2Templates(directory='templates')
DB_FILE = 'vendor_data.json'

def load_db():
    if not os.path.exists(DB_FILE):
        return {"headers": [], "rows": []}
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

class VendorTableExtension(Extension, WebAppExtension):

    @classmethod
    def get_descriptor(cls):
        return {
            "name": "Vendor Table Manager",
            "description": "Manage vendor lists with custom headers",
            "version": "1.0.0",
            "capabilities": {
                "webapp": {"url": "/admin"}
            }
        }

    async def retrieve_table_data(self, request):
        return JSONResponse(load_db())

    async def save_table_schema(self, request):
        payload = await request.json()
        db = load_db()
        db['headers'] = payload.get('headers', [])
        save_db(db)
        return JSONResponse({"status": "Schema updated"})

    async def add_row(self, request):
        payload = await request.json()
        db = load_db()
        # Create a simple ID
        new_id = len(db['rows']) + 1
        payload['row_data']['id'] = new_id
        db['rows'].append(payload['row_data'])
        save_db(db)
        return JSONResponse({"status": "Row added", "id": new_id})

    async def render_admin_page(self, request):
        return templates.TemplateResponse('index.html', {"request": request})
