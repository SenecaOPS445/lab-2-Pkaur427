#!/usr/bin/env python3
# Author: Parminder Kaur
# Author ID: 142566215
# Date Created: 2024/06/1

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')

