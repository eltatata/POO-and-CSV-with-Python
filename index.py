import pandas as pd
# from controllers_data import set_list_users 
from controllers.controllers_data import set_list_users

df = pd.read_csv("data\\data_users.csv")

listUsers = set_list_users(df)

for user in listUsers:
    print(vars(user), "\n")
