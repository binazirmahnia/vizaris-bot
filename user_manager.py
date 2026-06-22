users = {}

def get_user(user_id):
    return users.get(user_id, {"plan": "free"})

def upgrade_user(user_id, plan):
    users[user_id] = {"plan": plan}
