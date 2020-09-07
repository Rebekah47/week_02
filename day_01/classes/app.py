from modules.bank_account import *

bank_account = BankAccount("John", 500, "Business")
bank_account_personal = BankAccount("Steve", 20, "Personal")
print(bank_account.holder_name)
print(bank_account_personal.holder_name)

bank_account.holder_name = "Ada"
print(bank_account.holder_name)

bank_account.pay_in(50)
print(bank_account.balance)

bank_account.pay_monthly_fee()
bank_account_personal.pay_monthly_fee()
print(bank_account.balance)
print(bank_account_personal.balance)

# account = {
#     "holder_name": "John",
#     "balance" : 500,
#     "type": "business"

# }

# print(get_account_name(account))
