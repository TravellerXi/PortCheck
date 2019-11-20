#!/usr/bin/env python
#author:admin@mytlu.cn
# coding:utf-8

import socket
timeout=1
socket.setdefaulttimeout(timeout)
print('Please put "ip.txt" and "port.txt" in the root directory of the D drive.')
def get_ip_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip, port))
        print('connect to ip {0} on port {1} success'.format(ip, port))
        file= open('D:\\sucess.txt','a+')
        file.write('connect to ip {0} on port {1} success\n'.format(ip, port))
        file.close()

    except Exception as err:
        print('connect to ip {0} on port {1} failed'.format(ip, port))
        file = open("D:\\failed.txt", 'a+')
        file.write('connect to ip {0} on port {1} failed\n'.format(ip, port))
        file.close()

    finally:
        server.close()

#data=[]

#print (data)

ip=[]
port=[]
with open("D:\port.txt","r") as f:
    porta=f.read().split('\n')
    #print('主机列表：')
    #print (ipa)
    for port in porta:
        #print (host)
        port=int(port)
        with open("D:\ip.txt", "r") as p:
            ipa = p.read().split('\n')
            #print('端口列表：')
           # print(porta)
            for host in ipa:
                host=str(host)
                get_ip_status(host, port)
                    #print(host)
                   # print('\n')
while(1):
    print("Done!Press 1 to quit")
    exist=str(input())
    if exist=='1':
        quit()
    else:
        continue

