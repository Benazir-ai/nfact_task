userStorage = []

class UserManager:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def addUser(id, name):
        user = UserManager(id, name)
        userStorage.append(user)

    @staticmethod
    def getUser(id_for_search):
        for i in userStorage:
            if i.id == id_for_search:
                print(i.name)
        print("null")

    @staticmethod
    def deleteUser(id_for_delete):
        for i in userStorage:
            if i.id == id_for_delete:
                userStorage.remove(i)
                return True
        return False

    @staticmethod
    def findUserByName(name_for_search):
        ids = []
        for i in userStorage:
            if i.name == name_for_search:
                ids.append(i.id)
        return ids

is_continue = 1
while(is_continue):
    action = int(input("Which action would you like to do (1-addUser, 2-getUser, 3-deleteUser, 4-findUserByName)"))
    if action == 1:
        name = input("Name: ")
        id = int(input("ID: "))
        UserManager.addUser(id, name)
        print(f'user ${name} was added')
    elif action == 2:
        id = int(input("ID: "))
        UserManager.getUser(id)
    elif action == 3:
        id = int(input("ID: "))
        print(UserManager.deleteUser(id))
    elif action == 4:
        name = input("Name: ")
        print(UserManager.findUserByName(name))
    else:
        print("Not correct value")
    is_continue = int(input("If you wanna continue press 1 or if you wanna stop press 0: "))
    if is_continue == 0:
        print("Thanks for using! Programm is going to finish now. ")
    is_continue = bool(is_continue)

