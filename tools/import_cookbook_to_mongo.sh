#!/bin/sh
mongoimport -d douguo -c $1 ../data/$1.json
#mongoimport -d douguo -c cookbook ../data/cookbook.json
