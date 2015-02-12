#!/bin/bash

IFS=$'\n'
i=0
for line in `cat uniqueuri`; do 
    echo "$line" $i
    i=`expr $i + 1`
done
