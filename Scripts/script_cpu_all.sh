#!/bin/bash

if [ $# -eq 0 ] || [ "$1" -ne 0 ] && [ "$1" -ne 2 ] && [ "$1" -ne 4 ] && [ "$1" -ne 6 ] && [ "$1" -ne 8 ]
  then
    echo "Usage : ./script_cpu_all.sh <num_app_bg in [0, 2, 4, 6, 8]>"
    exit 1
fi

total_sum=0
max_sum=0


#adb shell input keyevent KEYCODE_APP_SWITCH
#adb shell input keyevent KEYCODE_DPAD_DOWN
#adb shell input keyevent KEYCODE_DPAD_DOWN
#adb shell input keyevent KEYCODE_ENTER


if [ "$1" -eq 2 ] || [ "$1" -eq 4 ] || [ "$1" -eq 6 ] || [ "$1" -eq 8 ]
then
	adb shell am start-activity -W -S com.zhiliaoapp.musically/com.ss.android.ugc.aweme.splash.SplashActivity #TikTok
	sleep 2
	adb shell input keyevent KEYCODE_HOME #appui sur la touche Home

	adb shell am start-activity -W -S com.rovio.baba/com.unity3d.player.UnityPlayerActivity #Angry Birds 2
	sleep 2
	adb shell input keyevent KEYCODE_HOME #appui sur la touche Home
	
	if [ "$1" -eq 4 ] || [ "$1" -eq 6 ] || [ "$1" -eq 8 ]
	then
	
		adb shell am start-activity -W -S com.machinezone.gow/com.mz.jix.MainActivity #Game of War
		sleep 2
		adb shell input keyevent KEYCODE_HOME #appui sur la touche Home

		adb shell am start-activity -W -S com.eg.android.AlipayGphone/.AlipayLogin #Alipay
		sleep 2
		adb shell input keyevent KEYCODE_HOME #appui sur la touche Home
		
		if [ "$1" -eq 6 ] || [ "$1" -eq 8 ]
		then
		
			adb shell am start-activity -W -S com.netflix.mediaclient/.ui.launch.UIWebViewActivity #Netflix
			sleep 2
			adb shell input keyevent KEYCODE_HOME #appui sur la touche Home

			adb shell am start-activity -W -S com.ebay.mobile/.home.impl.main.MainActivity #Ebay
			sleep 2
			adb shell input keyevent KEYCODE_HOME #appui sur la touche Home
		
			if [ "$1" -eq 8 ]
			then
			
				adb shell am start-activity -W -S com.sec.android.app.camera/.Camera #Camera
				sleep 2
				adb shell input keyevent KEYCODE_HOME #appui sur la touche Home

				adb shell am start-activity -W -S com.google.android.apps.maps/com.google.android.maps.MapsActivity #Google Maps
				sleep 2
				adb shell input keyevent KEYCODE_HOME #appui sur la touche Home
			fi
		fi
	fi
fi


sleep 10

echo -e "\n$1 BG Apps" >> cpu_percent_all.txt

for i in {1..100}; do

    sleep 1 & 
    output=$(adb shell top -o %CPU -o PID -o ARGS -s 1 -b -n 1 | grep -vw "top -o" | awk '$1 != "0.0" && NR > 4 {sum += $1;} END {print "Sum %CPU (8 coeurs):", sum}')
    
    sum_value=$(echo "$output" | awk '{print $NF}') #NF = dernier champ de output = sum
    total_sum=$(awk "BEGIN {print $total_sum + $sum_value}") 
    
    if (( $sum_value > $max_sum )); then
        max_sum=$sum_value
    fi
    
    echo "$output" >> cpu_percent_all.txt
done

mean=$(awk "BEGIN {print $total_sum / 100 / 8}") #diviser par 100 = nb iterations, diviser par 8 car le CPU possede 8 coeurs

echo -e "\tMean %CPU: $mean" >> cpu_percent_all.txt
echo -e "\tPeak %CPU: $(awk "BEGIN {print $max_sum / 8}")" >> cpu_percent_all.txt
