import os
import glob

# detect the file names in directory
files_lst = glob.glob("*")

# for storing the different file extensions
extn_set = set()
for file in files_lst:
    extn = file.split(sep=".") # later using to create a directory according to extension
    try:
        extn_set.add(extn[1])
    except IndexError:
        continue

# # some groups of the set
#     # video file extensions
# video = set(['webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'drc', 'gif', 'givf', 'mng', 'avi', 'mts', 'm2ts', 'ts', 'mov', 'qt', 'wmv', 'yuv', 'rm', 'rmvb', 'viv', 'asf', 'amv', 'mp4', 'm4p', 'm4v', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'm2v', 'svi', '3gp', '3g2', 'mxf', 'roq', 'nsv', 'flv', 'f4v', 'f4p', 'f4a', 'f4b'])

#     # music file extensions
# music = set(['3gp', 'aa', 'aac', 'aax', 'act', 'aiff', 'alac', 'amr', 'ape', 'au', 'awb', 'dct', 'dss', 'dvf', 'flac', 'gsm', 'iklax', 'ivs', 'mmf', 'mp3', 'mpc', 'sv', 'ogg', 'oga', 'mogg', 'opus', 'ra', 'rm', 'raw', 'rf64', 'sln', 'tta', 'voc', 'vox', 'wav', 'wma', 'wv', 'webm', '8svx', 'cda', 'm4a', 'mpb', 'm4p'])

#     # compressed file extensions
# cpressed = set(['arc', 'arj', 'as', 'b64', 'btoa', 'bz', 'cab', 'cpt', 'gz', 'hqx', 'iso', 'lha', 'lzh', 'mim', 'mme', 'pak', 'pf', 'rar', 'rpm', 'sea', 'sit', 'sitx', 'tbz', 'tbz2', 'tgz', 'uu', 'uue', 'z', 'zip', 'zipx', 'zoo'])

#     # audio-video file extensions
# av = video.intersection(music)

# # list of removing extensions
# remove_extn = set(['py','axd','asx','asmx','ashx','aspx','dll','xml','asp','css','cfm','yaws','swf','html','htm','xhtml','jhtml','jsp','jspx','wss','do','action','js','r','rmd'])

# # finally removing the extensions from the extn_set
# f_extn_set = extn_set.difference(remove_extn)

# create directory function for extensions which is stored in extension_set
def create_dir():
    for dir in f_extn_set:
        try:
            os.makedirs(dir+"_files")
        except FileExistsError:
            continue

# arranger function to move files into their respective directory
def arranger():
    for file in files_lst:
        fextension = file.split(sep=".")
        try:
            os.rename(file, fextension[1]+"_files/"+file)
        except (OSError, IndexError):
            continue

# calling order
create_dir()
arranger()