#pip install wget
import wget
url=input('Link ')
print('Download started')
file_name=input('Name')
wget.download(url,file_name)
print('Download  Completed')