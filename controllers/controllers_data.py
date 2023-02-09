import sys
path = sys.path[0].replace("controllers", "models")
sys.path.append(path)

from models.models import User, UserPremium

def set_list_users(data):
    listUsers = list()
    
    for index, row in data.iterrows():
        name, email, password, creation_date, premium = row.tolist()
        
        if premium:
            user = UserPremium(name, email, password, creation_date, premium)
        else: 
            user = User(name, email, password, creation_date, premium)

        listUsers.append(user)

    return listUsers