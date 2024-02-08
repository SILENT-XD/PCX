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
	print(f'''\n\n\n\n\n\n\n\n\n\n
{P}- PCX-brute update version terbaru 
{P}- Version  : {H}18.0
{P}- Date     : {H}6-02-2024 
{P}- Coded by : {H}Silent\n
{P}- Catatan  :
{P}- Admin tidak bertanggung jawab atas kerusakan dan/ kerugian dalam bentuk apapun.
{P}- Disarankan dan di wajibkan hanya crack akun yang sudah tidak dipakai owner lagi/akun mati.
{P}- Semua ini adalah tanggung jawab anda sendiri.
{P}- Terimah kasih.

     Hormat saya
     ~ {H}Silent{P} ~''');time.sleep(2)
	__import__("pcx").menu()
