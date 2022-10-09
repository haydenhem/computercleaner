import os
import shutil
input("Press enter to start cleaning")
temp = 'C:/Users/' + os.getlogin() + '/AppData/Local/Temp'
recent = 'C:/Users/' + os.getlogin() + '/AppData/Roaming/Microsoft/Windows/Recent'
discordcache = 'C:/Users/' + os.getlogin() + '/AppData/Roaming/discord/Cache'
chromecache = 'C:/Users/' + os.getlogin() + 'AppData/Local/Google/Chrome/User Data/Default/Cache'
bravecache = 'C:/Users/' + os.getlogin() + '/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Cache/Cache_Data'
deleteFileCount = 0
deleteFolderCount = 0
f = open("C://cleaned.temp", "a")

for the_file in os.listdir(temp):
    file_path = os.path.join(temp, the_file)
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

for the_file in os.listdir(recent):
    file_path = os.path.join(recent, the_file)
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
if os.path.exists(discordcache):
    for the_file in os.listdir(discordcache):
        file_path = os.path.join(discordcache, the_file)
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
if os.path.exists(chromecache):
    for the_file in os.listdir(chromecache):
        file_path = os.path.join(chromecache, the_file)
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
if os.path.exists(bravecache):
    for the_file in os.listdir(bravecache):
        file_path = os.path.join(bravecache, the_file)
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
print(str(deleteFileCount) + ' files and ' + str(deleteFolderCount) + ' folders deleted.')
f.close()

