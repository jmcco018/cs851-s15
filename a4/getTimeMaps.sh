#!/bin/bash

IFS=$'\n'

for line in `cat uniqueurinumbers`; do
  link='http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/'$(echo "$line" | cut -d' ' -f1)
  curl -D - $link  > timemaps/$(echo "$line" | cut -d' ' -f2)
  echo
done
