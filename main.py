import rsa

# implement 2 helper methods to generate 
# public and private keys

def key_generator():
    (pubkey, privkey) = rsa.newkeys(1024)
    with open('keys/public.pem', 'wb') as pubfile:
        pubfile.write(pubkey.save_pkcs1('PEM'))

    with open('keys/private.pem', 'wb') as privfile:
        privfile.write(privkey.save_pkcs1('PEM'))

# loadign the public and private keys
def load_keys():
    with open('keys/public.pem', 'rb') as pubfile:
        pubkey = rsa.PublicKey.load_pkcs1(pubfile.read())
    with open('keys/private.pem', 'rb') as privfile:
        privkey = rsa.PrivateKey.load_pkcs1(privfile.read())

    return pubkey, privkey

# Encrypting the message function
def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)

# Decription
def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return 'Error'

# sign and verify the message
def sign_sha1(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

# verification
def verify_sha1(message, sig, key):
    try:
        return rsa.verify(message.encode('ascii'), sig, key) == 'SHA-1'
    except:
        return False

key_generator()
pubkey, privkey = load_keys()

# message input from user
message = input('Enter a message: ')
#encrypt message
ciphertext = encrypt(message, pubkey)

# generate signature
signature = sign_sha1(message, privkey)

#  decrypt the message
plaintext = decrypt(ciphertext, privkey)

# print ciphertext and signature
print(f"Ciphertext: {ciphertext}")
print(f"Signature: {signature}")

# check if the signature is valid
if plaintext:
    print(f"Plaintext: {plaintext}")
else:
    print("Error. Unable to decrypt message")

if verify_sha1(plaintext, signature, pubkey):
    print("Signature is valid")
else:
    print('Could not verify signature.')
