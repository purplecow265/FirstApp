filename = raw_input("Enter location of file you want to add: ")
message = raw_input("Enter a message: ")
branchname = raw_input("Specify a branch")
from subprocess import call
call(["git", "add", filename])
call(["git", "commit", "-m", message])
call(["git", "push", "origin", branchname])
