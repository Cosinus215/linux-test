#!/bin/bash


function start() {
  #update;
  #install_core_tools;
  copy_files;
}


function copy_files() {
  cp -rf ./files/. "$HOME/";
}


function install_core_tools() {
  sudo zypper install -y \
    wget curl git make nano unzip neovim htop xprop \
    xorg-x11-server dbus-1-x11 xinit xauth xterm \
    xf86-video-amdgpu xf86-video-intel Mesa-dri \
    dolphin konsole kate \
    openbox feh rofi picom;

    # install tint2
    sudo zypper addrepo https://download.opensuse.org/repositories/X11:Utilities/15.6/X11:Utilities.repo;
    sudo zypper --gpg-auto-import-keys refresh;
    sudo zypper install -y tint2;
}


function update() {
  sudo zypper --gpg-auto-import-keys refresh;
  sudo zypper update -y;
}


start;
