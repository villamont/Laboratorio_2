### Main function

import api, ids
import time
import concurrent.futures
#import threading

ruta='https://github.com/villamont/Laboratorio_2'
#thread_local = threading.local()

def read_users():
    for i in ids.ids:
        usr=api.getOneUser(i)
        print("Username is: ", usr["name"])

def escritura_resultado(resul_time):
# open file with mode 'w'
    archivo = open(ruta + "log.txt", 'a+')
    #print(resul, oper, time,file=archivo)
    print("El resultado ejecutado sin threadind es:", resul_time,file=archivo)
    archivo.close

start_time = time.time()
read_users()
duration = time.time() - start_time
escritura_resultado(duration)
print(f"Readed {len(ids.ids)} users in {duration} seconds")
escritura_resultado(duration)
        
