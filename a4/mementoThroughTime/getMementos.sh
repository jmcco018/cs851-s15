#!/bin/bash

IFS=$'\n'

for line in `cat memento`; do
    memento=$(echo "$line" | cut -d' ' -f2)
    mkdir $memento
    i=0
    for uri in `cat ../timemaps/$memento | cut -d',' -f1- | grep 'rel="memento"' | cut -d'<' -f2 | cut -d'>' -f1`; do
       folder="/home/jmcconne/cs751/a4/mementoThroughTime/"$memento"/"
       echo $folder
       wget -E -t 5 -T 5 -O $folder$i -e robots=off "$uri"
       i=$(($i+1))
    done
done
