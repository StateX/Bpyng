import subprocess

#esto hace que el resutado se guarde en un txt
def pingOK():
	 print "OK"
	 barridoPing = str(direccion + " OK ")
	 LbarridoPing = open('LbarridoPing.txt', 'a+')
	 LbarridoPing.write(barridoPing)
	 LbarridoPing.close()
	 print "ping guardado con exito"
def pingFail():	 
	 print "Fail"
	 barridoPing = str(direccion + " Fail ")
	 LbarridoPing = open('LbarridoPing.txt', 'a+')
	 LbarridoPing.write(barridoPing)
	 LbarridoPing.close()
	 print "ping guardado con exito"
def pingMiss():
	 print "Miss"
	 barridoPing = str(direccion + " Miss ")
	 LbarridoPing = open('LbarridoPing.txt', 'a+')
	 LbarridoPing.write(barridoPing)
	 LbarridoPing.close()
	 print "ping guardado con exito"

print """

____________                  
| ___ \ ___ \                 
| |_/ / |_/ /   _ _ __   __ _ 
| ___ \  __/ | | | '_ \ / _` |
| |_/ / |  | |_| | | | | (_| |
\____/\_|   \__, |_| |_|\__, |
             __/ |       __/ |
            |___/       |___/ 

"""
#menu
print "[a = Hacer ping con mi propio input]  [b= Hacer un barrido ping]"
d1 = raw_input("")
if d1 == "a":
	 direccion =  raw_input("Escribe la direccion de la pagina: ")
	 busqueda = subprocess.call(['ping', direccion])
	 if busqueda == 0:
	 	 print pingOK()
	 elif busqueda == 1:
	 	 print pingFail() 	 	 	 		 	 	 
	 else: 	
	 	 print pingMiss()
	 	 
elif d1 == "b":	 
	 for ping in range (0,10): 
	 	 direccion = "127.0.0." + str(ping)
	 	 busqueda = subprocess.call(['ping', direccion])
	 	 if busqueda == 0:
	 	 	 print pingOK()
	 	 elif busqueda == 1:
	 	 	 print pingFail() 	 	 	 		 	 	 
	 	 else: 	
	 		 print pingMiss()
