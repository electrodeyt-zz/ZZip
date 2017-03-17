### This program requires Python 3.
# ZZip
ZZip is a File compression format with up to 80% File Compression (See Tests) and a extracter for its format.

# How it works
ZZip uses LZMA2 Compression. The magic Bytes are 5A 5A 49 50 31 2E 30, also "ZZIP1.0" in UTF-8. After these bytes, there are three 20's, " " in UTF-8.
# Tests
The tests were performed on a Computer (duh) with these Specs:
  i5 4440
  
  16GB of Ram
  
  GTX960 (This does not effect results)
  
The Blender Test file (Found under the Test Files folder) is 453.452 bytes large. The compressed file (also present in the Test Folder) is 83.516 bytes large.
This makes the Compressed file 81% Smaller. Keep in mind that the size differance **WILL** vary **A LOT** between types of files, as files with more random Content inside of them will have wore Precentages.

Using complety Random files genrated with dd from /dev/urandom yieled a far worse Percantage, with only a drop of about 30 Mb of a 131 Mb test file.

# What is possible and what isn't
~~At the moment ZZip can only compress 1 File at a time~~ *It is now possible to compress a Folder.* and it Compresses/Decompresses in ram before writing it to the disk, making it slower than other compression software.
~~I would **NOT** recommend using this, as~~



The MIT License applies to both the Extracting Software and the File format.

# Downloads
You can download the Extractor/Compressor from http://github.com/electrodeyt/ZZip/releases .
