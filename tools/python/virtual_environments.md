# Python Virtual Environments <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" width="30">
A virtual environment is a Python environment such that the **Python interpreter**, **libraries** and **scripts** installed into it are **isolated** from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.
Virtual environments are specially useful when you want to work with **different versions of libraries**, or when you are **collaborating with people** and you have to specify the requirements so that your code works.

## Creating virtual environments
To create a virtual environment just type ```virtualenv <name>``` and a new environment with its corresponding folder will be created. You can specify the python version that you want to use by setting the option ```-p``` followed by the corresponding path (e.g. ```-p /usr/bin/python3```). 

## Activating your virtual environment
After creating your virtual environment you need to activate it before working on the project. The command is ```source <name>/bin/activate```. You may notice that the  command prompt has slightly changed, displaying the name of your virtual environment between parenthesis. This means that you are currently inside the virtual environment.

## Installing dependencies
Now, you can install all the required dependencies for your project using ```pip```. For example ```pip install sktime==0.5.3```. This library will be placed inside your virtual dependency folder <name> and will be isolated from your system python.
  
:bulb: **Tip**: you can list all the required packages in a ```requirements.txt``` file, such as the one in this folder and install them all at once with the command ```pip install -r requirements.txt```. Also, if you have already installed some packages in your virtual environment and you want to save to a file all the versions that you are using, you can do ```pip freeze > requirements.txt``` so that next time you can install them directly.
  
## Deactivating your virtual environment
  You can exit your virtual environment by typing ```deactivate```.

  
## Bonus: using a virtual environment as kernel for Jupyter notebook
  1. Create (```virtualenv <name>```) and activate (```source <name>/bin/activate```) your virtual environment. 
  2. Install all the required packages
  3. Create jupyter kernel from your virtual environment with the command ```ipython kernel install --user --name=<name>```
  4. Open Jupyter as usual, and change your kernel to ```<name>```
  5. To delete your new kernel use ```jupyter-kernelspec uninstall <name>```
