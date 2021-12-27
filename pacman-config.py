from shell import exec_command
import os

def pacman_config():
    current_path = os.getcwd()
    stdout, stderr, status = exec_command(f'ln -sf {current_path}/pacman.conf /etc/pacman.conf')
    if status != 0:
        return False
    stdout, stderr, status = exec_command(f'ln -sf {current_path}/makepkg.conf /etc/makepkg.conf')
    if status != 0:
        return False
    return True

pacman_config()
