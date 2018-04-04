# -*- coding:utf8

import os
import sys

all = os.__all__

all.sort()

# try:
# 	f = open('os_info.txt','w')
# 	f.close()
# except OSError:
# 	print('The file has existed.')


for i in all:
	cmd = 'print(os.' + i + ')'
	cmd_doc = 'print(os.' + i + '.__doc__)'
	print('command: 	' + 'os.' + i)
	try:
		print('---------------------info')
		exec(cmd_doc)
		print('---------------------output')
		exec(cmd)
		print('---------------------')
	except:
		print('Need Args')

	print(),


