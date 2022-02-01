# Python Virtual Environments
A virtual environment is a Python environment such that the **Python interpreter**, **libraries** and **scripts** installed into it are **isolated** from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.
Virtual environments are specially useful when you want to work with **different versions of libraries**, or when you are **collaborating with people** and you have to specify the requirements so that your code works.

## Creating virtual environments
To create a virtual environment just type ```virtualenv <name>``` and a new environment with its corresponding folder will be created. You can specify the python version that you want to use by setting the option ```-p``` followed by the corresponding path (e.g. ```-p /usr/bin/python3```).
