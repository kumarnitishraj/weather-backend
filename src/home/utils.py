from rest_framework.authtoken.models import Token
from rest_framework import status


ERROR_STATUS = {
    "status": None,
    "message": None,
    "ResponseStatus":False,
}

notacceptable_message = "Incorrect Data !"
failure_message = "Something went wrong !"
unauthorized_messsage = "Token is not valid !"
not_found_message = "Releted Data is not there"
forbidden_message = "You do not have permission to access"
success_status = status.HTTP_200_OK

def not_found_404(message=not_found_message):

    ERROR_STATUS["status"] = status.HTTP_404_NOT_FOUND
    ERROR_STATUS["message"] = message
    return ERROR_STATUS, ERROR_STATUS["status"]

def notacceptable(message=notacceptable_message):

    ERROR_STATUS["status"] = status.HTTP_406_NOT_ACCEPTABLE
    ERROR_STATUS["message"] = message
    return ERROR_STATUS, ERROR_STATUS["status"]

def unauthorized(message=unauthorized_messsage):

    ERROR_STATUS["status"] = status.HTTP_401_UNAUTHORIZED
    ERROR_STATUS["message"] = unauthorized_messsage
    return ERROR_STATUS, ERROR_STATUS["status"]


def failure_400(message=failure_message):
    ERROR_STATUS["status"] = status.HTTP_400_BAD_REQUEST
    ERROR_STATUS["message"] = message
    return ERROR_STATUS, ERROR_STATUS["status"]

def forbidden_403(message=forbidden_message):
    ERROR_STATUS["status"] = status.HTTP_403_FORBIDDEN
    ERROR_STATUS["message"] = message
    return ERROR_STATUS, ERROR_STATUS["status"]

def success(data=None,success_status=success_status,message=False):
    SUCCESS_STATUS = {
        "status": success_status,
        "ResponseStatus":True,
    }
    if message:
        SUCCESS_STATUS["message"] = message
        SUCCESS_STATUS.pop('data', None)
    else:
        SUCCESS_STATUS["data"] = data

    return SUCCESS_STATUS, SUCCESS_STATUS["status"]
