
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)

## General info
This is a python cli application that takes user input and returns information about the Docker containers on the system. It uses the docker-py python api library and seeks to replicate some of the functionality of the ```docker ps``` native application. 
## Technologies
Project is created with:
* python: 3.8.1
* docker-py python library: 1.10.6
* columnar python library: 1.3.1
	
## Setup
To run this project, clone it locally and install the modules from requirements.txt 
```
$ pip install -r requirements.txt
```
Once the modules have been installed you will need to run the python application as root, due to the fact that docker typically requires it (unless you have installed Docker with a non-root setup). Run the following command to search for all Docker containers on your system:

```
$ python3 py_docker_ps/main.py
```
## Usage
```sh
$ python3 trellocard 
```

py_docker_ps uses the following options:

- [no arguments]    Show only running containers
- `-a`  `--all` 	  Show all containers (default shows just running)
- `-n`  `--last`	  Show n last created containers (includes all states)
- `-l`  `--latest` 	Show the latest created container (includes all states)
- `-`    `--notrunc` Don't truncate output'
- `-q`  `--quiet`	  Only display container IDs
- `-h` 		`--help` shows a helpful usage message

sample output:

```
$ python3 py_docker_ps/main.py --all 

  CONTAINER ID  IMAGE         COMMAND                CREATED     STATUS                     PORTS  NAMES                   
    
  ef828f21c101  3ae9bf4c115a  /bin/sh -c 'echo "CRE  1636894144  Exited (1) 26 hours ago           thirsty_jones           
  4afdc8df9247  078bc2297574  /bin/sh -c 'fpm --inp  1636894066  Exited (1) 26 hours ago           festive_sutherland  
```
## Roadmap
Implement ```filter``` and ```format```
Add test coverage
