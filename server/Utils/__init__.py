import hashlib

def hashPwd(pwd):
    encoded = hashlib.sha512(pwd.encode()).hexdigest()
    return encoded