import zipfile
# for i in dir(zipfile):
	# print(i)
# with zipfile.ZipFile('files.zip','w',compression=zipfile.ZIP_DEFLATED) as f:
	# f.write('paths.txt')
	# f.write('YouTube.mp4')
with zipfile.ZipFile('C:/Users/BALA/Desktop/developer_survey_2019.zip','r') as f:
	f.extractall('C:/Users/BALA/Desktop/Pandas/data')