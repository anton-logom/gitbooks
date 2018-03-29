def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    ciphertext = ''
    for s in plaintext:
        if ord(s) in range(65, 87) or ord(s) in range(97, 119):
            ciphertext += chr(ord(s) + 3)
        else:
            if ord(s) in range(88, 90) or ord(s) in range(120, 122):
                ciphertext += chr(ord(s) - 23)
            else:
                ciphertext += s

    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for s in ciphertext:
        if ord(s) in range(68, 90) or ord(s) in range(100, 122):
            plaintext += chr(ord(s) - 3)
        else:
            if ord(s) in range(65, 67) or ord(s) in range(97, 99):
                plaintext += chr(ord(s) + 23)
            else:
                plaintext += s
    return plaintext
