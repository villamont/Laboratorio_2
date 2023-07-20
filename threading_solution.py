##threading solution

import api, ids
import time
import concurrent.futures
import threading

thread_local = threading.local()

def read_users(lista):
    for i in lista:
        usr=api.getOneUser(i)
        print("Username is: ", usr["name"])


def read_all_users(lista):
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(read_users, lista)

if __name__ == "__main__":
    lista = ids.ids

start_time = time.time()
read_all_users(lista)
duration = time.time() - start_time
print(f"Readed {len(lista)} users in {duration} seconds")
        
