import os 
def is_hidden(entry):
    return entry.name.startswith(".")

def print_entries(list_of_entries):
    for entry in list_of_entries:
        if entry.is_file() and not is_hidden(entry):
            print("file: ", entry.name, type(entry) ) 
        elif entry.is_dir() and not is_hidden(entry):
            print("dir: ", entry.name, entry.path)


path = os.getcwd()
entries=os.scandir(path)
print_entries(entries)
print()


subdir=os.chdir('sub')
entries=os.scandir(subdir)
print_entries(entries)
