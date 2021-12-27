import subprocess
import shlex
import os
from basic import base_path as home

def exec_command(command, needs_split = True, as_root = True):
    if not as_root:
        os.seteuid(1000)
        os.environ['HOME'] = home
    splitted_command = shlex.split(command) if needs_split else command
    process = subprocess.run(splitted_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout = process.stdout
    stderr = process.stderr
    returncode = process.returncode
    if not as_root:
        os.seteuid(0)
        os.environ['HOME'] = '/root'
    return stdout, stderr, returncode
