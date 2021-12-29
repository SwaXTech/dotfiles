from shell import exec_command
from basic import base_path
import os

def copy_config_files():
    stdout, stderr, status = exec_command('konsole --version')
    if status != 0:
        print('Konsole is not installed')
        return False
    
    print('Executing: ' + stdout)
    current_path = os.getcwd()
    stdout, stderr, status = exec_command(f'ln -sf {current_path}/Sweet.colorscheme {base_path}/.local/share/konsole/Sweet.colorscheme')
    stdout, stderr, status = exec_command(f'ln -sf {current_path}/default.profile {base_path}/.local/share/konsole/default.profile')
    stdout, stderr, status = exec_command(f'ln -sf {current_path}/konsolerc {base_path}/.config/konsolerc')
    print('Activating blur. Remeber reboot')
    stdout, stderr, status = exec_command(f"kwriteconfig5 --file kwinrc --group Plugins --key blurEnabled --type bool true")
    stdout, stderr, status = exec_command(f"bash -c 'kwin_x11 --replace &'", no_redirect = True)
    print(stdout, stderr, status)

copy_config_files()
