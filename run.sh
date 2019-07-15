#!/bin/bash

IMAGE_NAME='xtract_jsonxml_image'

echo "Input a directory to mount"
#read DIRECTORY
DIRECTORY=/c/Users/space/Documents/CS/CDAC/official_xtract/xtract-jsonxml/test_files

echo $DIRECTORY
echo docker run -v "$DIRECTORY"/:"$DIRECTORY" $IMAGE_NAME
docker run -v "$DIRECTORY":/"$DIRECTORY" $IMAGE_NAME --path RY9405.xml

read wait
