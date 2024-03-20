import json

def validateUser(userName, userPassword):
    with open('users.json', 'r') as usersData:
        usersData = json.load(usersData)
        print(usersData, len(usersData))

        for i in range(len(usersData)):
            if usersData[i]['userName'] == userName and usersData[i]['userPassword'] == userPassword:
                return True
        return False