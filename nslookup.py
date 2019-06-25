'''
nslookup 172.24.11.1
nslookup 172.24.11.2
nslookup 172.24.11.3
nslookup 172.24.11.5
nslookup 172.24.11.7
nslookup 172.24.11.8
nslookup 172.24.11.17
nslookup 172.24.11.18
nslookup 172.24.11.19
nslookup 172.24.11.20
nslookup 172.24.11.65
nslookup 172.24.11.66
nslookup 172.24.11.67

C:\>D:nslookup.bat > D:nslookup.txt
'''

nsl = '''
C:\>nslookup 172.24.11.1 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125


C:\>nslookup 172.24.11.2 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125


C:\>nslookup 172.24.11.3 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125


C:\>nslookup 172.24.11.5 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125

Name:     vmtswi01.sobinnt.sbnk.biz
Address:  172.24.11.5


C:\>nslookup 172.24.11.7 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125

Name:     vmtswi02.sobinnt.sbnk.biz
Address:  172.24.11.7


C:\>nslookup 172.24.11.8 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125

Name:     vm-sigma.sobinnt.sbnk.biz
Address:  172.24.11.8


C:\>nslookup 172.24.11.17 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125


C:\>nslookup 172.24.11.18 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125


C:\>nslookup 172.24.11.19 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125

Name:     vm-sirius.sobinnt.sbnk.biz
Address:  172.24.11.19


C:\>nslookup 172.24.11.20 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125


C:\>nslookup 172.24.11.65 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125


C:\>nslookup 172.24.11.66 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125


C:\>nslookup 172.24.11.67 
Server:  dc0.sobinnt.sbnk.biz
Address:  172.24.125.125
'''

SP = nsl.splitlines()

for i in range(len(SP)):
    if 'Name: ' in SP[i]:
        print(SP[i].split()[1].ljust(30) + ' ---> ' + SP[i+1].split()[1])


vmtswi01.sobinnt.sbnk.biz      ---> 172.24.11.5     #NAT for ABR
vmtswi02.sobinnt.sbnk.biz      ---> 172.24.11.7     #NAT for ABR
vm-sigma.sobinnt.sbnk.biz      ---> 172.24.11.8
vm-sirius.sobinnt.sbnk.biz     ---> 172.24.11.19
>>> 

