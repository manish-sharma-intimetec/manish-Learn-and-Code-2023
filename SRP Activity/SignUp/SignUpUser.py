class SignUpUser:

    def connectionWithUserDatabase():
        try:
            connection = True
        except Exception:
            print("Error Occurred while Connecting to DB")
            return None
        
        return connection
    
    def createUserInDataBase(connection, userInfo):
        try:
            connection.createUser(userInfo.name, userInfo.password, userInfo.userName)
        except Exception:
            print("Error Occurred while creating user in DB")
            return False
        finally:
            connection.close()
        
        return True
            
    def fetchUserData(connection, userId, permission):
        if permission == True:
            return connection.get(userId)
        return "Permission Denied"

    def notification(connection, userInfo, notificationMssg):
        if connection.fetch(userInfo.id) == True:
            return notificationMssg
        return "Signup Failed"
    
    def closeConnection(connection):
        connection.close()


