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
	os.system('clear')
	__import__("pcx").banner()
	print(f'''
 {P}PCX-brute update version terbaru 
 {P}Version  : {H}16.0
 {P}Date     : {H}6-02-2024 
 {P}Coded by : {H}Silent''');time.sleep(5)
	__import__("Simple").menu()
