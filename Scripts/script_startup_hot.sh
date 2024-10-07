#!/bin/bash

sum=0
for i in {1..100}; do
    sleep 1
    startup_time=$(adb shell am start-activity -W com.sec.android.app.camera/.Camera | grep "TotalTime" | awk '{sum += $2; print $2}')
    adb shell input keyevent KEYCODE_HOME #appui sur la touche Home
    sum=$((sum + startup_time))
    echo "Hot Startup Time for Iteration $i: $startup_time ms" >> startup_hot.txt
    
done
mean=$((sum / 100))
echo "Mean Hot Startup Time: $mean ms" >> startup_hot.txt
