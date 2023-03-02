import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print("[*] koneksi anda buruk,silahkan refresh data anda.")
	exit()
	
if __name__ == "__main__":
	os.system("git pull")
	os.system("mkdir /sdcard/OK")
	os.system("mkdir /sdcard/CP")
	if "Indonesia" == fc:
		__import__("pcx").menu()
	else:
		__import__("pcx").menu()