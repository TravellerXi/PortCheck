#!/usr/bin/env python
#author:admin@mytlu.cn

import socket
timeout=100
socket.setdefaulttimeout(timeout)
print('Please put "ip.txt" and "port.txt" in the root directory of the D drive.')
def get_ip_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ADDR = (ip, port)
        server.connect(ADDR)
        server.close()
        print('connect to ip {0} on port {1} success'.format(ip, port))
        file= open('E:\\sucess.txt','a+')
        file.write('connect to ip {0} on port {1} success\n'.format(ip, port))
        file.close()

    except Exception as err:
        print('connect to ip {0} on port {1} failed'.format(ip, port))
        file = open("E:\\failed.txt", 'a+')
        file.write('connect to ip {0} on port {1} failed\n'.format(ip, port))
        file.close()

    finally:
        server.close()

#data=[]

#print (data)

ip=[]
port=[]
with open("E:\port.txt","r") as f:
    porta=f.read().split('\n')
    #print('主机列表：')
    #print (ipa)
    for port in porta:
        #print (host)
        port=int(port)
        with open("E:\ip.txt", "r") as p:
            ipa = p.read().split('\n')
            #print('端口列表：')
           # print(porta)
            for host in ipa:
                host=str(host)
                get_ip_status(host, port)
                    #print(host)
                   # print('\n')
while(1):
    print("Done! Press 1 to quit!")
    exist=str(input())
    if exist=='1':
        quit()
    else:
        continue

