from cryptography.fernet import Fernet
import os

f=Fernet('ljjugfff')
fi=os.listdir()[0]
f.encrypt(fi)