import os
import subprocess as sp

print("Welcome to my Tools")
print("~~~~"*15)
ch='y'

os.system("tput setaf 6")
print("""
For tasks related to Linux, press 'a'
For tasks related to Docker press 'b'
For tasks related to AWS-Cloud press 'c'
For tasks related to Hadoop press 'd'
For tasks related to Ansible press 'e'
""")
ch=input("Enter your choice: ").lower()
def Task_Linux():
	print('''
	press 1: To show today's date
	press 2: To open calender
	press 3: To show location of app
	press 4: To see the present directory & list all the things in it
	press 5: To see ur private ip
	press 6: To see the account you are working on
	press 7: To check capacity of hardisk
	press 8: To check RAM 
	press 9: To open binary calculator
	press 10: To shutdown or reboot the os
	press 11: To create a new directory
	press 12: To see the configuration of the node(master/slave/nothing)
	press 13: To switch the master node
	press 14: To disable firewall(don't do this it is not good!!!)
	press 15: To see the no. of cpus
	press 16: To see the current running processes
	press 17: To see when you loggedin to this os
	press 18: To see software n version if u have  in ur system	
	press 19: To clear cache memory
	press 20: To change the directory 
	press 21: To make the terminal inactive for specifed amount of time
	press 22: To show the files in hadoop 
	press 23: To change block size and upload a file
	press 24: To show the occupied port no.s
	press 25: To show the report of hadoop distributed file system.
	press 26: To see ths portal of hadoop in webUI
	press 27: To connect(ping) to website
	press 28: To provide a new name to a command
	press 29: To add a user and giving access as required
	press 30: To display cpu architecture
	press 31: To leave the safe mode in hadoop
	press 32: To find the id of the process
	press 33: To kill the process 
	press 34: To see the packets flow 
	press 35: To change the color
	''')
	ip=int(input("Enter ur choice: "))
	if ip==1:
		
		os.system("date")
	elif ip==2:
		os.system("cal")
	elif ip==3:
		file= input("enter the app/ file name: ")
		os.system(" which %s"%(file))
	elif ip==4:
		os.system("pwd")
		os.system("ls -lh")
	elif ip==5:
		os.system("ifconfig enp0s3")
	elif ip==6:
		print("you are :")
		#a=print(os.system("whoami"))
		a=sp.getoutput("whoami")
		print(a)
	elif ip==7:
		os.system("df -h")
	elif ip==8:
		os.system("free -m")
	elif ip==9:
		os.system("bc ")
		#print("press ctrl+c to close")
	elif ip==10:
		n=int(input("press 0:to to shutdown n 6: to reboot: "))
		if n==0:
			os.system("init %s"%(n))
		elif n==6:
		 	os.system("init %s"%(n))
		else:
			print("not supported!  enter either 1 or 6")
	elif ip==11:
		dir=input("enter the directory name:")
		dir="/%s"%(dir)
		#print(dir)
		os.system("mkdir %s"%(dir))
		#os.system("ls -lh")
		print("directory %s created"%(dir))
	elif ip==12:
		os.system("jps")
	elif ip==13:
		os.system("jps")
		s=input("start or stop?: ").lower()
		os.system("jps")		
		os.system("hadoop-daemon.sh %s namenode" %(s))
	elif ip==14:
		os.system("systemctl disable firewalld")
		os.system("setenforce 0")
		print("firewall disabled")
	elif ip==15:
		os.system("lscpu | less")
		#print("press q to quit")

	elif ip==16:
		os.system("ps -aux | less")
	elif ip==17:
		os.system("uptime")
	elif ip==18:
		s=input("name of file: ").lower()
		os.system("rpm -q %s" %(s))
		print("we can either use rpm cmd or yum cmd, using yum: ")
		os.system("yum whatprovides %s"%(s))
		c=input("do you want to install any s/w?: ").lower()
		if c=='y':
			s=input("enter the software name: ").lower()
			os.system("yum install %s" %(s))
		else:
			print("ok!!")
				 
	elif ip==19:
		os.system("echo 3 > /proc/sys/vm/drop_caches")
	elif ip==20:
		dr=input("enter the directory name:").lower()
		os.system("cd %s" %(dr))
	
	elif ip==21:
		slp=input("enter the time either in hours, mins or secs eg: 1s,1m or 1h :").lower()
		os.system("sleep %s" %(slp))
	
	elif ip==22:
		os.system("hadoop fs -ls /")
	elif ip==23:
		c=input("default size is 64mb, do you want to change and then upload(y/n):").lower()
		if c=='n':
			file=input("enter the file name along with extension: ")
			os.system("hadoop fs -put %s /"%(file))
		if c=='y':
			bs=input("enter block size properly (eg:32M):")
			fn=input("enter the file name along with extension: ")
			print("cmd--hadoop fs -D dfs.blocksize=%s -put %s /"%(bs,fn))
			os.system("hadoop fs -D dfs.blocksize=%s -put %s /"%(bs,fn))
		else:
			print("enter either y or n")
	elif ip==24:
		os.system("netstat -tnlp")
	elif ip==25:
		os.system("hadoop dfsadmin -report")
	elif ip==26:
		ip=input("enter master ip: ")
		print("cmd-- firefox %s:50070"%(ip))
		os.system("firefox %s:50070"%(ip))
	elif ip==27:
		ctr=input("enter the no. of packets u want to transfer or receive: ")
		add=input("enter website or ip:")
		os.system("ping -c %s %s"%(ctr,add))
	elif ip==28:
		n=input("What name would u like to give:")
		cmd=input("command to which you want to give:") 
		print("alias %s=%s" (n,cmd))
		os.system("alias %s=%s"(n,cmd))
	elif ip==29:
		usr=input("enter username:")
		pwd=input("enter password:")
		chc=input("would u give complete access to the user(y/n):").lower()
		if chc=='y':
			os.system("useradd %s" %(usr))
		elif chc=='n':
			p=input("enter the file which user can access:")
			p=sp.getoutput("which %s"%(p))
			print(p)
			print("cmd: useradd -s %s %s" %(p,usr))
			os.system("useradd -s %s %s" %(p,usr))
			
	
	elif ip==30:
		os.system("lscpu")
	elif ip==31:
		os.system("hadoop dfsadmin -safemode leave")
		
	elif ip==32:
		pn=input("enter the name of the process:")
		os.system("pgrep %s"%(pn))
	elif ip==33:
		pk=input("enter the process name:")
		os.system("kill | pgrep %s"%(pk))
	elif ip==34:
		pr=input("enter the protocol: SSH or Hadoop: ").upper()
		if pr=='SSH':
			pr=22
		elif pr=='HADOOP':
			pr=9001
		else:
			print("not supported")
		os.system("tcpdump -i enp0s3 tcp port %s -n -x"%(pr))
	elif ip==35:
		fb=input("enter f for foreground n b for background: ").lower()
		print("""
		press 1: for red
		press 2: for green
		press 3: for yellow
		press 4: for blue
		press 5: for purple
		press 6: for skyblue 
		press 7: for white
		 """)
		clr=input("enter your choice of color: ")
		if (clr>0 and clr<=7):
			if fb=='f':
			 	os.system("tput setaf %s"%(clr))
			elif fb=='b':
				os.system("tput setab %s"%(clr))
			else:
				print("Not supported(enter either f orb)!!")
		else:
			print("Not supported in this !!")
	os.system("tput setaf 7")

if(ch=='a'):
	Task_Linux()
	os.system("tput setaf 7")
#elif task == 'b':

	#code
#elif task=='c':
	#code	
#elif task=='d':
	#code
#elif task=='e':
	#code
#else:
#	print("Not Supported !!!")
ch=input("Do you want to continue(y/n): ").lower()

	

