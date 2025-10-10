from enum import Enum

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

# Separate processing logic for cleaner design
def process_paypal(amount):
    print(f"Processing PayPal payment of ${amount:.2f}")

def process_googlepay(amount):
    print(f"Processing GooglePay payment of ${amount:.2f}")

def process_creditcard(amount):
    print(f"Processing Credit Card payment of ${amount:.2f}")

# Checkout function (controller)
def checkout(mode: PaymentMode, amount: float):
    payment_processors = {
        PaymentMode.PAYPAL: process_paypal,
        PaymentMode.GOOGLEPAY: process_googlepay,
        PaymentMode.CREDITCARD: process_creditcard,
    }

    processor = payment_processors.get(mode)
    if processor:
        processor(amount)
    else:
        print("Invalid payment mode selected!")

# Example usage
if __name__ == "__main__":
    amount = 150.75
    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)

