import os
from PIL import Image
import re, PIL
from pathlib import Path

def resizeFoto(oldPicName, baseheight):
	file = os.path.basename(oldPicName)
	outDirectory = os.path.dirname(oldPicName)
	# Может проверять?
	#if os.path.isfile(Path(outDirectory,baseheight,file)): return()
	# Уменьшение размера фоток
	img = Image.open(oldPicName)

	if baseheight < 301:
		if img.size[1] > img.size[0]:
			hpercent = (baseheight / float(img.size[1]))
			wsize = int((float(img.size[0]) * float(hpercent)))
			img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
		else:
			wpercent = (baseheight / float(img.size[0]))
			hsize = int((float(img.size[1]) * float(wpercent)))
			img = img.resize((baseheight, hsize), PIL.Image.ANTIALIAS)
	else:
		hpercent = (baseheight / float(img.size[1]))
		wsize = int((float(img.size[0]) * float(hpercent)))
		img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)

	dstDir = Path(outDirectory,'_h'+str(baseheight))
	newPicName = Path(dstDir, file)
	os.makedirs(dstDir, exist_ok=True)
	if ( os.path.isfile(Path(newPicName)) ):
		os.remove(newPicName)
	img.save(newPicName)
	#print( "\tresizeFoto({}->{}\\{})".format(oldPicName, dstDir, file) )
	return(newPicName)

def listFoto(rootDir):
	print(rootDir)
	for dir, subdirs, files in os.walk(rootDir, followlinks=True):

		print(dir)
		rubbish = []
		rubbish = re.findall("(rubbish)", dir, re.IGNORECASE)
		if rubbish:
			print('Пропускаем папку Rubbish!')
			continue # пропускаем папку Rubbish

		i = 0
		for file in files:
			names = []
			names = re.findall("-1\.(jpe*g)$", file, re.IGNORECASE)
			if names:
				i+=1
				print(i, file)

				smallNewPicNameW = resizeFoto(rootDir+'\\'+file, 300)

if __name__ == '__main__': 
	listFoto('d:\\!!root_tiu_foto')

# ok