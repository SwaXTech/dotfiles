#!/usr/bin/env python

from shell import exec_command

def install_fonts():
    print('Installing JetBrains Mono Font')
    _, _, status1 = exec_command('cp -rvT ./fonts/jetbrains_mono/ttf/ /usr/share/fonts/TTF')
    print('Installing Meslo Nerd Font')
    stdout, stderr, status2 = exec_command('cp -rvT ./fonts/meslo_nerd_font/ /usr/share/fonts/TTF')
    print('All fonts installed. Remember restart terminal to refresh')
    return not status1 and not status2
