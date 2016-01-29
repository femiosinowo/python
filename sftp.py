#!/usr/bin/env python

#this module will ssh into a server and copy files from it

import paramiko
import os
hostname = '10.0.0.60'
port = 22
username = 'root'
password = 'P@ssw0rd'
dir_path = '/etc/puppet/'
if __name__ == "__main__":
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()