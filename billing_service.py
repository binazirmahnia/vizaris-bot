class BillingService:

    def charge(self, user, amount):
        return {
            "user": user,
            "amount": amount,
            "status": "waiting"
        }
