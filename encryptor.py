
import random

'''
Euclid's algorithm for determining the greatest common divisor
'''
def gcd(a, b):
    while not b == 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    for i in range(phi):
        if ((e*i)%phi) == 1:
            return i

'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

'''
Given two prime numbers, generate a new keypair.
'''
def generate_keypair(p, q):
    # validate input
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    # phi (φ or ϕ) is the totient of n:
    # the number of integers k in the range 1 ≤ k ≤ n
    # for which the greatest common divisor gcd(n, k) is equal to 1
    phi = (p-1) * (q-1)

    # choose an integer e such that e and phi(n) are co-prime
    e = random.randrange(1, phi)

    # use Euclid's Algorithm to verify that e and phi(n) are co-prime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # return public and private keypair
    # public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

'''
Encrypt a given message using the private key provided.
'''
def encrypt(pk, plaintext):
    # unpack the key into it's components
    key, n = pk
    # convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [
        (ord(char) ** key) % n \
            for char in plaintext]
    # return the array of bytes
    return cipher

'''
Decrypt an cipher using the public key provided.
'''
def decrypt(pk, ciphertext):
    # unpack the key into its components
    key, n = pk
    ciphertext = ciphertext[:-1]
    # generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [
        chr((int(char) ** key) % n) \
        for char in ciphertext]
    # return the array of bytes as a string
    return ''. join(plain)

def print_seprator() -> None:
    print('*'*55)

def print_welcome() -> None:
    print_seprator()
    print('   🔏 RSA Keypair Generator & Encrypter/Decrypter 🔏  ')
    print_seprator()

'''
Run the RSA key generator & provide a user demonstration of its use.
'''

# print_welcome()

# public, private = generate_keypair(17, 23)
# print('Public  🔑', public)
# print('Private 🔑', private)

# message = input('\nEnter a message to encrypt with your private key: \n')
# encrypted_msg = encrypt(private,message)
# print(encrypted_msg)
# print(type(encrypted_msg))

# print_seprator()

# print('Encrypted message:',''.join(map(lambda x: str(x),encrypted_msg)))

# print('Decrypted message:',decrypt(public, encrypted_msg))

# print_seprator()
# print()
