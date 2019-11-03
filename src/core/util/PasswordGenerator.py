import hashlib, binascii, os


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(782)).hexdigest().encode('ascii')
    password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                        salt, 100000)
    password_hash = binascii.hexlify(password_hash)
    return (salt + password_hash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    password_hash = hashlib.pbkdf2_hmac('sha512',
                                        provided_password.encode('utf-8'),
                                        salt.encode('ascii'),
                                        100000)
    password_hash = binascii.hexlify(password_hash).decode('ascii')
    return password_hash == stored_password
