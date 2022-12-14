# TimeKeep
![Screenshot from 2022-09-17 02-09-12](https://user-images.githubusercontent.com/99011743/190829038-b1dce0ae-adcb-47de-9599-1b0c685de4c9.png)

TimeKeep is a web-application, which gives you possibility to easily track and save your working time.

## Installation

#### 1.Clone the repository and create a virtual environment for it.

#### 2.Then use command:
```bash
pip install -r requirements.txt
```
#### to install all required packages.

####  3.After that you need to create tables using command :
```bash
python manage.py makemigrations && python manage.py migrate
```
#### 4.Create super user using command:
```bash
python manage.py createsuperuser
```
####  5.By the command from the root folder:
```bash
python manage.py runserver
```
#### you will launch application.


#### 6. And finally, navigate to 
http://127.0.0.1:8000
#### or 
http://localhost:8000

#### through your browser or by clicking on the link through your terminal.

## Usage

####  1. To run application, first you need to Log into admin panel using superuser account, which was created on step 4 of 'installation guide' using this form:

![Screenshot from 2022-09-17 02-10-41](https://user-images.githubusercontent.com/99011743/190829203-993f578e-1b89-40b6-8c5c-6ae25fcc0c1b.png)

####  2. Then You need to create Plans.



![Screenshot from 2022-09-17 01-38-22](https://user-images.githubusercontent.com/99011743/190827417-2139b963-4e24-4270-ac64-b9d1331ec53a.png)

####  'Free' with those values

![Screenshot from 2022-09-17 04-59-38](https://user-images.githubusercontent.com/99011743/190837996-36b4be1a-e9fe-46a3-a5c0-5e38bb485907.png)


####  'Pro' with those values:

![Screenshot from 2022-09-17 05-00-06](https://user-images.githubusercontent.com/99011743/190838001-32ffb69d-0a59-4ecf-b344-7828c524ba16.png)

####  Then you need SAVE changes and LOGOUT.
## NB!! DO NOT TRY TO ACCESS ANY PAGES WITH ADMIN ACCOUNT APART OF ADMIN PAGE !!!

![Screenshot from 2022-09-17 01-59-13](https://user-images.githubusercontent.com/99011743/190828674-527df2b8-b543-4c90-a8ee-9e37ddd69d9c.png)

####  3. Now, go back to the
http://127.0.0.1:8000
####  or 
http://localhost:8000

####  and register new account using this form: 

![Screenshot from 2022-09-17 02-05-06](https://user-images.githubusercontent.com/99011743/190828782-8e39f987-5509-4f67-9652-58b88f531693.png)

####  if your attempt was successful --> you will be redirected to the main page.

####  4. Then you need to create your First Team :

![Screenshot from 2022-09-17 02-02-40](https://user-images.githubusercontent.com/99011743/190828882-4ca1ed7c-37f0-4dfc-8ced-a79163f425d1.png)

####  5. Now you are fully set up an ready to go :) enjoy!


## License
[MIT](https://choosealicense.com/licenses/mit/)
