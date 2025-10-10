from payment_mode import PaymentMode
from paypal_processor import PayPalProcessor
from googlepay_processor import GooglePayProcessor
from creditcard_processor import CreditCardProcessor
from payment_processor import PaymentProcessor

class PaymentProcessorFactory:
    @staticmethod
    def get_processor(mode: PaymentMode) -> PaymentProcessor:
        if mode == PaymentMode.PAYPAL:
            return PayPalProcessor()
        elif mode == PaymentMode.GOOGLEPAY:
            return GooglePayProcessor()
        elif mode == PaymentMode.CREDITCARD:
            return CreditCardProcessor()
        else:
            print("Invalid payment mode selected!")
            return None
