#!/bin/bash
# Ask the user for login details
name=$1
newpath="/home/robel/Desktop/WebSiteproject/adminsite/project-enviroments/databasetest/media/deployedlist/"$name
sudo chmod -R 777 $newpath
cd $newpath
sudo docker-compose up -d