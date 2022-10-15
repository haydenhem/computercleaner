import os
import shutil
import winshell
input("Press enter to start cleaning")
path = ""
temp = 'C:/Users/' + os.getlogin() + '/AppData/Local/Temp'
recent = 'C:/Users/' + os.getlogin() + '/AppData/Roaming/Microsoft/Windows/Recent'
discordcache = 'C:/Users/' + os.getlogin() + '/AppData/Roaming/discord/Cache'
chromecache = 'C:/Users/' + os.getlogin() + '/AppData/Local/Google/Chrome/User Data/Default/Cache'
bravecache = 'C:/Users/' + os.getlogin() + '/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Cache/Cache_Data'
deleteFileCount = 0
deleteFolderCount = 0
deleteSkipCount = 0
f = open(os.getcwd() + "\cleaned.temp", "a")

actuatethrough = 0

while actuatethrough < 4:
    if actuatethrough == 0:
        path = temp
    elif actuatethrough == 1:
        path = recent
    elif actuatethrough == 2:
        path = discordcache
    elif actuatethrough == 3:
        path = chromecache
    elif actuatethrough == 4:
         path = bravecache
    if os.path.exists(path):
        for the_file in os.listdir(path):
            file_path = os.path.join(path, the_file)
            indexNo = file_path.find('\\')
            itemName = file_path[indexNo + 1:]
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    #   print('%s file deleted' % itemName)
                    deleteFileCount = deleteFileCount + 1
                    f.write('%s file deleted' % itemName + '\n')

                elif os.path.isdir(file_path):
                    if file_path.__contains__('chocolatey'):  continue
                    shutil.rmtree(file_path)
                    #  print('%s folder deleted' % itemName)
                    deleteFolderCount = deleteFolderCount + 1
                    f.write('%s folder deleted' % itemName + '\n')

            except Exception as e:
                f.write('Access Denied: %s' % itemName + '\n')
                deleteSkipCount = deleteSkipCount + 1
    actuatethrough += 1
    # i do this because it errors but still works anyway
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    except:
        pass
print(str(deleteFileCount) + ' files and ' + str(deleteFolderCount) + ' folders deleted. There were {} skipped files/folders'.format(deleteSkipCount))
f.close()

