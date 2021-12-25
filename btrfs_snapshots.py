from shell import exec
from datetime import datetime
from basic import base_path

def make_snapshot():
    print("Creating Snapshots")
    stdout, stderr, status = exec('btrfs subvolume list /')
    if status != 0:
        print("There was an error reading the btrfs subvolumes")
        return False

    folder_name = f'{base_path}/.snapshots/{datetime.now().isoformat()}'
    stdout, stderr, status = exec(f'mkdir -pv {folder_name}')
    if status != 0:
        print("There was an error creating snapshots folder")
        return False

    stdout, stderr, status = exec(f'btrfs subvolume snapshot / {folder_name}/root')
    if status != 0:
        print("There was an error creating root snapshot")
        return False
    print(stdout)

    stdout, stderr, status = exec(f'btrfs subvolume snapshot /home/ {folder_name}/home')
    if status != 0:
        print("There was an error creating home snapshot")
    print(stdout)

    return True

