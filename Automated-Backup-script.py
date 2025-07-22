import shutil
import os
import datetime

def backups_file(source,destination):
    today=datetime.date.today()
    backups_file_name=os.join(destination,f"backup_{today}.tar.gz")

shutil.make_archive(backups_file_name,'gztar',source)

source="location of file to Backup"
destination="location where to backup"

backups_file(source,destination)
