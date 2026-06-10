#!/bin/bash

cp -rf ./files/. "$HOME/";
chmod +x "$HOME/.xinitrc";
startx;
