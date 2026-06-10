#!/bin/bash

function start() {
  update;
  install_core_tools;
  #copy_files;
}

function copy_files() {
  cp -rf ./files/. "$HOME/";
  chmod +x "$HOME/.xinitrc";
  chmod +x "$(dirname "$0")/run.sh";
}

function install_core_tools() {
  sudo pacman -S --needed \
    xorg-server xorg-xinit xorg-xauth xorg-xprop \
    xf86-video-amdgpu xf86-video-intel mesa \
    qtile feh rofi \
    dolphin konsole kate \
    wget curl git make nano unzip neovim htop \
    xterm;
}

function update() {
  sudo pacman -Syu;
}

start;
