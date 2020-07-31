import zipfile
# for i in dir(zipfile):
	# print(i)
# with zipfile.ZipFile('files.zip','w',compression=zipfile.ZIP_DEFLATED) as f:
	# f.write('paths.txt')
	# f.write('YouTube.mp4')
zipfile_name=input('Enter path to folder')
extract_file_destination=input('Extract folder location')
with zipfile.ZipFile(zipfile_name,'r') as f:
	f.extractall(extract_file_destination)