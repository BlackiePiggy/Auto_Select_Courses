# Move ti search area
xdotool mousemove 468 237
xdotool click 1

# Delete search area
xdotool key ctrl+a
xdotool key Delete

# Add paste word
echo '人工智能的数学基础' | xsel -i -b

# Paste
xdotool key ctrl+v

# Search
xdotool mousemove 998 307
xdotool click 1

sleep 0.5