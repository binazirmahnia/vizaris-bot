class Payment:

    def create(self, user_id, plan):
        return {"user": user_id, "plan": plan, "status": "pending"}

    def verify(self, tx):
        return True
