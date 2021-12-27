from shell import exec_command
from basic import user

def install_docker():
    stdout, stderr, status = exec_command('pacman -S --noconfirm docker docker-compose')
    print(stdout)
    stdout, stderr, status = exec_command('systemctl enable docker.service')
    print(stdout, stderr, status)
    stdout, stderr, status = exec_command('systemctl start docker.service')
    print(stdout, stderr, status)
    stdout, stderr, status = exec_command(f'usermod -aG docker {user}')
    print(stdout, stderr, status)

    print('Docker is successfully installed. Please reboot and run `docker run hello-world`')

install_docker()
