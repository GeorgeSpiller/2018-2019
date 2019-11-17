from PIL import Image
from PIL import ImageFilter
from PIL.ExifTags import TAGS
import os
import sys

pixArray = []

def loading(val, maxVal):
    """Used for printing periods as a loading bar"""
    sys.stdout.write('\r')
    sys.stdout.write(f"{val} / {maxVal}")
    sys.stdout.flush()


def walklevel(some_dir, level=1):
    """Addaptaion on os.walk but allowing to select the level of recursion.
    Taken from: https://stackoverflow.com/questions/229186/os-walk-without-digging-into-directories-below"""
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

def printImageFile(ifobj):
    """Print all the attributes in a ImageFile named tuple object"""
    print(f"fileName:'{ifobj.fileName}'     fileType:'{ifobj.fileType}'     fileSize:'{ifobj.fileSize}'"
          f"     fileColorMode:'{ifobj.fileColorMode}'      fileLOC:'{ifobj.fileLOC}'")


def createThumbnail(imgObj, outpLoc, size = 128):
    """Create a thumbnail of imgObj at location outpLoc"""
    # format the size to be a tuple
    size = (size, size)
    # format the output dir: if it doesnt exist create it
    if os.path.isdir(outpLoc):
        pass
    else:
        os.makedirs(outpLoc)
    # check if the imgObj is a thumbnail already
    if "thumb" in imgObj.fileName:
        # don't do anything
        return False
    # create the thumbnail:
    # open image file
    im = Image.open(imgObj.fileLOC)
    # set it to size parameter
    im.thumbnail(size)
    # save image file at output location
    im.save(outpLoc + "thumb-" + imgObj.fileName.split(".")[0] + ".jpg")


def applyFilter(imgObj, outpLoc, filterType, customArgs = [0]):
    """Aplly filter to an image, if arguments arr required use the list customArgs
    Help from: https://hhsprings.bitbucket.io/docs/programming/examples/python/PIL/ImageFilter.html"""
    # format the output dir: if it doesnt exist create it
    if os.path.isdir(outpLoc):
        pass
    else:
        os.makedirs(outpLoc)
    # check if the imgObj is a thumbnail already
    if "filtr" in imgObj.fileName:
        # don't do anything
        return False
    # apply filter based on filter type:
    # open image file
    im = Image.open(imgObj.fileLOC)
    # apply filter based on filterType argument
    if filterType == "BLUR":
        currImFltr = im.filter(ImageFilter.BoxBlur(customArgs[0]))
    elif filterType == "CONTOUR":
        currImFltr = im.filter(ImageFilter.CONTOUR())
    elif filterType == "DETAIL":
        currImFltr = im.filter(ImageFilter.DETAIL())
    elif filterType == "EDGE_ENHANCE":
        currImFltr = im.filter(ImageFilter.EDGE_ENHANCE_MORE())
    elif filterType == "EMBOSS":
        currImFltr = im.filter(ImageFilter.EMBOSS())
    elif filterType == "FIND_EDGES":
        currImFltr = im.filter(ImageFilter.FIND_EDGES())
    elif filterType == "UNSHARP_MASK":
        currImFltr = im.filter(ImageFilter.UnsharpMask(radius=customArgs[0], percent=customArgs[1], threshold=customArgs[2]))
    else:
        print(f"no filter for filter type: {filterType}")
        return False
    # save filtered image
    currImFltr.save(outpLoc + "filtr-" + filterType + "-" + imgObj.fileName)


def maximum(r, g, b):
    """Used for calculating the largest pixel value of RGB
    returns the normalised pixel vale + 255"""
    list = [r, g, b]
    if (r + b + g) > 700:
        return (255, 255, 255)
    if (r + b + g) < 120:
        return (0, 0, 0)
    if max(list) == r:
        return (255, 0, 0)
    if max(list) == g:
        return (0, 255, 0)
    if max(list) == b:
        return (0, 0, 255)


def customRGBFilter(imgObj, outpLoc):
    """Aplly custom RGB filter"""
    # format the output dir: if it doesnt exist create it
    if os.path.isdir(outpLoc):
        pass
    else:
        os.makedirs(outpLoc)
    # check if the imgObj is a thumbnail already
    if "filtr" in imgObj.fileName:
        # don't do anything
        return False
    print("Generating custom RGB filter:")
    # For each pixel in image
    # Get pixel value
    # set it to omly the predominant RGB color
    im = Image.open(imgObj.fileLOC)
    outpim = Image.new(mode="RGB", size=im.size)
    px = outpim.load()
    width, height = im.size
    for x in range(width):
        loading(x, im.size[0])
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            outpim.putpixel((x, y), maximum(r, g, b))

    outpim.save(outpLoc + "filtr-customRGB-" + imgObj.fileName)
    print()


def listTags(imgObj):
    """ Extact ExIf tags from image to text file
    with help from: https://developer.here.com/blog/getting-started-with-geocoding-exif-image-metadata-in-python3"""
    # open image file
    im = Image.open(imgObj.fileLOC)
    # Get raw ExIf data
    exif_data = im._getexif()
    # used to store a dictionary of the ExIf data
    labeled = {}
    # Catch any images that do not have any metadata tags
    try:
        for (key, val) in exif_data.items():
            labeled[TAGS.get(key)] = val
    except AttributeError:
        print("AttributeError: This image has no readable ExIf Tags")
    # Write ExIf tags into text files,
    # ExIf-data-dump.txt: used for all ExIf data
    # ExIf-data-parsed.txt: used for specific useful ExIf data
    f = open("ExIf-data-dump.txt", "a+")
    f2 = open("ExIf-data-parsed.txt", "a+")
    f.write("------------------------------------------------------------ \n")
    f.write(imgObj.fileName + " \n")
    f.write("------------------------------------------------------------ \n")
    f2.write("------------------------------------------------------------ \n")
    f2.write(imgObj.fileName + " \n")
    f2.write("------------------------------------------------------------ \n")
    # List of all the useful ExIf data tags
    keyList = ["DateTimeOriginal", "DateTimeDigitized", "ExifImageWidth", "ExifImageHeight", "Make", "Model", "XResolution", "YResolution", "ISOSpeedRatings", "ResolutionUnit", "WhiteBalance"]
    for key in labeled:
        # Filter out keys that contain un-usable binary data dumps
        if key == "MeteringMode" or key == "UserComment" or key == "MakerNote" or key == "PrintImageMatching":
            continue
        # Write to ExIf dump
        f.write(f"key:{key}, val:{labeled.get(key)} \n")
        if key in keyList:
            # If the label is useful write to ExIf parsed
            f2.write(f"key:{key}, val:{labeled.get(key)} \n")
    f.close()
    f2.close()

