
from werkzeug.security import safe_str_cmp
from starter_code.models.user import UserModel


def Authenticate(username, password):
    '''
    Function get called when a user/pass calls the /auth endpoint
    :param username:
    :param password:
    :return: user is success, else None
    '''

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    '''
    Gets called when user has already authenticated ahd Flask-JwT verified the authentication
    header is correct
    :param payload: Dict with 'identity', key, which is the user id
    :return:  UserModel object
    '''

    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
