import subprocess

for ping in range (0,2): 
	 direccion = "127.0.0." + str(ping)
	 busqueda = subprocess.call(['ping', direccion])
	 d1 = str(busqueda)
	 LbarridoPing = open('LbarridoPing.txt', 'a+')
	 LbarridoPing.write(d1)
	 LbarridoPing.close()