#!/bin/bash
# Dependencies: xdotool, xclip

# Copy 'do <filename>' to clipboard
string='do ''"'$1'"'
echo "${string}" | xclip -selection clipboard

# Get Stata window ID (latest oppened?)
winid_stata=$(xdotool search --classname "stata" | tail -1)

# Send string to Stata's command pane, selecting previous text and copying on top
# Note: there is an issue with xdotool's clearmodifiers option (see https://github.com/jordansissel/xdotool/issues/43)
# xdotool type --window ${winid_stata} ${string} # xdotool type is slow AF
if [ ! -z "$winid_stata" ]; then
	xdotool key --window ${winid_stata} --delay 50 ctrl+a ctrl+v Return # Current method doesn't switch window:
else
	echo "No Stata window open."
	exit 1
fi