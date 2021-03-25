import zipfile
import os
# for i in dir(zipfile):
	# print(i)
os.chdir("..")
a=os.getcwd()

with zipfile.ZipFile(a+'/files.zip','w',compression=zipfile.ZIP_DEFLATED) as f:
	for i in os.listdir(a+'/coddde'):
		print(i)
		if os.path.isdir(i):
    			for j in i:
    				f.write(j)
		else:
    			f.write(i)
# zipfile_name=input('Enter path to folder')
# extract_file_destination=input('Extract folder location')
# with zipfile.ZipFile(zipfile_name,'r') as f:
# 	f.extractall(extract_file_destination)