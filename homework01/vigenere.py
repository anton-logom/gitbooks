def encrypt_vigenere(plaintext, keyword):
    """
    #  Encrypts plaintext using a Vigenere cipher.
    #
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    >>> encrypt_vigenere("attackatdawn", "lemon")
    'lxfopvefrnhr'
    """

    keyword *= len(plaintext) // len(keyword) + 1
    ciphertext = ''
    for i in range(len(plaintext)):
        upreg = 0
        s = plaintext[i]
        k = keyword[i]
        if ord(s) in range(65, 90):
            upreg = 1
        s = s.lower()
        k = k.lower()
        if ord(s) in range(97, 122):
            if (ord(s) + ord(k) - 97) <= 122:
                s = chr(ord(s) + ord(k) - 97)
            else:
                s = chr(ord(s) + ord(k) - 97 - 26)
        if upreg:
            s = s.upper()
        ciphertext += s

    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    # Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    plaintext = ''
    keyword *= len(ciphertext) // len(keyword) + 1
    for i in range(len(ciphertext)):
        upreg = 0
        s = ciphertext[i]
        k = keyword[i]
        if ord(s) in range(65, 90):
            upreg = 1
        s = s.lower()
        k = k.lower()
        if ord(s) in range(97, 122):
            if (ord(k) - ord(s)) <= 0:
                s = chr(ord(s) - ord(k) + 97)
            else:
                s = chr(ord(s) - ord(k) + 97 + 26)
        if upreg:
            s = s.upper()
        plaintext += s

    return plaintext
