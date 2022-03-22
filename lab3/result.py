from __future__ import print_function  
import Crypto.Cipher.AES as AES
import hashlib
import binascii
import tempfile


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
secret = 'OBqNBJOOeIE24Q9tsH3ZJQ=='
def generate():
 template = open("/home/ubuntu/environment/machon_lev_cyber_labs/exercises/lab3/file.txt", 'r').read()
 # print(template)
 #output = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
 #output.write(template)
 #output.close()

 
 #pick the hash algo
 algos = [hashlib.sha1(), hashlib.sha256(), hashlib.sha512(), hashlib.md5()]
 for hash_algo in algos:
     hash_algo.update(template.encode("utf-8"))
     h = hash_algo.digest()

     print('Hashed by %s to %s' % (str(hash_algo), h))
     #calculate the hash of the file
    # secret = 'SECRET'+''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    # print(bytes.fromhex('68656c6c6f').decode('utf-8'))

     key = pad(h.decode('utf-8', 'ignore'))[:16]
     print(key)
     iv = key
     secret.decode('base64')
     cipher = AES.new(key, AES.MODE_CBC, IV=iv)
     out_data = cipher.decrypt(secret.decode('base64'))
     print(out_data)
     out_data_f = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    # print(out_data.decode('base64'))
    # out_data_f.write(out_data.decode('base64'))
     out_data_f.close()

generate()