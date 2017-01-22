#
# consistency.py - v0.0.1
# License not decided yet.
#

#--------------------------------------------#
# TODO:                                      #
#  * Use arguments instead of manual editing #
#  * Test on Windows                         #
#  * Improve naming of functions and vars    #
#  * (pip package?)                          #
#--------------------------------------------#

import glob, os

"""
  This function changes all the detected files within a directory, using
the blob in specified in the line 26 and the 'dir' argument, to have
their trailing tabs and spaces stripped. 

  It also ensures that those files EOL character is the one specified in
line 31 and 32, and that the file will end with an EOL character.
"""
def refactor(dir):
	os.chdir((dir+"/"))
	for file in glob.glob("*.py"): # Change to match your requirements
		f = open(file, 'r+')

		lines = f.readlines()
		lines = [line.rstrip() for line in lines]
		text = "\r\n".join(lines) # Change to match your desired EOL
		text += "\r\n"            # Same as above

		f.seek(0)
		f.write(text)
		f.truncate()
		f.close()

#
#   If for example, one wants to refactor 'folder1' and 'folder2', which
# are in the same directory as this file, the code could be:
#
#
# full_path = os.path.dirname(os.path.abspath(__file__))
#
# refactor(full_path);
# refactor(full_path + "folder1");
# refactor(full_path + "folder2");
#
