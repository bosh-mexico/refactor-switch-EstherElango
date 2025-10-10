from payment_mode import PaymentMode
from payment_factory import PaymentProcessorFactory

def checkout(mode: PaymentMode, amount: float):
    processor = PaymentProcessorFactory.get_processor(mode)
    if processor:
        processor.process_payment(amount)
    else:
        print("Checkout failed: Unsupported payment mode.")

# Example usage
if __name__ == "__main__":
    amount = 150.75

    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)
