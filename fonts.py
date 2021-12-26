#!/bin/python

from shell import exec

def install_fonts():
    print('Installing JetBrains Mono Font')
    _, _, status = exec('cp -r ./fonts/jetbrains_mono/ttf /usr/share/fonts/TTF')
    print(status)
    print('Installing Meslo Nerd Font')
    _, _, status = exec('cp -r ./fonts/meslo_nerd_font /usr/share/fonts/TTF')
    print(status)

install_fonts()
