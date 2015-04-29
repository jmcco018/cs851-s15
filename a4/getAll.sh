#!/bin/bash
IFS=$'\n'
for line in `cat ~/cs751/a4/GoodFiles`;do 
    number=$(echo "$line" | cut -d'/' -f3)
    folder="./bodiesnew/"$number
    url=$(egrep " $number$" uniqueurinumbers | rev | cut -d' ' -f2- | rev)
    echo $folder $url
    mkdir $folder
    wget -E -t 5 -T 5 -P $folder -e robots=off "$url"
done
