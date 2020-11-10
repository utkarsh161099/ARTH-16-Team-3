import os

def docker_cmd():
   os.system("setterm -foreground yellow")
   print("\t\t Welcome to Docker!!")
   os.system("setterm -foreground blue")
   print('''
        press1: to launch a docker container...
        press2: to check the available images...
        press3: to check the running containers...
        press4: to pull the docker images from docker hub...
        press5: to get the interactive bash shell to your container...
        press6: to remove container...
        press7: to rename your container
        press8: to stop a container...
        press9: to start & attach a container...
        press10: to copy file to your container...
       ''')
   os.system("setterm -foreground cyan")
   cmd = int(input("ENTER YOUR CHOICE: "))
   if cmd==1:
     os.system("setterm -foreground cyan")
     image = input("Enter the Docker image: ")
     name = input("Enter the name for your container: ")
     os.system("docker run -dit --name %s %s " %(name, image))
     os.system("setterm -foreground green")
     print("Your %s container is created!!" %(name))
     os.system("setterm -foreground white")
   elif cmd==2:
     os.system("docker images")
   elif cmd==3:
     os.system("docker ps -a")
   elif cmd==4:
     os.system("setterm -foreground cyan")
     image=input("Enter the image name: ")
     os.system("docker pull %s" %(image))
     os.system("setterm -foreground green")
     print("Your image has pulled...")
     os.system("setterm -foreground white")
   elif cmd==5:
     os.system("setterm -foreground cyan")
     cont=input("Enter the name of the container you want to interact: ")
     os.system("setterm -foreground white")
     os.system("docker exec -it %s bash" %(cont))
   elif cmd==6:
     os.system("setterm -foreground cyan")
     cont=input("Enter the name of the container you want to delete: ")
     os.system("docker container rm -f %s" %(cont))
     os.system("setterm -foreground green")
     print("your container %s had been deleted!!" %(cont))
     os.system("setterm -foreground white")
   elif cmd==7:
     os.system("setterm -foreground cyan")
     cont=input("Enter the name of the container you want to rename: ")
     new_cont=input("Enter the new name for the container: ")
     os.system("setterm -foreground green")
     os.system("docker container rename %s %s" %(cont, new_cont))
     print("Your contianer has been renamed!")
     os.system("setterm -foreground white")
   elif cmd==8:
     os.system("setterm -foreground cyan")
     cont=input("Enter the name of container: ")
     os.system("docker stop %s" %(cont))
     os.system("setterm -foreground green")
     print("your container %s had been stopped!!" %(cont))
     os.system("setterm -foreground white")
   elif cmd==9:
     os.system("setterm -foreground cyan")
     cont=input("Enter the name of the container: ")
     os.system("docker start %s" %(cont))
     os.system("docker attach %s" %(cont))
     os.system("setterm -foreground green")
     print("Your container has started and been attached!")
     os.system("setterm -foreground white")
   elif cmd==10:
     os.system("setterm -foreground cyan")
     fil=input("Enter file name: ")
     cont=input("Enter the container name: ")
     os.system("docker cp %s %s:%s" %(fil, cont, fil))
     os.system("setterm -foreground green")
     print("Successfull!")
     os.system("setterm -foreground white")
