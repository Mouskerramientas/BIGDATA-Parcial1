from main import main
from botocore.exceptions import ClientError
from utils import NotFoundException
from responses import CLIENT_ERROR_RESPONSE, ERROR_NOT_FOUND_RESPONSE, ERROR_RESPONSE, SUCCESS_RESPONSE


def app(event, context):

    try:
        main(event["Records"][0])
    except ClientError:
        return CLIENT_ERROR_RESPONSE
    except Exception as e:
        return ERROR_RESPONSE
    except NotFoundException:
        return ERROR_NOT_FOUND_RESPONSE
    
    return SUCCESS_RESPONSE
