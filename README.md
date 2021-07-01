# Django Application for Representing Pedigrees

The application is made on Python 3, Django Web Framework and other technologies.

# How to run your application?

First, be sure you have installed Python 3 and PIP on your machine. You can check if you have already installed them with these commands:

```
python3 --version
pip3 --version
```

If you don't have them, install them with these commands:

```
sudo apt install python3
sudo apt install python3-pip
```

Important: Check and install the Python 3 version of the language. If you just type ```python --version``` and/or ```sudo apt install python```, you
will receive the latest version of Python 2, which will not be suitable with the project.

The next thing you should do is to install virtualenv. Virtualenv will help you with managing the packages locally in the project regardless of anything gloabally installed on your machine which is related to Python. If your have virtualenv already, pass the next command, but if you don't have it, install it with: 

```
pip3 install virtualenv
```

Your next step is to navigate to the folder and create the virtual environment. This can be made with:

```
virtualenv env_name
source env_name/bin/activate
```

If everything is done correct, you will see the name of the environment in the beginning of the command line, surrounded by brackets. The name of the environment
can by anything, so you can choose what to be.