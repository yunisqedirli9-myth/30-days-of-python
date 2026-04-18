class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = [] 
        self.expenses = [] 

    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def total_income(self):
        return sum(item['amount'] for item in self.incomes)

    def total_expense(self):
        return sum(item['amount'] for item in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = f"Hesab Sahibi: {self.firstname} {self.lastname}\n"
        info += f"Ümumi Gəlir: {self.total_income()}\n"
        info += f"Ümumi Xərc: {self.total_expense()}\n"
        info += f"Cari Balans: {self.account_balance()}"
        return info

person = PersonAccount("Ali", "Aliyev")

person.add_income(2500, "Aylıq Maaş")
person.add_income(500, "Bonus")
person.add_expense(800, "Ev kirayəsi")
person.add_expense(300, "Market xərcləri")

print(person.account_info())
