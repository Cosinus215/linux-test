#!/bin/bash

function start() {
  #update;
  #install_core_tools;
  install_qtile;
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
    python3-pip python3-setuptools python3-dbus-python \
    feh rofi cairo pango;
}

function install_qtile() {
  # Qtile from OBS X11:WindowManagers (system package, not pip)
  local leapver="15.6"  # change to your Leap version
  sudo zypper addrepo \
    "https://download.opensuse.org/repositories/X11:WindowManagers/openSUSE_Leap_$leapver/X11:WindowManagers.repo";
  sudo zypper --gpg-auto-import-keys refresh;
  sudo zypper install -y qtile;
}

function update() {
  sudo zypper --gpg-auto-import-keys refresh;
  sudo zypper update -y;
}

start;
