def get_dir():
	import os
	return os.getcwd()
def change_dir(directory):
	import os
	os.chdir(directory)
	return "Directory changed to "+os.getcwd()