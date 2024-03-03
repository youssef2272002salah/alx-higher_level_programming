#!/bin/bash
# Display all the HTTP methods allowed
curl - sI "$1" | grep "Allow" | cut - d " " - f 2-
