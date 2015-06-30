#!/usr/bin/env bash

xdotool search --class konversation behave %@ focus exec `pwd`/kill-konversation-indicator-applet.sh &

