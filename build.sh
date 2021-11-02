#!/bin/bash

IMAGE_NAME='xtract-jsonxml'

docker rmi $IMAGE_NAME

docker build -t $IMAGE_NAME .
