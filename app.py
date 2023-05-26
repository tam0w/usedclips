import os
def cleanname(sfk):
    if sfk.endswith('sfk'):
        newname = sfk.replace('.sfk','')
    elif sfk.endswith('sfk1'):
        newname = sfk.replace('.sfk1','')
    elif sfk.endswith('sfk0'):
        newname = sfk.replace('.sfk0','')
    return newname

# cwd = os.getcwd()
cwd = "E:\Videos\Valorant"
os.chdir(cwd)
dlist = os.listdir()

used = "usedclips"
path = os.path.join(cwd,used)

print("Current working directory:", cwd)
print('The total number of files in the current directory are:',len(dlist))

try:
    os.mkdir(path)
    print('Folder for used clips created.')
except:
    print('Ready to go.')

sfklist = []
usedmp4list = []

for name in dlist:
    if str.__contains__(name,'.sfk') == True:
        sfklist.append(name)
        print(len(sfklist))

        clean = cleanname(name)
        usedmp4list.append(clean)

for name in usedmp4list:
    os.rename(name,name,cwd,path)