#!/usr/bin/env python

from shell import exec

def install_fonts():
    print('Installing JetBrains Mono Font')
    _, _, status = exec('cp -rvT ./fonts/jetbrains_mono/ttf/ /usr/share/fonts/TTF')
    print(status)
    print('Installing Meslo Nerd Font')
    stdout, stderr, status = exec('cp -rvT ./fonts/meslo_nerd_font/ /usr/share/fonts/TTF')
    print(status)
    print(stderr)

install_fonts()
