<h1 align="center">🐍Sistema de gestión de condominios y edificios
🐍</h1>
<h4 align="center">🫧For [GBS]🫧. </h4>


The backend is the first segment of the Building and Condominium Management System for gbs project that will collectively cover the fundamentals of high-level programming. The objective of this project is to implement in our system the administration of condominiums and buildings that can make ordinary and extraordinary charges to the tenants in an automated way, see the history of receipts and their details. As part of the administration, you can see income and expenses, create new condominiums, owners and tenants, assign them to your building and/or department.


Functionalities from the database:

- Create a new object (ex: a new User or a new building)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

Table of Content

- Environment
- Installation
- File Descriptions
- Usage
- Examples of use
- Bugs
- Authors
- License

## Environment

This project is interpreted/tested on Ubuntu 20.04 LTS using python3 (version 3.8.10)

## Installation

- Clone this repository: git clone https://github.com/GerardoMP18/web-condominio-edificio-backend.git
- Access web-condominio-edificio-backend directory:  cd web-condominio-edificio-backend
- run api: sudo python3 -m api.app
- run mysql: sudo service mysql start 

The API contains the database entry point:

`api/views/` directory contains classes used for this project:

_`buildings.py`_ - Methods that handle all default
RestFul API actions for buildings

-  `def get_buildings(condominium_id=None):` - Method that returns the list of all buildings objects
- `get_building_id(building_id=None):` -  Method that returns the values of a building by means of their ID
- `def delete_building(building_id=None):` - Method that deletes a building by their ID
- `def post_building(condominium_id=None):` - Method that creates a building
- `def put_building(building_id=None):` - Method that updates a building by their ID

_`bulk_load.py`_ - RestFul API bulk_load for users

- `def allowed_file(filname):` - Method to validate the allowed extensions
- `def bulk_load():` - Endpoint that loads the excel file to then carry out the bulk load of user and income data

_`condominiums.py`_ - Methods that handle all default
RestFul API actions for condominiums

- `def get_condominiums():` - Method that returns the list of all condominium objects.
- `get_condominium_id(condominium_id=None):` - Method that returns the values of a condominium by means of their ID
- `def delete_condominium(condominium_id=None):` - Method that deletes a condominium by their ID
- `def post_condominium():` - Method that creates a condominium
- `put_condominium(condominium_id=None):` - Method that updates a condominium by their ID
- ``

_`departaments.py`_ - Methods that handle all default
RestFul API actions for departaments
- `def get_departaments(building_id=None):` - Method that returns the list of all departaments objects
- `def get_departament_id(departament_id=None):` -  Method that returns the values of a departament by means of their ID
- `def delete_departament(departament_id=None):` - Method that deletes a departament by their ID
- `def post_departament(building_id=None):` - Method that creates a departament
- `def put_departament(departament_id=None):` - Method that updates a departament by their ID

_`departaments_users.py`_ - Methods that handle all default
RestFul API actions for departaments_users
- `def get_departaments_users(user_id=None):` - Method that returns the list of all departaments_users objects
- `def delete_departament_user(user_id, departament_id):` - Method that deletes a departament_user by their ID
- `def post_departament_user(user_id, departament_id):` - Method that link departament user

_`index.py`_ -  Module Index
- `def status():` Status of API
- `def number_register():` - Method that returns a dictionary with all the tables and the number of their records

_`login.py`_ - RestFul API that is responsible for verifying if
the users are in the database to be able
to enter the system

- `def login_user():` - Method that verifies if a user can access the system through their email and password

_`user.py`_ - Methods that handle all default
RestFul API actions for users
- `def get_owners():` - GET method that returns all owners
- `def get_tenants():` - GET method that returns all tenants
- `def get_users():` - Method that returns the list of all user objects
- `def get_user_id(user_id=None):` - Method that returns the values of a user by means of their ID
- `def delete_user(user_id=None):` - Method that deletes a user by their ID
- `def post_user():` - Method that creates a user
- `def put_user(user_id=None):` Method that updates a user by their ID


`database/procedure` -  database processes
- `sp_add_building.sql`_ - procedure create new building 
- `sp_add_condominium.sql` - SP for the create new condominium 
- `sp_add_departament.sql` - procedure create departament 
- `sp_add_departament_user.sql` - procedure link departament_user
- `sp_add_user.sql` - SP for the create new user 
- `sp_update_building.sql` - procedure update building
- `sp_update_condominium.sql` - procedure update condominium -  
- `sp_update_departament.sql` - procedure update departament
- `sp_update_user.sql` - procedure update user

`models/` -  directory contains classes used for this project:
_`base_model.py`_ -  This module defines a base class for all models
- `class BaseModel:` - The BaseModel class contains methods needed by the other classes 
- `def __str__(self):` - String representation of a class
- `def new(self, procedure):` - Method that sends the dictionary full of object information to the create method of Db_storage. If the dictionary contains (password) then it is encrypted with  ashlib and then sent
- `def to_dict(self):` - Method that prepares the given dictionary to only display the actual data


_`building.py`_ - Module that defines the Building class
- `class Building(BaseModel):` - This class defines a building by various attributes
- `def buildings_get():` - method that returns all the buildings within a condominium by their ID
- `def building_get():` - method that returns a building by its ID

_`condominium.py`_ - Module that defines the Condominium class
- `class Condominium(BaseModel):` This class defines a condominium by various attributes

_`departament.py`_ - Module that defines the Departament class
- `class Departament(BaseModel):` - This class defines a departament by various attributes

_`departament_user.py`_ - Module that defines the Departament_user class

- `class Departament_User(BaseModel):` - This class defines a departament_user by various attributes

_`user.py`_ - Module that defines the User class
- `class User(BaseModel):` - This class defines a user by various attributes

_`__init__.py`_ - initialize the models package

`models/engine/` 

_`db_storage.py`_ - Module that connects to the database

- `class DBStorage():` Class that interacts with
    the MySQL database
- `def __init__(self):` Method that initializes the
        connection to the database
- `def all():` Method that consults in the current session
        of the database and returns all the data
        of the indicated table
- `def create():` Method that adds values to the
        indicated table of the current session
- `def get():` Method that obtains and returns the values
        of a single object of the current session
- `def to_dict():` Method that returns a dictionary
        to be displayed in the APIs
_ `def update(self):` - Method that receives a dictionary from
        the api and an id, to update its indicated data
- `def verify():`  Method that checks if an
        email is in the database
- `def delete():` - Method that receives the name of the
        table and the id of the data that I want
        to delete from the database
- `def count(self):` - Method that returns a dictionary with all
        the tables and the number of their records
- `def filters():` - Method that filters any table with Where
- `def create_many():` Method that allows further insertion through the user and income tables
- `def get_id():` - Method to obtain the id according to the attribute searched for
        by fixed word

`template_carga/` -  

_`carga_masiva_user.xlsx`_ - excel for mass loading of condominium and building to condominium management systems


## Bugs
No known bugs at this time.

## Authors
- Fernando J. Gonzales Pradinett. - [Github]()[Twitter]()
- Gerardo Marín. - [Github]()[Twitter]()
- Paolo Abarca. - [Github]()[Twitter]()
- Dhanna Palomino. - [Github]()[Twitter]()
- Juan Salinas. - [Github]()[Twitter]()

## License
Public Domain. No copy write protection.





