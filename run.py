import os
H = '\x1b[38;5;43m'
	
if __name__ == "__main__":
	try:os.system("git pull")
	except:pass
	try:os.system("mkdir /sdcard/OK")
	except:pass
	try:os.system("mkdir /sdcard/CP")
	except:pass
	print(f"\n {H}Update terbaru 6 February 2024 ");time.sleep(4)
	__import__("pcx").menu()
