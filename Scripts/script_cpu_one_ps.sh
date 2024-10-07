#!/bin/bash

for i in {1..100}; do

    sleep 1 & 
    output=$(adb shell top -o %CPU -o PID -o ARGS -s 1 -b -n 1 -p 17790 | grep -vw "top -o" | awk '$1 != "0.0" && NR == 6 {print $1/8;}')
    
    echo "$output" >> cpu_percent_one_ps.txt
done
