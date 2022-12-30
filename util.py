from passlib.hash import ldap_md5_crypt


def encrypt_string(string: str):
    return ldap_md5_crypt.hash(string)

def byte_to_string(byte: bytes):
    return str(byte, 'utf-8')