#!/bin/bash
# Dependencies: xdotool, xclip

# Copy 'do <filename>' to clipboard
string='do ''"'$1'"'
echo "${string}" | xclip -selection clipboard

# Get relevant windows' IDs
# winid=$(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}')
winid_stata=$(xdotool search --name "Stata/MP 15.1")

# swich to command line and select existing text via ctrl-a and paste clipboard
# Note: there is an issue with xdotool's clearmodifiers option (see https://github.com/jordansissel/xdotool/issues/43)
# sleep .1

# OG method:
# xdotool key --clearmodifiers --delay 50 ctrl+a ctrl+v Return

# OG method without clearmodifiers option (see note):
# xdotool key --delay 50 ctrl+a ctrl+v Return

# Separating commands seems to improve OG method:
# xdotool key --clearmodifiers --delay 50 ctrl+a
# xdotool key --clearmodifiers --delay 50 ctrl+v
# xdotool key --clearmodifiers --delay 50 Return

# Current method doesn't switch window:
# xdotool type --window 48234499 ${string} # xdotool type is slow AF
xdotool key --window ${winid_stata} --delay 50 ctrl+a ctrl+v Return

# sleep .1

# if [ "$test" -eq "2" ]
#   then
#   xdotool key --clearmodifiers Return
# fi

# go back to editor window
# wmctrl -i -a $winid
