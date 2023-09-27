class SecurityError(Exception):
    def __init__(self, message ):
        print(message)
    def logout(self):
        print('logging u out from all the devices')
        

class Browser:
    def __init__(self, name, email, password, device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device
        
    def login(self, email, password, device):
        if device != self.device:
            raise SecurityError('not the same device as registered with')
        if email == self.email and password == self.password:
            print('WELCOME TO THE BROWSER')
        else:
            print('wrong credentials')
            
            
        
user = Browser('Abhimanyu', 'abhimanyu22nits@gmail.com', 'huehuehue', 'android')
#let's assume that device's address or something would be saved in device string above
#there could be a code written for the to get the deive's name, number and model, but not here

try:
    user.login('abhimanyu22nits@gmail.com', 'huehuehue', 'windows')
except SecurityError as e:
    e.logout()
else:
    print(user.name)
finally:
    print('database connection closed')