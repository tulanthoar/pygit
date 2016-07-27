import subprocess
p = subprocess.Popen(['xclip', '-selection', 'p', '-o'],          stdout=subprocess.PIPE, close_fds=True)
stdout, stderr = p.communicate()
print(stdout.decode('utf-8'))
