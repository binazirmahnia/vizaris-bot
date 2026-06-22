users_db = {}

def save_user(user_id, data):
    users_db[user_id] = data

def get_user(user_id):
    return users_db.get(user_id)
