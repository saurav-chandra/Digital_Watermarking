#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image
from math import *


# In[ ]:


def encrypt():
    im1=Image.open("input.jpg")
    dimension=im1.size
    pix=im1.load()
    abc=floor((dimension[0]*dimension[1])/(2*(dimension[0]+dimension[1])))
    flag=0
    if(dimension[0]>dimension[1]):
        efg=floor((dimension[0]*dimension[1])/(abc*(dimension[0]-dimension[1])))
        flag=1
    elif(dimension[0]<dimension[1]):
        efg=floor((dimension[0]*dimension[1])/(abc*(dimension[1]-dimension[0])))
        flag=2
    else:
        efg=floor((dimension[0]*dimension[1])/(abc*(dimension[0]+dimension[1])))
    if(flag==0 or flag==1):
        row=abc
        col=efg
    elif(flag==2):
        row=efg
        col=abc
#     print ('flag is',flag)
#     print ('row is',row)
#     print ('col is',col)
    new_arr1=[]
    new_arr2=[]
    x1=input("Enter the string: ")
#     x2=""
    for i in range(0,len(x1)):
        new_arr1.append(255-ord(x1[i]))
#     for i in range(0,len(x2)):
#         new_arr2.append(255-ord(x2[i]))
#     print (new_arr1)
#     print (new_arr2)
    new_pix=pix[row,col]
#     print ('new_pix',new_pix)
    new_pix1=pix[(new_pix[0]+new_pix[1]),(new_pix[2]+new_pix[0])]
#     print ('new_pix1',new_pix1)
    qwer=int(new_pix[2])
    jkl=int(new_pix[1])
    fgh=int(new_pix[0])
    col=dimension[1]
    row=dimension[0]
#     print ('now row is=',row)
#     print ('now col is=',col)
    for i in range(0,len(x1)):
        ele=new_arr1.pop(0)
#         print ('ele is',ele)
        pix[(fgh+jkl),(qwer+jkl)]=(new_pix1[0],ele,new_pix1[2])
#         print ('changed pixel is',pix[(fgh+jkl),(qwer+jkl)])
#         print ('new_pix[2] is',qwer)
#         print ('new_pix[1] is',jkl)
#         print ('new_pix[0] is',fgh)
#         print ('new_pix1[2] is',new_pix1[2])
#         print ('new_pix1[1] is',new_pix1[1])
#         print ('new_pix1[0] is',new_pix1[0])
#         print ('col is',int(col))
#         print ('row is',row)
        
        qwer=col-(new_pix1[2]/4)
        col=qwer
        jkl=i
        fgh=row-(new_pix1[0]/4)
        row=fgh
        if((new_pix[2]+i)<0):
            print ('Encryption intercepted')
            break
        if((new_pix[1]+i)<0):
            print ('Encryption intercepted')
            break
        new_pix1=pix[(new_pix[0]+i+1),(new_pix[2]+1+i)]
#         print(new_pix1)
#         print()
#     print ('var is',pix[dimension[0]-3,dimension[1]-3])
#     pix[dimension[0]-3,dimension[1]-3]=(0,len(x1),len(x2))
    pix[dimension[0]-3,dimension[1]-3]=(0,len(x1),0)
#     print ('now var is',pix[dimension[0]-3,dimension[1]-3])
    
    '''
    for i in range(0,len(x2)):
        ele=new_arr2.pop(0)
        pix[(new_pix[0]+new_pix[1]),(new_pix[2]+new_pix[1])]=(new_pix1[0],ele,new_pix1[2])
#         print ('changed pixel is',pix[(fgh+jkl),(qwer+jkl)])
        qwer=(col)-new_pix1[2]
        col=qwer
        jkl=i
        fgh=(row)-new_pix1[0]
        row=fgh
        if((new_pix[2]+i)<0):
#             print ('Encryption intercepted')
            pass
        if((new_pix[1]+i)<0):
#             print ('Encryption intercepted')
            pass
        new_pix1=pix[(new_pix[0]+i),new_pix[2]+i]
    '''
    print ('Encryption complete (file saved as output.bmp)')
    im1.save("output.bmp")
#     decrypt()


# In[ ]:


encrypt()


# In[ ]:


def decrypt():
    im1=Image.open("output.bmp")
    dimension=im1.size
    pix=im1.load()
#     print (dimension)
    abc=floor((dimension[0]*dimension[1])/(2*(dimension[0]+dimension[1])))
#     print (abc)
    flag=0
    if(dimension[0]>dimension[1]):
        efg=floor((dimension[0]*dimension[1])/(abc*(dimension[0]-dimension[1])))
        flag=1
    elif(dimension[0]<dimension[1]):
        efg=floor((dimension[0]*dimension[1])/(abc*(dimension[1]-dimension[0])))
        flag=2
    else:
        efg=floor((dimension[0]*dimension[1])/(abc*(dimension[0]+dimension[1])))
    if(flag==0 or flag==1):
        row=abc
        col=efg
    elif(flag==2):
        row=efg
        col=abc
    new_pix=pix[row,col]
#     print ('new_pix is',new_pix)
    new_pix1=pix[(new_pix[0]+new_pix[1]),(new_pix[2]+new_pix[0])]
    qwer=int(new_pix[2])
    jkl=int(new_pix[1])
    fgh=int(new_pix[0])
    col=dimension[1]
    row=dimension[0]
    var=pix[dimension[0]-3,dimension[1]-3]
#     print ('var is',var)
    bv=''
    bv1=''
    for i in range(0,int(var[1])):
#         print (fgh)
#         print (jkl)
#         print (qwer)
        new_var=pix[(fgh+jkl),(qwer+jkl)]
        arre=(chr(255-(new_var[1])))
        bv=bv+arre
        qwer=col-(new_pix1[2]/4)
        col=qwer
        jkl=i
        fgh=row-(new_pix1[0]/4)
        row=fgh
        new_pix1=pix[(new_pix[0]+i+1),(new_pix[2]+1+i)]
    for i in range(0,var[2]):
        new_var=pix[(fgh+jkl),(qwer+jkl)]
        arr1=chr(255-(new_var[2]))
        bv1 +=arr1
        qwer=col-new_pix1[2]
        col=qwer
        jkl=i
        fgh=row-new_pix1[0]
        row=fgh
        new_pix1=pix[(new_pix[0]+i+1),(new_pix[2]+1+i)]
    print('File decrypted succesfully\nEncrypted message is: ',end="")
    print (bv)
    if(var[2]!=0):
        print (bv1)


# In[ ]:


decrypt()


# In[ ]:





# In[ ]:




