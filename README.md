# SSH to AWS instance given a boto3 profile

## Assumptions:
* You have added your ssh keys with ssh-agent
* You have setup your ~/.aws/credentials file with profiles
* Your default is called production
* Your default user is called ubuntu.
* All your instances have a PublicDnsName, i.e. is assigned a public IP

## Reasons:
* Have to look up instance IP address from all places too many times, i.e. too lazy

## Caveats:
* Use the exceptions to make sense of errors, boto3 exceptions actually make sense, and is easy to understand

## Installation
* Copy aws-ssh.py to anywhere in your `PATH`
* Install boto3 via package manager or pip

## Running

```
$ aws-ssh.py -i i-2381y23812ewq
ssh -l ubuntu ec2-11-22-33-44.compute-1.amazonaws.com
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-1052-aws x86_64)
```
```
$ aws-ssh.py
usage: SSH directly to an instance with a given boto profile
       [-h] [-p PROFILE] [-r REGION] -i INSTANCE [-u USER]
SSH directly to an instance with a given boto profile:
error: the following arguments are required: -i/--instance
```
```
$ ./aws-ssh.py -h
usage: SSH directly to an instance with a given boto profile
       [-h] [-p PROFILE] [-r REGION] -i INSTANCE [-u USER]

optional arguments:
  -h, --help            show this help message and exit
  -p PROFILE, --profile PROFILE
                        BOTO3 profile, default = production
  -r REGION, --region REGION
                        Region, default = us-east-1
  -i INSTANCE, --instance INSTANCE
                        Instance ID
  -u USER, --user USER  Username, default = ubuntu
```

## Customizations:
* Just change the default variables at the top of the file