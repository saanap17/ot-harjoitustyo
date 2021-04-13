import os.path

class Users:
    def __init__(self,filename):
        self.users = filename
    
    def add_user(self,username,password):
        if not self.check_user(username):
            string = 'user=' + username + ' , ' + 'password=' + password + ' \n' 
            file = open(self.users, 'a+')
            file.write(string)
            file.close()
            return True
        else:
            return False
    
    def check_user(self,username):
        if not os.path.exists(self.users):
            open(self.users,'a+').close()
    
        file = open(self.users, 'r')
        data = file.read().split()
        file.close()
        string = 'user=' + username
        
        if string in data:
            return True
        return False
    
    def check_login(self,usr,psw):
        if not os.path.exists(self.users):
            open(self.users,'a+').close()
            
        file = open(self.users, 'r')
        data = file.read()
        file.close()
        string = 'user=' + usr + ' , ' + 'password=' + psw + ' '
        
        if string in data:
            return True
        return False