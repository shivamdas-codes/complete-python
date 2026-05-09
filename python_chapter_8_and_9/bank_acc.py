class Account:

    def __init__(self, name, balance , account):
        self.name = name
        self.balance = balance
        self.account_no = account

    def debit(self, amount):
        self.balance -= amount
        print(f"hello {self.name} \ndebited {amount} \nyour balance is {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"hello {self.name} \ncredited {amount} \nyour balance is {self.balance}")
        
    def get_balance(self):
        return self.balance
    
acc1 = Account("shivam",1000, "1234")
acc1.credit(500)
acc1.debit(200)
print(acc1.get_balance())

acc2 = Account("rahul",3000, "4321")
acc2.credit(1000)
acc2.debit(500)
print(acc2.get_balance())