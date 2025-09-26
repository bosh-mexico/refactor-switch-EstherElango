
from enum import Enum

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

# Checkout function (only returns message, no printing)
def checkout(mode: PaymentMode, amount: float) -> str:
    match mode:
        case PaymentMode.PAYPAL:
            return f"Processing PayPal payment of ${amount:.2f}"
        case PaymentMode.GOOGLEPAY:
            return f"Processing GooglePay payment of ${amount:.2f}"
        case PaymentMode.CREDITCARD:
            return f"Processing Credit Card payment of ${amount:.2f}"
        case _:
            return "Invalid payment mode selected!"

# Example usage (separate responsibility: printing/logging)
if __name__ == "__main__":
    amount = 150.75

    print(checkout(PaymentMode.PAYPAL, amount))
    print(checkout(PaymentMode.GOOGLEPAY, amount))
    print(checkout(PaymentMode.CREDITCARD, amount))
    print(checkout(PaymentMode.UNKNOWN, amount))
