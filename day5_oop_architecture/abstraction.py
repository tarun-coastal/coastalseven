from abc import ABC, abstractmethod


# Abstract Class
class Bank(ABC):

    @abstractmethod
    def interest_rate(self):
        pass


# Child Class 1
class SBI(Bank):

    def interest_rate(self):
        print("SBI Interest Rate = 6.5%")


# Child Class 2
class HDFC(Bank):

    def interest_rate(self):
        print("HDFC Interest Rate = 7.2%")


# Child Class 3
class ICICI(Bank):

    def interest_rate(self):
        print("ICICI Interest Rate = 7.0%")


# Usage
banks = [SBI(), HDFC(), ICICI()]

for bank in banks:
    bank.interest_rate()