from payment_processor import PaymentProcessor

class GooglePayProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing GooglePay payment of ${amount:.2f}")
        # TODO: Integrate with GooglePay API
