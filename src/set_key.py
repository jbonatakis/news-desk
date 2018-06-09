import os
import getpass
import time

def set_key():
	home = os.path.expanduser('~')
	try:
		os.makedirs(os.path.join(home, '.nd_config'))
		f = open(home +'/.nd_config/key', 'w')
		print("Welcome to News Desk! You need an API key. Please point your browser to https://newsapi.org, register for a free developer account, and copy your API key.")
		print("Once you complete this process you will not need to repeat it unless you regenerate your API key or delete the key file.")
		key = str(getpass.getpass("Enter newsapi.org key here >> ")).strip()
		f.write(key)
		f.close()
		print("Key saved to ~/.nd_config/key. Gathering your news now...")
		print("\n")
		time.sleep(5)

	except FileExistsError:
		f = open(home + '/.nd_config/key', 'w')
		print("Your API key is invalid. Please point your browser to https://newsapi.org, confirm your API key, and enter it below.")
		key = str(getpass.getpass("Enter newsapi.org key here >> ")).strip()
		f.write(key)
		f.close()
		print("Key saved to ~/.nd_config/key. Gathering your news now...")
		print("\n")
		time.sleep(5)
