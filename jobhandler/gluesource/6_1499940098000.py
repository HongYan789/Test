#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import sys

print "xxl-job: hello python"
print "脚本文件：", sys.argv[0]
for i in range(1, len(sys.argv)):
	time.sleep(1)
	print "参数", i, sys.argv[i]

print "Good bye!"
exit(0)