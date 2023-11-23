import cv2
import os
import string
img=cv2.imread("image1.jpg")
msg=input("enter the secret message")
password=input("enter password")
d={}
c={}
for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)
m=0
n=0
z=0
for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3
    
cv2.imwrite("encryptedmsg.jpg",img)
os.system("start encryptedmsg.jpg")

message=""
n=0
m=0
z=0

pas=input("enter passcode for decryption")
    
if password==pas:
    for i in range(len(msg)):
        message=message+c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
    print("decryption message",message)
else:
    print("not valid key")
