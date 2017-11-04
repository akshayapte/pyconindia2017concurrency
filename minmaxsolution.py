import os
from multiprocessing import Queue,Process
import multiprocessing
files = ([i for i in os.walk('.')])
files[0][2].remove('solution.py')
files = files[0][2]
final_min = 10000000
final_max = 0
qmin = Queue()
qmax = Queue()
end = False
ctr = 0
def producer(file):
    with open(file,'r') as f:
        numbers = f.readlines()
        numbers = [int(num.strip('\n')) for num in numbers]
        qmin.put(min(numbers))
        qmax.put(max(numbers))
        return

pool = multiprocessing.Pool(multiprocessing.cpu_count())
pool.map(producer,files)

while end==False:
    ctr += 1
    mn = qmin.get()
    mx = qmax.get()
    final_min = min(mn,final_min)
    final_max = max(mx,final_max)
    if ctr == len(files):
        print("Minimum:", final_min)
        print("Maximum:", final_max)
        end=True
    
