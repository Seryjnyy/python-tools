import os
import argparse

def convertFileName(filename, substrings, fileExtension):
    # split filename from extension to prevent modifying the extension
    new_filename, _ = filename.split("."+fileExtension)

    # go through substrings and replace them in the filename
    for subs in substrings:
        if subs in new_filename:
            new_filename = new_filename.replace(subs, "")

    return new_filename.strip() + "." + fileExtension

def filterFunc(fileName, fileExtension):
    # slice the filename from the back to get check the extension
    if fileName[-len(fileExtension):] == fileExtension:
        return True
    return False

def getFiles(fileExtension):
    fileNameList = os.listdir(".")

    # filter out files that are not 
    filtered = filter(lambda x : filterFunc(x, fileExtension), fileNameList)
    return list(filtered)



def convertSongs(fileExtension, substrings):
    filesToConvert = getFiles(fileExtension)

    for f in filesToConvert:
        os.rename(f, convertFileName(f, substrings, fileExtension))


def main():
    parser = argparse.ArgumentParser(
                    prog='FilenameSubstringRemover',
                    description='Add the program to the folder with the files. Pass in the extension (.mp3, .txt, etc.). Pass in the substrings.',
                    epilog='')

    parser.add_argument('-ext', '--extension', help="The file format of the files without the dot. (mp3, txt, etc.)", required=True)  
    parser.add_argument("substrings", nargs="*")  
    args = parser.parse_args()

    print(args.substrings, args.extension)
    
    # check if extension has an appended dot
    if args.extension[0] == ".":
        parser.error(f"{args.extension} should be {args.extension[1:]}")

    convertSongs(args.extension, args.extension )

if __name__ == "__main__":
    main()