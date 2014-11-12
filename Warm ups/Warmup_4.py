"""
add_comment <file> <msg>
Example usage at Shell Prompt / Terminal

add_comment notes "#todo Call that cool person I met at that party"
Description of Behavior

Appends remark to end of text file.
Leaves an extra blank line between the new remark and the existing content ** but doesn't accidentally leave 2 if the last line was already blank.
Limitations
"""




# !/bin/bash

# file="$1"
# msg="$2"
# if [[ `tail -n 1 "$file"` ]];   then echo "" >> "$file";   fi
# echo -e "$msg" >> "$file"


 # -- FILE “example.txt” START --
 #   "This is an example file."

 #  -- FILE “example.txt” END --

 # add_comment example.txt "#todo Call that cool person I met at that party"

def add_comment(string_data, remark):
	return string_data + remark 

 #remark("This is an example file.")

 #add string_data + remark 



"""
Austin Coding Academy Warmup challenge!

Create a script that does the same thing in Python:

Make a function def add_comment(string_data, remark) that adds the remark to the string_data and returns the resulting string_data 
with the new comment added. Remember to leaves an extra blank line between the new remark and the existing content, but don't leave 2!

BONUS 1: Make a function def add_comment_to_file(filename, remark) that uses your first function add_comment to add the remark to the file named filename.
BONUS 2: Use if __name__ == "__main__" to let your python script be used from the command line just like my bash script.
"""