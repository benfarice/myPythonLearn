from os import listdir,rename
def rename_files():
	#find files names in directory
	file_list = listdir(r"/home/youssed/prank")
	print(file_list)
	directory = "/home/youssed/prank/"
	#for each file rename filename
	for item in file_list:
		rename(directory+item,directory+item.translate(None,"0123456789"))
rename_files()