import os,datetime,time
H = '\x1b[38;5;43m'
P = '\x1b[38;5;255m'
	
if __name__ == "__main__":
	try:os.system("git pull")
	except:pass
	try:os.system("mkdir /sdcard/OK")
	except:pass
	try:os.system("mkdir /sdcard/CP")
	except:pass
	print(f'''\n
 {P}PCX-brute update version terbaru 
 {P}Version  : {H}16.0
 {P}Date     : {H}6-02-2024 
 {P}Coded by : {H}Silent''');time.sleep(4)
	__import__("pcx").menu()
