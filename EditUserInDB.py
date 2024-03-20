import json

def editUserInfo(userName, newUserName, newUserPassword, newUserType):
    # editUserIndex = -1
    usersData = []

    with open('users.json', 'r') as usersFile:
        usersData = json.load(usersFile)
        print(usersData, len(usersData))

        for i in range(len(usersData)):
            print(usersData[i]['userName'])
            if usersData[i]['userName'] == userName:
                print("matched")
                del usersData[i]
                usersData.append(
                    {
                        "userName": newUserName,
                        "userPassword": newUserPassword,
                        "userType": newUserType
                })
                # json.dump("", usersFile)
                break

    with open('users.json', 'w') as usersFile: 
        json.dump(usersData, usersFile)
    
    return False