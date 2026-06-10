#!/bin/bash

cp -rf ./files/. "$HOME/";
chmod +x "$HOME/.xinitrc";
xinit "$HOME/.xinitrc" -- :0
