#!/usr/bin/env python

from shell import exec

def install_fonts():
    print('Installing JetBrains Mono Font')
    _, _, status1 = exec('cp -rvT ./fonts/jetbrains_mono/ttf/ /usr/share/fonts/TTF')
    print('Installing Meslo Nerd Font')
    stdout, stderr, status2 = exec('cp -rvT ./fonts/meslo_nerd_font/ /usr/share/fonts/TTF')
    return !status1 && !status2
