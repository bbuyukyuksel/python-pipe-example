from subprocess import Popen,PIPE
import os

#os.popen("ls /home/pardus/Masaüstü/Burak/")
output = Popen("python3 xx.py",stdin=PIPE,stdout=PIPE,shell=True)
output.stdin.write("Burak\nBuyukyuksel\n".encode())
output.stdin.close()
print(output.stdout.read().decode("utf-8"))



