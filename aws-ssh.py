#!/usr/bin/env python
import argparse
import subprocess

import boto3

default_profile = 'production'
default_region = 'us-east-1'
default_user = 'ubuntu'

p = argparse.ArgumentParser('SSH directly to an instance with a given boto profile')
p.add_argument('-p', '--profile', action='store', dest='profile', default=default_profile, type=str,
               help='BOTO3 profile, default = ' + default_profile)
p.add_argument('-r', '--region', action='store', dest='region', default=default_region, type=str,
               help='Region, default = ' + default_region)
p.add_argument('-i', '--instance', action='store', dest='instance', required=True, type=str, help='Instance ID')
p.add_argument('-u', '--user', action='store', dest='user', type=str, default=default_user,
               help='Username, default = ' + default_user)

if __name__ == '__main__':
    args = p.parse_args()

    session = boto3.Session(profile_name=args.profile)
    ec2 = session.client('ec2', args.region)
    i = ec2.describe_instances(InstanceIds=[args.instance])
    host = i['Reservations'][0]['Instances'][0]['PublicDnsName']
    cmd = 'ssh -l ' + args.user + ' ' + host

    print(cmd)
    ret = subprocess.call(cmd, shell=True)
    print('Done, exitcode: ' + ret)
