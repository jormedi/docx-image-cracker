import os
import sys
from PIL import Image

'''
TODO
    Organizar images? -> row
'''

def main():
    path = "docx-image-extractor/images/"
    ignored = {"Upper.png", ".DS_Store"}
    row = [x for x in os.listdir(path+"word-file/") if x not in ignored]

    for files in row:
	#print(row)
        #print(files)
        #sys.exit()
        background = Image.open(path+"word-file/"+files)
        foreground = Image.open(path+"Upper.png")
        background.paste(foreground, (0, 0), foreground)
        #background.show()
        background.save(path+"out/"+files)
    #sys.exit()



if __name__ == "__main__":
    main()
