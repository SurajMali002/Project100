class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-50000")
        
    def withdrawl(self,withdraw):
        new_amount = 100 - withdraw
        print("You have withdrawn amount "+str(withdraw) + ". Your remaining balance is "+ str(new_amount))



def main():
    print("Welcome to State Bank! ")
    Account = input("Please enter your Account number: ")
    Card_number = input("Insert your Card number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):       
        choose = int(input("Add withdraw: "))
        if (choose == 1):
           withdraw = int(input("Enter the amount:- "))
           new_user.withdrawl(withdraw)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()