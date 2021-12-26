from shell import exec_command
from urllib.request import Request
from urllib.request import urlopen
from basic import user

def install_fish():
    print("Installing fish shell")
    stdout, stderr, status = exec_command('pacman -S --noconfirm fish')
    if status != 0:
        print('There was an error installing fish')
        print(stdout, stderr)
        return False
    print(stdout)

    print("Downloading OhMyFish!")
    request = Request('https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install')
    response = urlopen(request)
    omf_script = response.read().decode('utf8')
    
    with open('ohmyfish.sh', 'w') as script:
        script.write(omf_script)

    print("Installing OhMyFish!")
    stdout, stderr, status = exec_command(f'fish ohmyfish.sh --noninteractive --yes')
    #print(stdout, stderr, status)
    stdout, stderr, status = exec_command(f'rm ohmyfish.sh')
    #print(stdout, stderr, status)

    print("Changing Shell")
    stdout, stderr, status = exec_command(f'chsh {user} -s /usr/bin/fish')
    print(stdout)

    print("Now set default shell on Konsole Profile")



#install_fish()

def install_fisher():
    print('Downloading fisher')
    request = Request('https://git.io/fisher')
    response = urlopen(request)
    fisher_script = response.read().decode('utf8')
    print('Installing fisher')
    with open('fisher.sh', 'w') as script:
        script.write(fisher_script)

    stdout, stderr, status = exec_command(['fish', '-c', 'source fisher.sh; fisher install jorgebucaran/fisher'], needs_split = False)
    print(stdout, stderr, status)
    exec_command('rm fisher.sh')

install_fisher()
