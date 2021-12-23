import os; import base64;
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

	def _prepend_salt(self, encryption_results):
		if encryption_results['status'] != 200: return encryption_results['message']

		output = encryption_results['output']

		return output['hash'] + '.' + output['salt']

	def _extract_salt(self, message):
		if '.' in message:
			extension = os.path.splitext(message)[-1]
			return extension[1:]
		else:
			raise ValueError('Error: Failed to extract salt.')

	def fernet_enc(self, message, password, salt=None, decrypt=False):
		"""
		Example data inputs:
		data = {'medium': 'file', 'input': '/filepath/example', 'outpath': '/example-c', 'salt': None}
		data = {'medium': 'text', 'input': 'hello world', 'outpath': None, 'salt': None}
		"""
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