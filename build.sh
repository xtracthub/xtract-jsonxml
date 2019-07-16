#!/bin/bash

IMAGE_NAME='xtract_jsonxml_image'

docker rmi $IMAGE_NAME

docker build -t $IMAGE_NAME .