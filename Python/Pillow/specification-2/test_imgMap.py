import collections
import imageManipulations as imgMap
from PIL import Image
import os

ImageFile = collections.namedtuple("ImageFile", ["fileName", "fileType", "fileSize", "fileColorMode", "fileLOC"])
# Get current working directory
dirpath = os.getcwd()
# create path to image folders
# get root dir (practical-3) and navigate to /resources/img/spec2-images
LOC = str(os.path.abspath(os.path.join(dirpath, os.pardir))) + "\\resources\\img\\spec2-images\\"
outp = str(os.path.abspath(os.path.join(dirpath, os.pardir))) + "\\specification-2\\tmp_testFiles\\"
# sample image used for testing
name = "image01.jpg"
im = Image.open(LOC + name)

# different edge case images to test
testimage_valid = ImageFile(fileName=name, fileType=im.format, fileSize=im.size, fileColorMode=im.mode,
                       fileLOC=LOC + name)
testimage_thumb1 = ImageFile(fileName="thumb-textimage.jpg", fileType="jpg", fileSize=1000, fileColorMode="RGB",
                       fileLOC="tmp")
testimage_filt1 = ImageFile(fileName="filtr-textimage.jpg", fileType="jpg", fileSize=1000, fileColorMode="RGB",
                       fileLOC="tmp")



# tests:
def test_thumbnail_invalidFilename():
    """test for invalid file name"""
    global testimage_thumb1, outp
    assert imgMap.createThumbnail(testimage_thumb1, outp) == False

def test_thumbnail_validimage():
    """Test for valid image"""
    global testimage_valid, outp
    assert imgMap.createThumbnail(testimage_valid, outp) == None

def test_applyFilter_invalidFilename():
    """test for invalid file name"""
    global testimage_filt1, outp
    assert imgMap.applyFilter(testimage_filt1, outp, "BLUR", [9]) == False

def test_applyFilter_invalidFilterType1():
    global testimage_valid, outp
    assert imgMap.applyFilter(testimage_filt1, outp, "", [9]) == False

def test_applyFilter_invalidFilterType2():
    global testimage_valid, outp
    assert imgMap.applyFilter(testimage_filt1, outp, "AAAAAA", [9]) == False

def test_applyFilter_invalidFilterType3():
    global testimage_valid, outp
    assert imgMap.applyFilter(testimage_filt1, outp, "284O@[]G£7HF^H", [9]) == False

def test_applyFilter_validimage():
    """Test for valid image"""
    global testimage_valid, outp
    assert imgMap.applyFilter(testimage_valid, outp, "BLUR", [9]) == None

def test_maximum_min01():
    assert imgMap.maximum(0, 0, 0) == (0, 0, 0)

def test_maximum_min02():
    assert imgMap.maximum(0, 0, 119) == (0, 0, 0)

def test_maximum_min03():
    assert imgMap.maximum(70, 31, 18) == (0, 0, 0)

def test_maximum_max01():
    assert imgMap.maximum(255, 255, 255) == (255, 255, 255)

def test_maximum_max02():
    assert imgMap.maximum(255, 255, 191) == (255, 255, 255)

def test_maximum_max03():
    assert imgMap.maximum(199, 251, 253) == (255, 255, 255)

def test_maximum_Rmin():
    assert imgMap.maximum(60, 30, 31) == (255, 0, 0)

def test_maximum_Rmax():
    assert imgMap.maximum(255, 254, 100) == (255, 0, 0)

def test_maximum_Gmin():
    assert imgMap.maximum(30, 60, 31) == (0, 255, 0)

def test_maximum_Gmax():
    assert imgMap.maximum(254, 255, 100) == (0, 255, 0)

def test_maximum_Bmin():
    assert imgMap.maximum(30, 31, 60) == (0, 0, 255)

def test_maximum_Bmax():
    assert imgMap.maximum(254, 100, 255) == (0, 0, 255)

def test_customRGB_invalidFilename():
    """test for invalid file name"""
    global testimage_filt1, outp
    assert imgMap.customRGBFilter(testimage_filt1, outp) == False

def test_customRGB_validimage():
    """Test for valid image"""
    global testimage_valid, outp
    assert imgMap.customRGBFilter(testimage_valid, outp) == None
