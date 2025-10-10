from payment_processor import PaymentProcessor

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")
        # TODO: Integrate with PayPal API
