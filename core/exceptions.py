from rest_framework.views import exception_handler
from rest_framework import status
from .responses import error_response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return error_response(
            code="SERVER_ERROR",
            message="Internal server error",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return error_response(
        code="API_ERROR",
        message=response.data,
        status=response.status_code
    )
