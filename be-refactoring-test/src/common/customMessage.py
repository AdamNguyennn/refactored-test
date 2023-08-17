from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled


# 2. Customing the exceeded rate limit response
def custom_exception_handler(exc, context):
        response = exception_handler(exc, context)

        if isinstance(exc, Throttled):
            response.data['detail'] = 'Rate limit exceeded 10 req/m'

        return response
