import subprocess
from typing import Text
try: 
    #c=subprocess.call('dir',shell=True)
    #c=subprocess.run(['ls' , '-la'] ,shell=True)
    #c=subprocess.run(['ls' , '-la'] ,shell=True)
    #print(c)
    #subprocess.run(["echo", "Hi Rahul"], shell=True)
    #subprocess.run(['echo', 'hello world'], shell=True)
  #  c=subprocess.call(["ls", "-la"], stdout=subprocess.PIPE ,Text=True)
  #  print(c.stdout)

   # Popen.__init__():
   # n=int(input("Enter a no: "))
    cmd = "df -h"
    p=subprocess.Popen(cmd, shell=True)
    p.wait()
    if p.returncode == 0:
        print("success")
    else:
        print("failed")

except Exception as e:
    print(e)

