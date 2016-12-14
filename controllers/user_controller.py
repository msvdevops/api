def create_user(body = None) -> str:
    return 'do some magic!'

def delete_user(userId) -> str:
    return 'do some magic!'

def get_services(userId) -> str:
    return 'do some magic!'

def get_tokens(userId) -> str:
    return 'do some magic!'

def get_user_by_id(userId) -> str:
    return 'do some magic!'

@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth ("admin")
def get_users() -> str:
    return 'do some magic!'

def update_user(userId, body = None) -> str:
    return 'do some magic!'
