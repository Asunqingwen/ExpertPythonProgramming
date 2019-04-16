# hosts = open('./hello.py')
# try:
# 	for line in hosts:
# 		if line.startswith('#'):
# 			continue
# 		print(line.strip())
# finally:
# 	hosts.close()

with open('./hello.py') as hosts:
	for line in hosts:
		if line.startswith('#'):
			continue
		print(line.strip())

