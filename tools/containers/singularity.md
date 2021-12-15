# Basic tutorial for building singularity containers

## Basic definitions
### The ```build``` command
To build a singularity container, you must use the ```build``` command. The ```build``` command installs an OS, sets up your container’s environment and installs the apps you need. You need root priviledges to build containers. To use the ```build``` command, we need a definition file.

If you want to avoid using root priviledges because of security reasons, you can use the ```--fakeroot``` option. Doing so allows you to pretend to be the root user inside of your container without actually granting singularity elevated privileges on host system.

### The Singularity definition file
A Singularity definition file is a set of instructions telling Singularity what software to install in the container.
Example:
```
BootStrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian/

%runscript
    echo "This is what happens when you run the container..."

%post
    echo "Hello from inside the container"
    apt-get -y --allow-unauthenticated install vim

```
### Sandbox containers
When building a container, we can specify the option ```--sandbox```. This command tells Singularity that we want to build a special type of container (called a sandbox) for development purposes. This is great when you are still developing your container and don’t yet know what to include in the definition file. These containers are directories.

### The ```shell``` command
We can enter the container with the ```shell``` command. In order to modify the container (and for example install packages), we need to specify the ```--writable``` option. To do so, you need to enter the container with sudo priviledges. Once you have installed your required packages, you need to add them to the path. For example ```export PATH=$PATH:/usr/games```.

### SIF files
Singularity can build containers in several different file formats. The default is to build a SIF (singularity image format) container that uses squashfs for the file system. SIF files are compressed and immutable making them the best choice for reproducible, production-grade containers. To build this type of containers, ommit the ```--sandbox``` option in the ```build``` command. 

## Steps
1. Create your definition file.
2. Build either a sandbox container (```sudo singularity build --sandbox lolcow lolcow.def```) or a SIF container (```sudo singularity build lolcow.sif lolcow.def```)
3. Enter the container (```singularity shell lolcow```). Recall that you need to enter the container with root priviledges and to specify the flag ```--writable``` in order to modify the container.
4. *Bonus*: to view the definition file of an already built container use ```singularity inspect --deffile  lolcow.sif```

Source: https://singularity-tutorial.github.io/03-building/
