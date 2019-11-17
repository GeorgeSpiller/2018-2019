from PIL import Image
import os
import collections
import sys
import imageManipulations as imgMap

currotp = ""
def loading():
    """Used for printing periods as a loading bar"""
    # Stores how manny previous periods have been printed
    global currotp
    # Escape character to cess the previous line
    sys.stdout.write('\r')
    currotp += "."
    sys.stdout.write(currotp)
    # Flush the sys feed
    sys.stdout.flush()


def loading_flush():
    """Used for finishing printing periods as a loading bar"""
    global  currotp
    currotp = "."
    sys.stdout.flush()
    # Escape off the loading line
    print()

# empty the file used as output for the ExIf data
f = open("ExIf-data-dump.txt", "w+")
f.write("")
f.close()
f = open("ExIf-data-parsed.txt", "w+")
f.write("")
f.close()

# Get current working directory
dirpath = os.getcwd()
# create path to image folders
# get root dir (practical-3) and navigate to /resources/img/spec2-images
LOC = str(os.path.abspath(os.path.join(dirpath, os.pardir))) + "\\resources\\img\\spec2-images\\"

# Generate storage handeler
ImageFile = collections.namedtuple("ImageFile", ["fileName", "fileType", "fileSize", "fileColorMode", "fileLOC"])

# used to store all image names so we can add them to the image storage handler
imgList = []
# loop through all images to get image file names
# 2nd arg specifies the lvl of recursion for the walk (0 only current dir)
for entities in imgMap.walklevel(LOC, 0):
    # entities gives us allot of unnecessary info, the 3rd index is the full name of all image files
    for file in entities[2]:
        # if there are multiple image files in entities we add them to list
        if file not in imgList and file != []:
            # list of all image file names
            imgList.append(file)

# open each image as a file object
for i in range(len(imgList)):
    # check if the type is an image file:
    try:
        im = Image.open(LOC + imgList[i])
    except IOError:
        print(f"invalidFile: file {imgList[i]} is not an image file")
        continue
    # add verified images to storage handler
    im = Image.open(LOC + imgList[i])
    # Store the current image in the named tuple
    currImg = ImageFile(fileName=imgList[i], fileType=im.format, fileSize=im.size, fileColorMode=im.mode,
                        fileLOC=LOC + imgList[i])
# --------- images obtained ---------
    # Pring image imformation
    imgMap.printImageFile(currImg)

    # create thumbnails
    imgMap.createThumbnail(currImg, LOC + "thumbnails\\")
    # ----- apply filters -----
    # loading() here used to add to the progress bar
    loading()

    # apply a blur filter
    imgMap.applyFilter(currImg, LOC + "filters\\BLUR\\", "BLUR", [9])
    loading()
    # apply a contor filter
    imgMap.applyFilter(currImg, LOC + "filters\\CONTOUR\\", "CONTOUR")
    loading()
    # apply a detail filter
    imgMap.applyFilter(currImg, LOC + "filters\\DETAIL\\", "DETAIL")
    loading()
    # apply an edge enhance filter
    imgMap.applyFilter(currImg, LOC + "filters\\EDGE_ENHANCE\\", "EDGE_ENHANCE")
    loading()
    # apply an emboss filter
    imgMap.applyFilter(currImg, LOC + "filters\\EMBOSS\\", "EMBOSS")
    loading()
    # apply a find edges filter
    imgMap.applyFilter(currImg, LOC + "filters\\FIND_EDGES\\", "FIND_EDGES")
    loading()
    # apply an unsharp mask filter
    imgMap.applyFilter(currImg, LOC + "filters\\UNSHARP_MASK\\", "UNSHARP_MASK", [2, 150, 3])
    loading()
    loading_flush()

    # create custom RGB filtered images
    imgMap.customRGBFilter(currImg, LOC + "filters\\RGB-Custom\\")
    # Get ExIf data from image
    imgMap.listTags(currImg)