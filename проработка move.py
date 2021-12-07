import os
from pathlib import Path


myVars = {}

myVars['srcDirectory'] = r'd:\1\2\3'
myVars['arcDirectory'] = r'd:\2\2\3'

oldPicName = myVars['srcDirectory']+r'\10215\DSCN5875.JPG'

arcPicName = Path(str(oldPicName).replace(myVars['srcDirectory'], myVars['arcDirectory']))




def move(oldPicName, arcPicName):
	os.makedirs(os.path.dirname(arcPicName), exist_ok=True)
	if (os.path.isfile(arcPicName)):
		os.remove(arcPicName)
	# Доработать!
	# Лучшен использовать copy и затем удалять каталог, если он пустой!
	print('переносим', oldPicName, arcPicName)
	os.rename(oldPicName, arcPicName)
	# если сейчас это стал пустой каталог, то попробовать (try) его удалить!
	
	#(dir, subdirs, files) = os.walk(oldPicName, followlinks=True)
	#print(files)
	print('Каталог', os.path.dirname(oldPicName))
	for dir, subdirs, files in os.walk(os.path.dirname(oldPicName), followlinks=True):
		print(files)
		if len(files) == 0:
			print('need delete', os.path.dirname(oldPicName))
			os.removedirs(os.path.dirname(oldPicName))


	#os.renames(oldPicName, arcPicName) # с S - этот удаляет пустые каталоги
	# удалять пустые каталоги, если это не ссылка

move(oldPicName, arcPicName)
move(arcPicName, oldPicName)


#os.makedirs(myVars['srcDirectory'], exist_ok=True)
#try:
#	print('В ', myVars['srcDirectory']+'\\MEGA', ' пересоздаём ссылку на папку с фотками от фотографа: ', myVars['mega'])
#	os.symlink(myVars['mega'], myVars['srcDirectory']+'\\MEGA')
#except:
#	print('Ссылка на MEGA уже есть')
##quit()