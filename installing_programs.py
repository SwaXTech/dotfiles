from shell import exec_command
import os
from basic import user
from programs import paru as paru_programs
from programs import flatpak as flatpak_programs

def pacman_config():
    current_path = os.getcwd()
    stdout, stderr, status = exec_command(f'ln -sf {current_path}/pacman.conf /etc/pacman.conf')
    if status != 0:
        return False
    stdout, stderr, status = exec_command(f'ln -sf {current_path}/makepkg.conf /etc/makepkg.conf')
    if status != 0:
        return False
    return True

#pacman_config()

def install_paru():
    stdout, stderr, status = exec_command('pacman -Syu --noconfirm')
    print(stdout)
    stdout, stderr, status = exec_command('pacman -S --noconfirm git')
    print(stdout)
    stdout, stderr, status = exec_command('pacman -S --noconfirm --nedded base-devel')
    print(stdout)

    stdout, stderr, status = exec_command(f"sudo -u {user} fish -c 'git clone https://aur.archlinux.org/paru.git /tmp/paru'", as_root = False) 
    print(stdout, stderr, status)
    stdout, stderr, status = exec_command(f"sudo -u {user} fish -c 'cd /tmp/paru; makepkg -si --noconfirm'", as_root = False)
    print(stdout, stderr, status)
    stdout, stderr, status = exec_command('rm -rf /tmp/paru')


def install_programs():
    to_install = ' '.join(paru_programs)
    stdout, stderr, status = exec_command(f"sudo -u {user} fish -c 'paru -Sy --noconfirm {to_install}'", as_root = False)
    print(stdout, stderr, status)


def install_flatpak_programs():
    for program in flatpak_programs:
        stdout, stderr, status = exec_command(f'flatpak install -y --noninteractive {program}')
        print(stdout, stderr, status)

install_flatpak_programs()
