import os
import subprocess as sp
from linux import *

print("Welcome to my Tools")
print("~~~~"*15)
ch = 'y'

os.system("tput setaf 6")
print("""
For tasks related to Linux, press 'a'
For tasks related to Docker press 'b'
For tasks related to AWS-Cloud press 'c'
For tasks related to Hadoop press 'd'
For tasks related to Ansible press 'e'
""")
ch = input("Enter your choice: ").lower()
if(ch == 'a'):
    Task_Linux()
    os.system("tput setaf 7")
# elif ch == 'b':

    # code
# elif ch=='c':
    # code
# elif ch=='d':
    # code
# elif ch=='e':
    # code
# else:
#	print("Not Supported !!!")
ch = input("Do you want to continue(y/n): ").lower()
