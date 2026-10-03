from pwdlib import PasswordHash 

context = PasswordHash.recommended()

def hash(password:str):
    return context.hash(password)

def verify(plain_password : str, hashed_password: str):
    return context.verify(plain_password, hashed_password)
