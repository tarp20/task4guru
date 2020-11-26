# task4guru
 
dec_task

Deployed: https://task4guru.herokuapp.com

Installation Instructions:

Clone the project. git clone git@github.com:tarp20/task4guru.git

cd intro the project directory

cd dec_task

3.Create a new virtual environment using Python 3.9 and activate it.

$ python3 -m venv env $ source env/bin/activate

4.Install dependencies from requirements.txt: (env)$ pip install -r requirements.txt

5.Migrate the database. (env)$ python manage.py migrate

6.Run the local server via: (env)$ python manage.py runserver

DONE! The local application will be available at http://localhost:8000, and the browsable api will be available at http://localhost:8000/api/cars

Docker:

1) Install Docker— https://docs.docker.com/get-docker/
1.1) Install docker-compose - https://docs.docker.com/compose/install/
2.) Make a clone of the git repository - git@github.com:tarp20/task4guru.git
3.) Build the build using docker-compose build (to run docker-compose up)

Functionality of the application:

POST api/cars: requires 2 fields (Make_Name,Model_Name) checks if this car exists if yes add to database

GET api/cars: Display all cars in database with average rating 

POST api/rating: You Can rate car in database by using car_id  

Get api/popular  Displaying сar ordered by the number of ratings
