import os; import base64;
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class FernetEnc:

	def _get_fernettoken(self, password, salt_byte):
		pass_byte = bytes(password, encoding='utf-8')
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt_byte,
			iterations=320000,
			backend=default_backend())
		token = Fernet(base64.urlsafe_b64encode(kdf.derive(pass_byte)))

		del password; del pass_byte
		return token

	def prepend_salt(self, cipher):
		if cipher['status'] != 200: return cipher['message']

		output = cipher['output']

		return output['hash'] + '.' + output['salt']

	def extract_salt(self, message):
		if '.' in message:
			extension = os.path.splitext(message)[-1]
			return extension[1:]
		else:
			raise ValueError('Error: Failed to extract salt.')

	def encrypt(self, password, message, salt=None, decrypt=False):
		result = {'status': None, 'message': None, 'output':{}}

		#=== Create Salt ===
		if decrypt==True:
			if type(salt) != str:
				result['status'] = 400
				result['message'] = 'Error: Salt of type str is required.'
				del password
				return result
			salt_byte = base64.urlsafe_b64decode(bytes(salt,'utf-8'))
		else:
			if salt != None:
				result['status'] = 400
				result['message'] = 'Error: Leave salt=None for encryption, it will auto-generate.'
				del password
				return result
			salt_byte = os.urandom(16)
			salt = base64.urlsafe_b64encode(salt_byte).decode('utf-8')

		msg_byte = bytes(message, encoding='utf-8')
		token = self._get_fernettoken(password, salt_byte)

		#=== Create Hash ===
		if decrypt==True:
			try:
				hash = base64.urlsafe_b64decode(msg_byte)
				hash_readable = token.decrypt(hash).decode('utf-8')
			except:
				result['status'] = 400
				result['message'] = 'Error: Unable to decrypt hash. Potentially invalid password or salt.'
				del password
				return result
		else:
			hash = token.encrypt(msg_byte)
			hash_readable = base64.urlsafe_b64encode(hash).decode('utf-8')

		result['status'] = 200
		result['message'] = 'Successfully completed.'
		result['output']['hash'] = hash_readable
		result['output']['salt'] = salt

		del password
		return result

class FernetEncGUI:

	def __init__(self, fernetenc,):
		self.fernetenc = fernetenc

	def clear(self):
		os.system('cls' if os.name=='nt' else 'clear')

	def splashscreen(self):
		self.clear()
		print('Welcome to Fernet Encryption!')

	def optionscreen(self):
		print(' ')
		print('What would you like to do?')
		print('(e) Encrypt, (d) Decrypt, (q) Quit')

	def option_enc(self, decrypt=False):
		if decrypt == True:
			keyword = 'Decrypt'
		else:
			keyword = 'Encrypt'
		self.clear()
		print('What is the message you want to {}?'.format(keyword.upper()))
		print(' ')
		message = input('Input your message: ')
		if message == '': self.clear(); print('Exited, no action taken.'); return
		print(' ')

		password = getpass('Password: ')
		if password == '':
			self.clear(); print('Password cannot be blank, no action taken.'); return

		if decrypt == True:
			confirm = password
		else:
			print(' ')
			confirm = getpass('Please confirm password: ')

		self.clear()
		if password != confirm: del password; del confirm; print('Password mismatch, no action taken.'); return

		if decrypt == True:
			salt = self.fernetenc.extract_salt(message)
			data = self.fernetenc.encrypt(password=password,message=message,salt=salt,decrypt=decrypt)
			if data['status'] != 200: self.clear(); print(data['message']); return
			result = data['output']['hash']
		else:
			data = self.fernetenc.encrypt(password=password,message=message,decrypt=decrypt)
			if data['status'] != 200: self.clear(); print(data['message']); return
			result = self.fernetenc.prepend_salt(data)

		print('Status: {}ion complete.'.format(keyword))
		print(' ')

		if decrypt == True:
			print('====== Secret ======')
			print(' ')
			print(result)
		else:
			print('====== Cipher ======')
			print(' ')
			print(result)
		del password; del confirm
		input(); self.clear(); return

	def run(self):
		self.clear()
		self.splashscreen()

		while True:
			self.optionscreen()
			select = input()

			if select not in ('e','d','q'):
				#'(e) Encrypt, (d) Decrypt, (q) Quit'
				self.clear(); print('Invalid selection. Try again.')

			if select == 'q':
				self.clear()
				break

			if select == 'e':
				self.option_enc(decrypt=False)

			if select == 'd':
				self.option_enc(decrypt=True)
