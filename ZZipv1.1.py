import lzma
import sys
version = 1.1
string_identifier = "ZZIP1.0   "
print("ZZip Version", version)
filterstouse = [
    {"id": lzma.FILTER_DELTA},
    {"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME},
]
if len(sys.argv) < 4:
    print("Usage:")
    print("python3 ZZip.py [FUNCTION] [FILE1] [FOLDER/FILE]")
    print("FUNCTION --- -d Decompression -c Compression")
    print("FILE1 ------ File to be Decompressed/File to be created")
    print("FOLDER/FILE ------  Destination Folder/File to be compressed")
    raise SystemExit
else:
    if sys.argv[1] == "-c":
        clzma = lzma.LZMACompressor(format=lzma.FORMAT_RAW,filters=filterstouse)
        f = open(sys.argv[2], "ab")
        f.write(bytes(string_identifier, "utf-8"))
        f2 = open(sys.argv[3], "rb")
        print("Now compressing. Please wait")
        tempcompress = clzma.compress(f2.read())
        compress = clzma.flush()
        result = b"".join([tempcompress,compress])
        f.write(result)
        print("Done.")
        raise SystemExit
    elif sys.argv[1] == "-d":
        dlzma = lzma.LZMADecompressor(format=lzma.FORMAT_RAW,filters=filterstouse)
        f = open(sys.argv[2], "rb")
        initread = f.read()
        newfile = initread.split(bytes("   ", "utf-8"))
        if not newfile[0] == bytes("ZZIP1.0", "ASCII"):
            print("File is not a ZZip file!")
            print(newfile)
            raise SystemExit
        f2 = open(sys.argv[3], "ab")
        print("Now Decompressing. Please wait")
        decompress = dlzma.decompress(newfile[1])
        f2.write(decompress)
        print("Done.")
        raise SystemExit
