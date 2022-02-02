<h1 align="center">
   <img src="https://i.pinimg.com/originals/c7/b8/11/c7b8113247fecd83bd9b5ed5bd3f34d5.png" width="100"> <br>
   Linux concepts 
</h1> 

## Definitions
* **Interactive shell**: interactive shells read commands from user input. Usually, they read a set of files on activation, display a prompt and enable job control. 
* **Non-interactive shells**: these shells do not allow user interaction. They are often run from scripts. Init and startup scripts are necessarily non-interactive, since they must run without human intervention. Many administrative and system maintenance scripts are likewise non-interactive. 
* **Login-shell**: a login shell is created after a successful login of user. For example, when you login t a Linux system via terminal, SSH or switch to user with “su -” command. 
* **Non-login shell**: Non Login Shell is the shell, which is started by the login shell. For example, A shell which you started from another shell or started by a program etc.
To check if you are in a login or a non-login shell type ```echo $0```. If the output is ```bash``` you are in a non-login shell, if the output is ```-bash``` you are in a login shell. Tmux shells are usually login by default.

## Tips
* Tmux shells are usually login by default. You might be interested in having non-login shells in your tmux window, for example because you want to keep your aliases or configuration. To do so, create a ~/.tmux.conf file if needed and add the following line ```set -g default-command "${SHELL}"```.

## References
* https://tldp.org/LDP/abs/html/intandnonint.html
* https://tecadmin.net/difference-between-login-and-non-login-shell/
