class account:
    def __init__(self, balance , acc_number):
        self.balance = balance
        self.acc_number = acc_number

    def debt(self, debit):
        self.balance -= debit
        print("balance is : ", self.get_balance())
    
    def crdt(self, credit):
        self.balance += credit
        print("remaining balace is :", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = account(int(input("enter balance: ")), int(input("enter account number: ")))
acc1.debt(int(input("Enter ammount to debit: ")))
acc1.crdt(int(input("Enter amount to credit: ")))