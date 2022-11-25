from api import api, app
from api.registerController import RegisterController, TestController
from data import email_repo

def start():   
   # api.add_resource(RegisterController, '/register',resource_class_kwargs={'email_repo': email_repo})
    api.add_resource(TestController, '/test')
    app.run(debug=False, port=5002)

if __name__ == '__main__':
    start()

