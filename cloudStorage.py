import dropbox 

class Transferdata:
    def __init__ (self,access_token):
        self.access_token=access_token
    def upload_file (self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.AsvFp3_5VEHxzx4cLIbFnLW9lLmaRjFAHs4DAfPvQw1iqonOxypwdhvMPL0gW5_yny0-uNaOEV1oCto8l11U2l1WebUMyMzDDH0p7oNZE3_-VgkC1rFXCHk4WR40SewY2VvO5ck'
    transferdata=Transferdata(access_token)
    file_from=input('enter the file path to transfer')
    file_to=input('enter the full path to upload to dropbox')

    transferdata.upload_file(file_from,file_to)
    print('file has been moved')

main()


