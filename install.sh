#!/bin/bash

function start() {
  update;
  install_core_tools;
}

function install_core_tools() {
  sudo pacman -S --noconfirm --needed \
    xorg-server xorg-xinit xorg-xauth xorg-xprop \
    xf86-video-amdgpu xf86-video-intel mesa \
    qtile feh rofi \
    dolphin konsole kate \
    wget curl git nano unzip neovim htop \
    xterm;
}

function update() {
  sudo pacman -Syu --noconfirm;
  sudo pacman -S --noconfirm --needed base-devel python-pip;
  sudo pacman -Syu --noconfirm;
}

start;
