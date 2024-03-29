import sys, os, time

def get_current_directory():
    if getattr(sys, 'frozen', False):
        # Running in a PyInstaller bundle
        return os.path.dirname(sys.executable)
    else:
        # Running in a normal Python environment
        return os.path.dirname(os.path.abspath(__file__))
# Example usage:
cwd = get_current_directory()
def cleanname(sfk):
    '''Strips the .sfk ends from each of the files and returns the cleaned name
    which can be used for locating the respective mp4 file.'''

    if sfk.endswith('sfk'):
        newname = sfk.replace('.sfk','')
    elif sfk.endswith('sfk1'):
        newname = sfk.replace('.sfk1','')
    elif sfk.endswith('sfk0'):
        newname = sfk.replace('.sfk0','')

    return '\\'+newname

# Locating the directory and listing files in it

dlist = os.listdir()

print("Current working directory:", cwd)
print('The total number of files in the current directory are:',len(dlist))

path = os.path.join(cwd, 'used_clips')

# Folder Creation

try:
    os.mkdir(path)
    print('Folder for used clips created.')
except:
    print('Ready to go.')
finally:
    print('This is the path of the destination:', path)

# Initializing the lists:

sfklist = []
usedmp4list = []

for name in dlist:
    if str.__contains__(name,'.sfk') == True:
        sfklist.append(name)

        clean = cleanname(name)
        usedmp4list.append(clean)

        dest = path + clean
        curfile = cwd + clean

        try:
            os.rename(curfile, dest)
            print(clean, 'has been moved.')
            print(len(usedmp4list))

        except FileNotFoundError:
            print('File has been deleted earlier.')

time.sleep(10)
