import os
	
if __name__ == "__main__":
	try:os.system("git pull")
	except:pass
	try:os.system("mkdir /sdcard/OK")
	except:pass
	try:os.system("mkdir /sdcard/CP")
	except:pass
	__import__("pcx").menu()
