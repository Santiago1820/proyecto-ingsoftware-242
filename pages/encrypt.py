import hashlib
def encriptar(contraseña):
    md5 = hashlib.md5(contraseña.encode()).hexdigest()
    sha256 = hashlib.sha256(md5.encode()).hexdigest()
    hash = hashlib.sha256(sha256.encode()).hexdigest()
    return hash