class PaymentEngine:

    def create_invoice(self, user_id, plan):
        return {
            "user_id": user_id,
            "plan": plan,
            "status": "pending",
            "currency": "USDT",
            "network": "TRC20"
        }

    def verify_payment(self, tx_id):
        return True
