#!/bin/bash
env=~/Desktop 
test=`ls ${env}`
for loop in ${test}; 
do
    echo $loop
done
