from payment_processor import PaymentProcessor

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing Credit Card payment of ${amount:.2f}")
        # TODO: Integrate with Credit Card API
