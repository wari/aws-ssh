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

## Customizations:
* Just change the default variables