import subprocess
import shlex

def exec_command(command):
    splitted_command = shlex.split(command)
    process = subprocess.run(splitted_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout = process.stdout
    stderr = process.stderr
    returncode = process.returncode
    return stdout, stderr, returncode
