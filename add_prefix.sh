#! /bin/sh

# Author: Fernando González <fergonzaramos@yahoo.es>

# Add a prefix name to all files or directories located
# in a specific folder

# Usage:
# ./add_prefix.sh path_to_folder prefix_name

if [ ! $# -eq 2 ]
then

    echo "[ERROR] Usage Error!"
    exit 1

fi

FOLDER=$1
PREFIX=$2

# If folder does not exist, exit:

if [ ! -d $FOLDER ]
then
    echo "[ERROR] Specificated folder doesn't exist!"
    exit 1
fi

cd $FOLDER

for i in $(ls)
do

    filename=$PREFIX$i
    mv $i $filename

done

echo '[INFO] SUCCESS'
exit 0