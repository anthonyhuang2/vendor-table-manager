# We import 'WebApplicationBase' from the core library
from connect.eaas.core.extension import WebApplicationBase
from connect.eaas.core.decorators import web_app, router

@web_app(router)
class VendorTableExtension(WebApplicationBase):

    @router.get('/admin')
    def admin_page(self, request):
        return {
            'template': 'index.html',
            'context': {
                'title': 'Vendor Table Manager',
                'data': 'Welcome to your extension!'
            }
        }
# Final fix for version 1.0.6
