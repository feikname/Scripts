#!/bin/bash

#
# piqueserver_autopep8.sh
# MIT License
#
# v0.0.1 - 2017-01-30
#

# Define directories to run autopep8 on:
DIRS[0]="./feature_server/*.py"
DIRS[1]="./feature_server/config/scripts/*.py"
DIRS[2]="./pyspades/*.py"

# Rudimentar check
if ! [[ -d "./feature_server" ]]
then
    echo "This file should be run from the root of piqueserver source code."
    exit 1 # Exit with failure status (*NIX systems)
fi

# Check if virtualenv can be found
MSG="Virtualenv could not be found!"
command -v virtualenv >/dev/null 2>&1 || { echo >&2 "$MSG"; exit 1; }
echo "Found virtualenv binary"

# Check if a venv already exists
echo -n "Searching for ./venv/Scripts/activate existence... "
if [[ -f "./venv/Scripts/activate" ]]
then
    echo "found"
else
    echo "NOT FOUND!"
    
    echo "Creating virtualenv venv..."
    virtualenv venv
fi

# Activate virtualenv and install autopep8 if is not installed already
source ./venv/Scripts/activate
echo -n "Checking if autopep8 is already installed in this virtualenv... "
if python -c "import autopep8" >/dev/null 2>&1
then
    echo "found"
else
    echo "NOT FOUND!"
    
    echo "Installing autopep8..."
    pip install autopep8
fi

# Run autopep8 in the main python directories
echo "Applying autopep8 to the selected directories..."
for DIR in "${DIRS[@]}"
do
    echo "Applying autopep8 to $DIR"
    for F in $DIR; do autopep8 --in-place $F; done;
done

# Deactivate virtualenv
deactivate
