from shell import exec

def install_fish():
    print("Installing fish shell")
    stdout, stderr, status = exec('pacman -S --noconfirm fish')
    if status != 0:
        print('There was an error installing fish')
        return False
    print(stdout)
    return True

install_fish()
