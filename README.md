## NEIGHBOURHOOD
An application where users are categorized into three:
* System administrator
* Neighbourhood Admin
* Normal user

## FEATURES
The features a user is able to access is dependent on the category of user, he/she is.
|System Administrators  |  Neighbourhood Admins  |   Normal Users   
| :--------------------|  :--------------------| :------------- |
|  See all users       | Add info about neighbourhoods | Sign in |
| Check users' status  | Perform all operations of a normal user | Set up a profile |
| Remove users         |   | Create a post that will be visible to everyone in a neighbourhood |
| Edit neighbourhood info |    | Change a neighbourhood when they move  |
| Create and delete a neighbourhood | |  View details of a neighbourhood |

## TECHNOLOGIES USED
* Django
* Python
* POstgres database
* Bootstrap


## SET UP INSTRUCTIONS

* Clone the repo locally to your desired folder in your PC.
   ` git clone https://github.com/Emmanuel-9/Neighbourhood `

* Open the cloned application in an IDE of choice such Sublime Text, VSCode and many others.

* Create a virtual environment to for the application. This can on the terminal using the command
  ` python3.6 -m venv --without-pip <name_of_the_virtual_environment> `
  If giving the virtual environment is a bit difficult, you can assign it the default name **VIRTUAL**
  
* Activate the created virtual environment 
  ` source virtual/bin/activate `

* In the activated virtual environment, install pip which would be used to install dependencies in Python, which can be using the   command: ` curl https://bootstrap.pypa.io/get-pip.py | python `

* Install the dependencies used in the application ` pip install -r requirements.txt `.

* Create an .env file which contains the environment variables
```
SECRET_KEY='<Secret_key>'
DEBUG=True 
DB_NAME='<db_name>'
DB_USER='<db_username>'
DB_PASSWORD='<db_password>'
DB_HOST='127.0.0.1'
MODE='dev' 
ALLOWED_HOSTS='.localhost','floating-falls-55062.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```
* Run the application 
` python3 manage.py runserver `


## LICENSE
- This project is licensed under the MIT License - see the LICENSE.md file for details.


## AUTHORS
* Andrew Yaah
* Joan Wanjiku
* Emmanuel Orega



