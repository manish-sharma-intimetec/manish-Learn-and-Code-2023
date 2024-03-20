from flask import render_template, request
from ValidateUser import validateUser
from EditUserInDB import editUserInfo

def routes(app):
    @app.route('/')
    def renderUserLoginPage():
        return render_template('userLogin.html')

    @app.route('/authentication', methods=["POST", "GET"])
    def authenticateUser():
        userName = request.form['userName']
        userPassword = request.form['userPassword']
        isValid = validateUser(userName, userPassword)

        if isValid == True:
            return render_template("adminPage.html")
        return "Invalid Crendentials"
    

    @app.route('/editUser', methods=["POST", "GET"])
    def editUser():
        userName = request.form['userName']
        newUserName = request.form['newUserName']
        newUserPassword = request.form['newUserPassword'] 
        newUserType = request.form['newUserType'] 

        print("userName =", userName)
        editUserInfo(userName, newUserName, newUserPassword, newUserType)
        return 'a'
        