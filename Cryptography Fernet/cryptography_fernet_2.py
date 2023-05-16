from cryptography.fernet import Fernet
import os
import argparse




def generate_key():
	key= Fernet.generate_key()
	with open('secret.key','wb') as f:
		f.write(key)

def load_key():
	with open('secret.key','rb') as f:
		return f.read()
		


password=input("Enter a password: ")
cpassword=input("Confirm password: ")

def encrypt_file(key,filename, password):
	

	if __name__ == "__main__":
		if (password != cpassword):
			print("Passwords do not match!!")
		else:
			parser = argparse.ArgumentParser(description = "[*]Encrypt youre files and password protect them")
			parser.add_argument('file_path', help="Add the name of the file to be encrypted")
			parser.add_argument('mode',choices=['encrypt','decrypt'],help="Choose either encrypt or decrypt")
			args = parser.parse_args()

			if args.mode == 'encrypt':
				generate_key()
				key = load_key()
				encrypt_file(key,args.file_path,password)
				print(f"File ${args.filepath} has been encrypted")

	



