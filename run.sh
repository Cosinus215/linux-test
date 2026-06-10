#!/bin/bash

cp -rf ./files/. "$HOME/";
chmod +x "$HOME/.xinitrc";
xinit "$HOME/.xinitrc" -- /usr/bin/Xorg :0 -keeptty
