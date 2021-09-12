# givekudo
Give Kudos to your teammate! 

### 1. Clone the project on your system
```git clone https://github.com/mridubhatnagar/kudos.git```

### 2. Go inside in the project directory.
```cd kudos```

### 3. Create virtual environment
```virtualenv <enviornment_name>```

### 4. Activate environment
```source <enviornment_name/bin/activate>```

### 5. Configure the database based on your local database credentials in settings.py

### 6. Run server
``` python manage.py runserver```

### Features
1. Only logged in users can give kudos.
2. Logged in user can only give kudo to folks within their organization.
3. Number of kudos that can be given by an individual in current week is 3.
4. Personal Dashboard - Dashboard to see who has given, how many kudos to the logged in user.
5. User login, signup pages.
6. No backdated kudos can be given. Only current week is considered

### DB Schema
![DB Schema](https://user-images.githubusercontent.com/16894718/75120009-f819e900-56ad-11ea-9191-23f7303769a8.png)

### home when no user is logged in 
![logged_out_home](https://user-images.githubusercontent.com/16894718/75120048-416a3880-56ae-11ea-815e-af8f0a139a3e.png)

### home when user is logged in
![loggedin_home](https://user-images.githubusercontent.com/16894718/75120058-6363bb00-56ae-11ea-877a-daae357134d5.png)

### SignUp 
![signup](https://user-images.githubusercontent.com/16894718/75120083-88582e00-56ae-11ea-83fb-a1b10b6d8254.png)

### LogIn
![login](https://user-images.githubusercontent.com/16894718/75120093-a2920c00-56ae-11ea-89d8-f885b28a6a2f.png)

### GiveKudo
![givekudo](https://user-images.githubusercontent.com/16894718/75120110-b9d0f980-56ae-11ea-991d-37a7f65a253a.png)

### Personal Dashboard
![Screenshot from 2020-02-24 02-01-17](https://user-images.githubusercontent.com/16894718/75120119-e08f3000-56ae-11ea-991d-1a8ab59d4cef.png)





