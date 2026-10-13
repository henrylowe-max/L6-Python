# OOP Syntax Demo

class Account:
    description = str() # public
    __balance = float() # private
    _interestRate = float() # protected

#constructor
def __init__(self,description:str,monthlyInterest:float):
    self.description=description
    self.setInterest(monthlyInterest)
    self.__balance = 0.0

def setInterest(self,monthlyInterest):
    if 0 <= monthlyInterest and monthlyInterest <= 1:
        self._interestRate = monthlyInterest
    else:
        print("Interest not set as it must be between 0 and 1")
        print(f"interest rate is still {self._interestRate:.2f}")


"""
def __str__(self):
    value = "-"*10
    value += f"\nAccount Description : {self.description}"
    value += f"\nAccount Balance {self.__balance:.2f}"
    value += f"\nMonthly Interest {self._interestRate:.2f}"
    value += f"\n+ {'-'*10}\n"

    return value
"""
def getBalance(self)->float:
    return self.__balance

def deposit(self,amount:float):
    if amount >= 0:
        self.__balance += amount
    else:
        print(f"deposit failed {amount:.2f} must be positive.")

def withdraw(self,amount:float):
    if amount < 0:
        print(f"withdraw failed {amount:.2f} must be positive.")
        return

    if self.__balance - amount >= 0:
        self.__balance -= amount
    else:
        print(f"withdraw failed insufficient funds for {amount:.2f}")

"""
def monthlyInterest(self):
    self.__balance *= 1+self._interestRate
    13/10/2026, 05:58 bank.py

localhost:51809/562206db-d47f-43e0-bbcd-6e21740b4817/ 1/2
"""
def testAccount():
    savings = Account("Savings Account",0.05)
    print("savings after instantiation")
    print(savings)

    print("depositing £100")
    savings.deposit(100)
    print(savings)

    print("Earning monthly interest")
    savings.monthlyInterest()
    print(savings)

    print("Fail deposit test -100")
    savings.deposit(-100)
    print(savings)

    print("Withdrawing £10")
    savings.withdraw(10)
    print(savings)
    print("Fail interest test setInterest(5)")
    savings.setInterest(5)
    print(savings)

    print("Account status after failed tests")
    print(savings)

if __name__ == "__main__":
    testAccount()