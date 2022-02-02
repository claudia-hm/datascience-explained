<h1 align="center">
   <img src="https://www.docker.com/sites/default/files/d8/2019-07/Moby-logo.png" width="100"> <br>
   Docker 
</h1> 

### Basic concepts

#### Docker images and docker containers

A **Docker image** is an immutable (unchangeable) file that contains the source code,  libraries, dependencies, tools, and other files needed for an  application to run. A **Docker container** is a virtualized run-time environment where users can isolate  applications from the underlying system. These containers are compact,  portable units in which you can start up an application quickly and  easily.

Images  can exist without containers, whereas a container needs to run an image  to exist. Therefore, containers are dependent on images and use them to  construct a run-time environment and run an application.

#### Dockerfiles

Dockerfiles are used to build images. It is a list of commands that will be sent to the docker engine, which will read them from the top to the bottom. Here is an example dockerfile for building a python image:

``` 
# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./server.py" ] 
```

As order of commands matters, we need to place the instructions for layers that change frequently after the ones that incur less changes. This will enable caching when rebuilding the image.

The first command is the FROM. When building images we usually start from a base image that is verified. We also specify the version that we want to use. Then, the WORKDIR specifies the directory to use. ENV sets up an environment variable (not present in this example), that we give a name. The COPY command moves the required files into the working directory, or whatever directory we speciy. The RUN command will state what commands to run inside the docker. CMD specifies the default command to execute when running the container.

The Dockerfile is then processed by the Docker builder which generates the Docker image. Then, with a simple *docker run* command, we create and run a container with the Python service.

### Steps

Bellow I summarize the steps that I've followed to create a container running a flask python app. You can find the files and source code in ```./docker-tutorial/``` 

1. Create the python source code that you want to execute in your app. In my case, I saved it in the file ```server.py``` . The code should be saved by itself in a folder named ```src```. Put all the required dependencies and libraries inside a file called ```requirements.txt``` so that they can be installed inside the container. 

2. Set up your dockerfile with the needed commands and save it to a file named simpy ```Dockerfile```. For this tutorial, I used the dockerfile above, where I specify the base image, copy the requirements file, install the dependencies, copy the code and specify the comman to run on container start. The  final structure of your folder should be:

   ```
   docker-tutorial 
   ├─── requirements.txt 
   ├─── Dockerfile
   └─── src   
   	└─── server.py
   ```

3. Build your image from the docker file. Run the command  ```docker build -t myimage .``` where ```myimage``` can be replaced by a custom name. We can visualize the images stored in our machine with the command ```docker images``` 

4. Run the container. In our case, ```docker run -d -p 5000:5000 myimage``` will run our image ```myimage``` in the background (flag ```-d```) and map the port 5000 of the host machine to the port 5000 of the container. Docker containers can connect to the outside without any configuration, but the outside world cannot connect to a Docker container by default. This is the reason why we must explicitly state the port mapping.

