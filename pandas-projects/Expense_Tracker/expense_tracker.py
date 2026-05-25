"""
Add expenses (date, amount, category, description)
Save to CSV
View all expenses
Show total spent
Show spending by category (using Pandas)
"""

import pandas

class TrackerBrain:
    def __init__(self,expense_csv_file):
        self.expense_csv_file = expense_csv_file
        self.expense_data_frame = pandas.read_csv(expense_csv_file)

    def check_values(self,date,amount,category,description):
        if str(type(date)) != "<class 'int'>":
            return False
        elif str(type(amount)) != "<class 'int'>":
            return False
        elif str(type(category)) != "<class 'str'>":
            return False
        elif str(type(description)) != "<class 'str'>":
            return False
        else:
            return True

    def check_duplicates(self,date,amount,category,description):
        if len(self.expense_data_frame[(self.expense_data_frame.Date == date) & (self.expense_data_frame.Amount == amount) & (self.expense_data_frame.Category == category) & (self.expense_data_frame.Description == description)]):
            return True
        else:
            return False

    def add_expense(self,date,amount,category,description):
        if self.check_values(date,amount,category,description) == False:
            return "Wont work"
        if self.check_duplicates(date,amount,category,description) == False:
            return "Wont work"
        new_data = pandas.DataFrame({
            "Date":[date],
            "Amount":[amount],
            "Category":[category],
            "Description":[description]
        })
        new_data.to_csv("expenses.csv",mode="a",header=False,index=False)

    def update_dataframe(self):
        self.expense_data_frame = pandas.read_csv(self.expense_csv_file)



    def show_total_spent(self):
        total_amount = self.expense_data_frame['Amount'].to_list()
        total_spend = sum(total_amount)
        self.update_dataframe()
        return total_spend
    

    def show_entire_expenses(self):
        #Converts the datargam to string with the index set to false, with the row number to not be shown
        return self.expense_data_frame.to_string(index=False)
    

    


    


tester = TrackerBrain("expenses.csv")
g = tester.expense_data_frame[(tester.expense_data_frame.Category == "Hello") | (tester.expense_data_frame.Category == "dead")]
print(g)
print(type(g))
print(len(g))




