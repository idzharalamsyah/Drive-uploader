from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LoadSettingsFile("settings.yaml")
gauth.CommandLineAuth()  # sekali login, nanti pakai refresh token

drive = GoogleDrive(gauth)

f = drive.CreateFile({'title': 'contoh.txt'})
f.SetContentFile('contoh.txt')
f.Upload()

print("Upload selesai!")
