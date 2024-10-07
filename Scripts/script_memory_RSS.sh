#!/bin/bash

sum=0
for i in {1..100}; do
    sleep 1
    memory=$(adb shell cat /proc/17790/status | grep VmRSS | awk '{sum += $2; print $2}')
    sum=$((sum + memory))
    echo "$memory" >> memory_RSS.txt
done
