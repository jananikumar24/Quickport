import socket
import threading
from queue import Queue

target="192.168.10.1"
queue=Queue()
open_ports=[]

def portscan(port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port=queue.get()
        if portscan(port):
            print("port {} is open".format(port))
            open_ports.append(port)

port_list=range(1,1024)
fill_queue(port_list)
thread_list=[]

for t in range(100):
    thread=threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports:", open_ports)
