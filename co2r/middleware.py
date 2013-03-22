from dynamicresponse.middleware.dynamicformat import DynamicFormatMiddleware
from dynamicresponse.response import DynamicResponse


class Co2rMiddleware(object):
    def process_response(self, request, response):
        if isinstance(response, DynamicResponse):
            response = response.render_response(request, response)

        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'origin, x-requested-with, content-type, accept'

        return response
