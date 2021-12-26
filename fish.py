from shell import exec
from urllib.request import Request
from urllib.request import urlopen
from basic import user

def install_fish():
    print("Installing fish shell")
    stdout, stderr, status = exec('pacman -S --noconfirm fish')
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
    #stdout, stderr, status = exec(f'fish ohmyfish.sh --noninteractive --yes')
    print(stdout, stderr, status)
    stdout, stderr, status = exec(f'rm ohmyfish.sh')
    #print(stdout, stderr, status)

    print("Changing Shell")
    stdout, stderr, status = exec(f'chsh {user} -s /usr/bin/fish')
    print(stdout)

    print("Now set default shell on Konsole Profile")



install_fish()
