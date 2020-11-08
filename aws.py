import os


def aws_infra():
    print('''
	press 1: To Create a Key Pair
	press 2: To Create a Security Group
	press 3: To Launch an Instance
	press 4: To Terminate an Instance
	press 5: To delete Key Pair
	press 6: To Launch EBS volume
    press 7: To Delete an EBS Volume
    press 8: To Create a S3 bucket
    press 9: To Attach a Volume to an Instance
    press 10: To Delete a S3 bucket
    press 11: To Delete a Security Group 
	''')
    i = int(input("Enter ur choice: "))
    if i == 1:
        put = input("Enter Key-pair name: ")
        os.system(
            "aws ec2 create-key-pair --key-name %s --query KeyMaterial --output text > %s.pem" % (put, put))
        print("Key pair created")
    elif i == 2:
        put = input("Enter Description of security group: ")
        put2 = input("Enter Security group Name: ")
        sg = os.system(
            "aws ec2 create-security-group --description %s --group-name %s" % (put, put2))
        print(sg)
    elif i == 3:
        put1 = input("Enter Image id: ")
        put2 = input("Enter Instance type: ")
        put3 = input("Enter key name to be attached: ")
        put4 = input("Enter Security Group Id: ")
        put5 = int(input("Enter number of Instance to be Launched: "))
        ins = os.system(
            "aws ec2 run-instances  --image-id %s  --instance-type %s --key-name  %s  --security-group-ids %s --count %s " % (put1, put2, put3, put4, put5))
        print(ins)
    elif i == 4:
        put = input("Enter Instance Id to be Terminated: ")
        ins = os.system(
            "aws ec2 terminate-instances --instance-ids %s" % (put))
        print(ins)
    elif i == 5:
        put = input("Enter Key-pair name to be Deleted: ")
        os.system(
            "aws ec2 delete-key-pair --key-name %s" % (put))
        print("Key pair Deleted")
    elif i == 6:
        put1 = input("Enter Availability zone name: ")
        put2 = int(input("Enter Size of the volume to be created: "))
        put3 = input("Enter volume type: ")
        vol = os.system(
            "aws ec2 create-volume --availability-zone %s --size %s  --volume-type %s" % (put1, put2, put3))
        print(vol)
    elif i == 7:
        put = input("Enter Volume Id to be Deleted: ")
        os.system(
            "aws ec2 delete-volume --volume-id %s" % (put))
        print("Volume Deleted")
    elif i == 8:
        put1 = input("Enter Bucket name(unique): ")
        put2 = input("Enter Region to launch S3: ")
        buck = os.system(
            "aws s3api create-bucket --bucket %s --region %s" % (put1, put2))
        print(buck)
    elif i == 9:
        put1 = input("Enter device : ")
        put2 = input("Enter Instance Id whom to attach: ")
        put3 = input("Enter Volume Id to be attached: ")
        vol = os.system(
            "aws ec2 attach-volume --device %s --instance-id  %s  --volume-id %s" % (put1, put2, put3))
        print(vol)
    elif i == 10:
        put1 = input("Enter Bucket name to Delete: ")
        put2 = input("Enter Region to delete S3: ")
        buck = os.system(
            "aws s3api delete-bucket --bucket %s --region %s" % (put1, put2))
        print(buck)
    elif i == 11:
        put = input("Enter name of the security group to delete: ")
        sg = os.system(
            "aws ec2 delete-security-group --group-name %s" % (put))
        print(sg)
