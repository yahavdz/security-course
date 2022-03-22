from __future__ import print_function  
import Crypto.Cipher.AES as AES
import hashlib
import binascii
import tempfile

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
secret = "OBqNBJOOeIE24Q9tsH3ZJQ=="
def generate():
 template = open("/home/ubuntu/environment/machon_lev_cyber_labs/exercises/lab3/file.txt", 'r').read()
 #noise = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))
 #template = template.replace('###KEY###', noise)
 output = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
 output.write(template)
 output.close()
 #pick the hash algo
 algos = [hashlib.sha1(), hashlib.sha256(), hashlib.sha512(), hashlib.md5()];
 for hash_algo in algos:
    hash_algo.update(template);
    h = hash_algo.hexdigest()

    print ("Hashed %s by %s to %s" % (output.name, str(hash_algo), h))
     
     #calculate the hash of the file
    key = pad(h.decode('hex'))[:16]
    iv = key
    
    
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    out_data = cipher.decrypt(secret.decode('base64'))
    print("data")
    print(out_data)
   # out_data_f = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
#    out_data_f.write(out_data.encode('base64'))
    #out_data_f.close()

generate()