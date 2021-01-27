import json

from django.utils.safestring import mark_safe

from rest_framework.exceptions import APIException, _get_error_details
from rest_framework import status


class APIError(APIException):
    status_code = status.HTTP_200_OK
    default_detail = ''
    default_code = ''
    error = ''

    def __init__(self, detail=None, code=None, error=None):
        if not error and detail is None:
            detail = self.default_detail
        elif error is not None:
            detail = error
        if code is None:
            code = self.default_code

        if isinstance(detail, list) or isinstance(detail, dict):
            detail = mark_safe(json.dumps(detail))

        self.detail = _get_error_details(detail, code)
