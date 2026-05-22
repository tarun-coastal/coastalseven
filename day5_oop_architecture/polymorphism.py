class Payment:

    def pay(self, amount):
        print("Processing payment...")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class Card(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Credit/Debit Card")


class Cash(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Cash")


# Common function ---polymorpshism
def make_payment(payment_method, amount):
    payment_method.pay(amount)


# Objects
upi = UPI()
card = Card()
cash = Cash()

# Same function, different behavior
make_payment(upi, 500)
make_payment(card, 1200)
make_payment(cash, 300)