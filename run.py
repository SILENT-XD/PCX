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
	print(f'''
 {P}PCX-brute update version terbaru 
 {P}Version  : {H}16.0
 {P}Date     : {H}6-02-2024 
 {P}Coded by : {H}Silent
 
 Catatan :
 {P}Admin tidak bertanggung jawab atas kerusakan dan/ kerugian dalam bentuk apapun.\n
 {P}Disarankan dan di wajibkan hanya crack akun yang sudah tidak dipakai owner lagi/akun mati.\n
 {P}Semua ini adalah tanggung jawab anda sendiri.\n
 {P}Terimah kasih.\n

 Hormat saya
 ~ {H}Silent{P} ~''');time.sleep(5)
	__import__("pcx").menu()
