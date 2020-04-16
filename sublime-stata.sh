#!/bin/bash
# Dependencies: xdotool, xclip

# Copy 'do <filename>' to clipboard
string='do ''"'$1'"'
echo "${string}" | xclip -selection clipboard

# Get Stata window ID (first window that matches the regex)
winid_stata=$(xdotool search --name --limit 1 "Stata/(IC|SE|MP)? 1[0-9]\.[0-9]")

# Send string to Stata's command pane, selecting previous text and copying on top
# Note: there is an issue with xdotool's clearmodifiers option (see https://github.com/jordansissel/xdotool/issues/43)
# xdotool type --window ${winid_stata} ${string} # xdotool type is slow AF
if [ ! -z "$winid_stata" ]; then
	xdotool key --window ${winid_stata} --delay 50 ctrl+a ctrl+v Return # Current method doesn't switch window:
else
	echo "No Stata window open."
	exit 1
fi