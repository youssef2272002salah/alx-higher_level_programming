#!/bin/bash
# bash script to know the body size of site

curl -sI $1 | grep "Content-Lenght" | cut -d " " -f2
