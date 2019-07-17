#!/bin/bash

IMAGE_NAME='xtract_jsonxml_image'

echo "Input a directory to mount"
#read DIRECTORY
DIRECTORY=/xtract-jsonxml/test_files

echo $DIRECTORY
docker run -it -v ~/pub8:/xtract-jsonxml/test_files $IMAGE_NAME /bin/bash

