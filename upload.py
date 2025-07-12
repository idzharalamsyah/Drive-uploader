from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Inisialisasi langsung dengan settings.yaml
gauth = GoogleAuth(settings_file="settings.yaml")
gauth.CommandLineAuth()

drive = GoogleDrive(gauth)

file = drive.CreateFile({'title': 'contoh.txt'})
file.SetContentFile('contoh.txt')
file.Upload()

print("✅ Upload selesai!")
