##threading solution

import api, ids
import time
import concurrent.futures
import threading

ruta='https://github.com/villamont/Laboratorio_2/'

thread_local = threading.local()


def escritura_resultado(resul_time):
# open file with mode 'w'
    archivo = open(ruta + "resultados.md", 'a+')
    #print(resul, oper, time,file=archivo)
    print("El resultado ejecutado con threadind es:", resul_time,file=archivo)
    archivo.close


def read_users(user):
    #for i in lista:
        usr=api.getOneUser(user)
        print("Username is: ", usr["name"])


def read_all_users(lista):
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(read_users, lista)

if __name__ == "__main__":
    lista = ids.ids

start_time = time.time()
read_all_users(lista)
duration = time.time() - start_time
escritura_resultado(duration)
print(f"Readed {len(lista)} users in {duration} seconds")
        

