class User:
    def __init__(self, name, email, password, creation_date, premium) -> None:
        self.name = name
        self.email = email
        self.__password = password
        self.creation_date = creation_date
        self.premium = premium
        self.access = []

    def ShowInfo(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nCreation date: {self.creation_date}\n")

class UserPremium(User):
    def __init__(self, name, email, password, creation_date, premium) -> None:
        super().__init__(name, email, password, creation_date, premium)
        self.access = ["Settings superuser", "Admin", "Delete"]

    def ShowInfo(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nCreation date: {self.creation_date}\n")