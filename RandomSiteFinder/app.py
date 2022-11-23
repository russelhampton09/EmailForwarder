from api import api, app
from api.registerController import RegisterController
from data import email_repo

def start():   
    api.add_resource(RegisterController, '/register',resource_class_kwargs={'email_repo': email_repo})
    app.run(debug=True, port=5001)

if __name__ == '__main__':
    start()

