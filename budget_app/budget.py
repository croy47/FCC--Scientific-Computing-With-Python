class Category:
    # 
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
        self.__balance = 0
    # 
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.__balance += amount
    # 
    def check_funds(self, amount):
        if amount > self.__balance:
            return False
        else:
            return True
    # 
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.__balance += -amount
            return True
        else:
            return False
    # 
    def transfer(self, amount, new_category):
        success = new_category.withdraw(amount, f"Transfer to {new_category.category_name}")
        if success:
            self.deposit(amount, f"Transfer from {self.category_name}")
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

    def __repr__(self):
        length_cat = len(self.category_name)
        title = ((30 - length_cat) // 2) * "*" + self.category_name + (30 - (((30 - length_cat) // 2) + length_cat)) * "*"+"\n"
        # ALTERNATIVELY, string center method can also be used which implements the same logic as line above. 
        # title = self.category_name.center(30, "*")
        item_table = ''
        for item in self.ledger:
            # :<23 and :>7 format specifier makes life easier but low level implementation is simple. item_name + (30 - (length of item name + length of amount)) * space + amount
            item_table += f"{(item['description'][:23]):<23}{float((str(item['amount'])[:4])):>7.2f}\n"        
        total = f'Total: {self.__balance:.2f}'
        return title + item_table + total
# =====================================================================


def create_spend_chart(categories):
    spendings_list = []

    for category in categories:
        money_spent_a_cat = 0
        for item in category.ledger:
            money_spent_a_cat += item['amount'] if item['amount'] < 0 else 0
        # 
        spendings_list.append(money_spent_a_cat)
    
    # time to calculate the share of each cateogry in expenses.
    total_money_spent = sum(spendings_list)
    perc_each_cat = list(map(lambda money_spent_a_cat: int(round((money_spent_a_cat/total_money_spent * 100), -1)), spendings_list))
    # print(perc_each_cat)
    # CHART LOGIC BELOW
    # 
    title = "Percentage spent by category"
    chart = f"{title}"
    for perc in range(100, -1, -10):
        chart += f'\n{str(perc).rjust(3)}|'
        for perc_a_cat in perc_each_cat:
            # lol, this mistake. I was adding space even when it wasn't required.
            # whitespace mistakes are difficult to spot. Always use something like +/* etc to visualize it. 
            chart+=  ' o ' if perc_a_cat >= perc else ""
        chart = chart.rstrip()
    
    dashed_line = f"\n    {3 * len(categories) * '-'}-\n"
    chart += dashed_line
    # print(chart)
    max_length = max(map(lambda category: len(category.category_name), categories))
    bottom_strings = zip(*list(map(lambda category: category.category_name.ljust(max_length), categories)))
    # 
    for string in bottom_strings:
        chart += " " * 5
        for i in range(len(string)):
            chart += string[i] + "  " 
            if i == len(string) - 1:
                chart = chart.rstrip()
                chart += '\n'
    # 
    return chart.rstrip()
#    ====================================================

# clothing = Category('Clothing')
# clothing.deposit(3000, 'initial deposit')
# clothing.withdraw(400, 'innerwear')
# clothing.withdraw(1298, 'Shirt')
# clothing.withdraw(187.23, 'Miscellenious')
# clothing.get_balance()


# food = Category('Food')
# food.deposit(1000, 'initial deposit')
# food.withdraw(100.52, 'groceries')
# food.withdraw(100.2567, 'restaurant and more food items')
# food.withdraw(187.23, 'liquor')
# food.transfer(300, clothing)
# food.get_balance()
# # 
# # 
# rent = Category('Rent')
# rent.deposit(15000.00, 'initial deposit')
# rent.withdraw(9873, 'house rent')
# rent.withdraw(500, 'internet rent')
# rent.withdraw(500, 'television rent')
# rent.get_balance()
# # 
# travel = Category('Travel')
# travel.deposit(7000.00, 'initial deposit')
# travel.withdraw(2756, 'Metro')
# travel.withdraw(800, 'Taxi')
# travel.withdraw(1200, 'Fuel')
# travel.get_balance()



# print(food)
# print(clothing)
# print(rent)
# print(travel)
# categories = [food, clothing, rent, travel]
# print(create_spend_chart(categories))

# # x = round(243534, -2)
# # print(x)


    
        