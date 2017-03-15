import lzma
import sys
import os
import io
import tarfile
#ZZip Extracter Version 1.2
#Copyright (c) Alexander Richards
tar_bytes = bytes()
version = 1.2
write_string_identifier_dir = "ZZIP1.0DIR   "
write_string_identifier = "ZZIP1.0   "
string_identifier = "ZZIP1.0"
string_identifier_dir = "ZZIP1.0DIR"
filterstouse = [
    {"id": lzma.FILTER_DELTA},
    {"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME},
]
probsdirectunzzip = False
def compressfolder(folder_to_compress, file_name_archive):
    tar_io = io.BytesIO(tar_bytes)
    memtarfile = tarfile.TarFile(fileobj=tar_io, mode="w")
    print("Creating Tar File in Memory. This may take some time and may crash!")
    print("Please close unimportent applications to make sure it does not crash.")
    memtarfile.add(name=folder_to_compress,recursive=True)
    memtarfile.close()
    print("Done. DO NOT CLOSE ZZIP EXTRACTOR JUST YET! There are still some things to do.")
    clzma = lzma.LZMACompressor(format=lzma.FORMAT_RAW,filters=filterstouse)
    f = open(file_name_archive, "ab")
    f.write(bytes(write_string_identifier_dir, "ASCII"))
    print("Now compressing. Please wait")
    tempcompress = clzma.compress(tar_io.getvalue())
    compress = clzma.flush()
    f.write(b"".join([tempcompress,compress]))
    print("Done.")
    raise SystemExit

def compressfile(file_to_compress, file_name):
    clzma = lzma.LZMACompressor(format=lzma.FORMAT_RAW,filters=filterstouse)
    f = open(file_name, "ab")
    f.write(bytes(write_string_identifier, "ASCII"))
    f2 = open(file_to_compress, "rb")
    print("Now compressing. Please wait")
    tempcompress = clzma.compress(f2.read())
    compress = clzma.flush()
    f.write(b"".join([tempcompress,compress]))
    print("Done.")
    raise SystemExit

def decompressfile(file_to_decompress, file_to_decompress_to):
    dlzma = lzma.LZMADecompressor(format=lzma.FORMAT_RAW,filters=filterstouse)
    f = open(file_to_decompress, "rb")
    initread = f.read()
    newfile = initread.split(bytes("   ", "utf-8"))
    if not newfile[0] == bytes(string_identifier, "ASCII"):
        print("File is not a supported ZZip file!")
        raise SystemExit
    f2 = open(file_to_decompress_to, "ab")
    print("Now Decompressing. Please wait")
    f2.write(dlzma.decompress(newfile[1]))
    print("Done.")
    raise SystemExit
def decompresszzipfolder(file3):
    dlzma = lzma.LZMADecompressor(format=lzma.FORMAT_RAW,filters=filterstouse)
    f = open(file3, "rb")
    initread = f.read()
    newfile = initread.split(bytes("   ", "utf-8"))
    if not newfile[0] == bytes(string_identifier_dir, "ASCII"):
        print("File is not a supported ZZip file!")
        raise SystemExit
    print("Now Decompressing. Please wait")
    tar_bytes = dlzma.decompress(newfile[1])
    print("Done. DO NOT CLOSE ZZIP EXTRACTOR JUST YET! There are still some things to do.")
    tar_io = io.BytesIO(tar_bytes)
    memtarfile = tarfile.TarFile(fileobj=tar_io, mode="r")
    print("Extracting. Please Wait")
    memtarfile.extractall()
    raise SystemExit

def finddecompress():
    f = open(sys.argv[2], "rb")
    oneread = f.read()
    tworead = oneread.split(bytes("   ", "utf-8"))
    if tworead[0] == bytes(string_identifier, "ASCII"):
        if probsdirectunzzip == True:
            print("Not enough Parameters")
        else:
            decompressfile(sys.argv[2], sys.argv[3])
    elif tworead[0] == bytes(string_identifier_dir, "ASCII"):
        print("File is a Directory File; Decompressing into directory")
        decompresszzipfolder(sys.argv[2])
print("ZZip Extracter Version", version)

if len(sys.argv) == 3:
    if sys.argv[1] == "-d":
        finddecompress()
    else:
        print("Not enough Parameters")
elif len(sys.argv) < 4:
    print("Usage:")
    print("ZZip[FUNCTION] [FILE1] [FOLDER/FILE]")
    print("FUNCTION ----------------- -d Decompression / -c Compression")
    print("FILE1 ------------- File to be Decompressed / File to be created")
    print("FOLDER/FILE ------  Destination File|No effect on Directory ZZips / File|Folder to be compressed")
    raise SystemExit
else:
    if sys.argv[1] == "-c" and os.path.isdir(sys.argv[3]):
        print("Compressing Directory.")
        compressfolder(sys.argv[3], sys.argv[2])
    elif sys.argv[1] == "-c":
        compressfile(sys.argv[3], sys.argv[2])
    elif sys.argv[1] == "-d":
        finddecompress(sys.argv[2], sys.argv[3])
    else:
        print("Function is not an implemented function")
