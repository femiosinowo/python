#!/usr/bin/env python

#this gets what platform you are on
import os
import platform

profile = [
platform.architecture(),
platform.dist(),
platform.libc_ver(),
platform.mac_ver(),
platform.machine(),
platform.node(),
platform.platform(),
platform.processor(),
platform.python_build(),
platform.python_compiler(),
platform.python_version(),
platform.system(),
platform.uname(),
platform.version(),
]

print os.listdir(path ='/tmp')

print platform.uname()

for item in profile:
    print item