#!/bin/bash

sum=0
for i in {1..100}; do
    sleep 1
    startup_time=$(adb shell am start-activity -W -S com.facebook.katana/.LoginActivity | grep "TotalTime" | awk '{sum += $2; print $2}')
    sum=$((sum + startup_time))
    echo "Cold Startup Time for Iteration $i: $startup_time ms" >> startup_cold.txt
done
mean=$((sum / 100))
echo "Mean Cold Startup Time: $mean ms" >> startup_cold.txt
