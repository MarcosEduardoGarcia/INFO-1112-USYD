import sys
import os
import time
import pwd
import stat

'''
Student's name: Marcos Eduardo Garcia Ortiz
ID: 520605309
'''

def get_info(path, g_read, g_exec):
	'''
	Function to extract the properties of the file

	path: path of the file to be analized [string]
	g_read: current state of read permission [bool]
	g_exec: current state of execute permission [bool]

	return: the complete properties [string]
	'''
	# Get size
	size = os.path.getsize(path)
	# Get owner
	owner = pwd.getpwuid(os.stat(path).st_uid).pw_name
	# Get Group
	group = pwd.getpwuid(os.stat(path).st_gid).pw_name
	# Get the last modification date
	modTimeEpoc = os.path.getmtime(path)
	modTime = time.strftime('%b %d  %Y', time.localtime(modTimeEpoc))
	# Get the last access date 
	modTimeEpoc2 = os.path.getatime(path)
	modTime2 = time.strftime('%b %d  %Y', time.localtime(modTimeEpoc2))

	s_out = path + ' Group Readable: ' + str(g_read) +\
	 		',' + ' Group Executable: ' + str(g_exec)+\
			' ' + 'Size: ' + str(size) + ',' + ' Owner: ' + str(owner)+\
			',' + ' Group: ' + str(group) + ',' +\
			' last modified date: ' + str(modTime) + ',' +\
			' last access date: ' + str(modTime2) + '\n'

	return s_out

def main(filelist,output_file):
	'''
	main function execute the reading of file
	and the change of permissions
	
	filelist: The path of the file that contain the paths to the 
	other files e.g filelist.txt [string]

	output_file: The path to output file if the file is not created
	it will be created for example output.txt or folder/output.txt [string]
	'''
	# Creating array to save paths 
	paths = []
	# create the file to write information on it
	out = open(output_file, 'w')
	# Verify if the file of filelist exist 
	if os.path.exists(filelist):
		#open the file and read line by line storing every line in the array
		with open(filelist) as file_in:
			paths = file_in.readlines()
		# Closing the file to avoid corrupting the file
		file_in.close()
		# Deleting the newline character 
		paths = list(map(lambda x:x.strip(),paths))
		#print(paths)
		# For loop to analyze every path
		for path in paths:
			if os.path.exists(path):
				#Getting permisssions of current path
				permissions = os.stat(path).st_mode
				# Get the state of permission read group
				g_read  = bool(permissions & 0o0040)
				# Get the state of permission exec group
				g_exec  = bool(permissions & 0o0010)
				# Getting the properties of file to write on output
				result = get_info(path,g_read,g_exec)
				out.write(result)
				
				#Toggling the group execute permission
				if g_exec == False:
					os.chmod(path, permissions | stat.S_IXGRP)  #BITWISE OR 
				else:
					NO_EXEC_GROUP = ~stat.S_IXGRP
					os.chmod(path, permissions & NO_EXEC_GROUP)	#BITWISE AND		
			else:
				out.write(str(path) + " can not be found\n")
	else:
		warning = filelist + " can not be found\n"
		out.write(warning)
	out.close()

if __name__ == '__main__':
	main('filelist.txt', 'output.txt')

