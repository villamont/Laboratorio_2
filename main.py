### Main function

import api, ids
import time
import concurrent.futures
import threading

thread_local = threading.local()

def read_users():
    for i in ids.ids:
        usr=api.getOneUser(i)
        print("Username is: ", usr["name"])

start_time = time.time()
read_users()
#download_all_sites(sites)
duration = time.time() - start_time
print(f"Readed {len(ids.ids)} users in {duration} seconds")
        
