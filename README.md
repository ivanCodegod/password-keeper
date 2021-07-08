# Password Keeper
![GitHub language count](https://img.shields.io/github/languages/count/ivanCodegod/password-keeper?logo=GitHub)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ivanCodegod/password-keeper?color=yellow)
![GitHub repo size](https://img.shields.io/github/repo-size/ivanCodegod/password-keeper?logo=GitHub)

Password Keeper is a program that allows you to:
- Storage your 'information' like __password__, __login__ and __mail__.
- Get back your 'information' you already store.


## How To Use?
1. Create file 'database.ini.txt' and make it for yourself:

``database.ini.txt``
```txt
    [postgresql]
    host=localhost  # your host
    database=some  # name of your database
    user=abstract  # your username
    password=123  # Your password
```
2. Look at the contents of the file 'requirements.txt' and download libraries
which you don't have:
   
``For Linux``
```txt
    sudo pip3 install 'library name'
```
``For Windows``
```txt
    pip3 install numpy | pip install numpy
```

3. To run the program, write:
```txt
    python db_part.py
```

## Available commands
- get 

Get your information that you already save.
- set

Set your information into a storage.
- all

See all Title's of information that you already save.
- q

Quit the program.
- comm
Open navigation panel and show all available commands.