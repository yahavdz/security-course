from __future__ import print_function  
import Crypto.Cipher.AES as AES
import hashlib
import binascii

coins = ["Bitcoin", "Ethereum", "BNB", "XRP", "Terra", "Cardano", "Solana", "Avalanche", "Polkadot", "Dogecoin"]

for coin in coins:
     
     sec = hashlib.sha384((str.encode(coin) + str.encode(coin[::-1])  + b'2022')).digest()
     cipher = AES.new(sec[:32], AES.MODE_ECB)

     # notice - the message' length is divisible by 16
     message = b'18051d0908f4cba9f23d474a3de4d96e3628a3d8232b75295adccca724e8272b'
     secret = cipher.decrypt(binascii.unhexlify(message))
     print("%s -> %s" % (coin, secret))
     
# explaination:
# I took a list of the first 10 coins
# Then check each of them if this is the correct coin by decrypting the message 
# Print all the results and looking for normal message in the output