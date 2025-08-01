class Person:
    def __init__(self, fullname, age, id):
        self.fullname = fullname
        self.age = age
        self.id = id

class BankAccount:

    def __init__(self,number,owner,amount):
        self.number = number
        self.owner =owner
        self.amount = amount

    def transfer_to(self,acc,amount):
        if self.amount > amount:
            self.amount -= amount
            acc.amount += amount
            print(f"Acc1 owner mr/ms {self.owner.fullname} transferred {amount} to acc2 owner mr/ms {acc.owner.fullname}")
        else:
            print("Insufficient amount")

p1 = Person("Giorgos Katramidis",31, "AA0000")
p2 = Person("Teo Savvidis", 30,"AB11111")
acc1 = BankAccount(123456789876543,p1,1000)
acc2 = BankAccount(596879403201, p2, 2000)
print(f"acc1 amount is {acc1.amount}")
print(f"acc2 amount is {acc2.amount}")
acc1.transfer_to(acc2,999)
print(f"acc1 amount is {acc1.amount}")
print(f"acc2 amount is {acc2.amount}")
print(acc1.owner.id)
#valame to class person mesa sto class account