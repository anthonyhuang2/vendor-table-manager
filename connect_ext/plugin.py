from connect.eaas.core.extension import WebApplicationBase
from connect.eaas.core.decorators import web_app, router

@web_app(router)
class VendorTableExtension(WebApplicationBase):

    @router.get('/admin')
    def admin_page(self, request):
        # We can grab the user's name from the request header if available, 
        # or just hardcode a placeholder for now.
        return {
            'template': 'index.html',
            'context': {
                'user_name': request.headers.get('Connect-User-Name', 'Partner')
            }
        }
