#!/bin/bash

#Activate the project virtual environment if it exists
#This makes sure we use the right dependencies for the tests
if [ -d "venv" ]; then
    source venv/Scripts/activate
fi

#Execute the test suite
python -m pytest testapp.py

#Capture the exit status of the pytest command
#In bash, $? stores the result of the last thing that ran
test_status=$?

#Return exit code 0 if all tests passed, or 1 if something went wrong
if [ $test_status -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi