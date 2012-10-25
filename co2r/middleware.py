from dynamicresponse.middleware.dynamicformat import DynamicFormatMiddleware
from dynamicresponse.response import DynamicResponse

class Co2rMiddleware(object):
    def process_response(self, request, response):    
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'X-Requested-With'
        return response
