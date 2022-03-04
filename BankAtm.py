class Atm(object):
     def __init__(self,atm_card_number, pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
    
     def CashWithdrawal(self):
        print("Cash Withdrawn")
    
     def BalanceEnquiry(self):
        print("Balance Enquired")
    
Atms=Atm("1234 5678 9012","9999 9999")

print("Details of ATM Card:")
print("ATM Card Number: ", Atm.atm_card_number)
print("Pin Number: ", Atm.pin_number)
print(Atm.CashWithdrawal())
print(Atm.BalanceEnquiry())