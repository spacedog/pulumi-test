import pulumi
from pulumi_aws import iam

ssh_key = iam.SshKey("it-team",
  encoding="SSH",
  public_key="AAAAB3NzaC1yc2EAAAADAQABAAABAQDjrL5XkIjVn4Fh8vV6DzfExsAatAVRXAXXXoNqfbXyc/6a/eej8tmEWcpen2w+FcN1YfRo5nLDpK6kTqULCWpVsxmLwUr1XgEoReASVHIxJnDInztMqLw6u9e15OZAVYW9ofuVjGniDXMDFwOtexEX/owJfci4bs9IcyS3HVflFin3LI7oJPv3HyFEDbtvt2bH4R8bFtvhz5WVDtqQY9he0vAUusQtmCqKNbxPGLz9VhJ+hAtOIgKeyr/RAQawhdoHNGXAGBIcVVCgIlxj9rqOPci+uStn0ZqevitmZyhNGKlQB+HMYKo8AHDRBlOUsSs0m3keLFRuPyc+RHeR64Xp",
  username="anton@hell"
)