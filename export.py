#Python 3

import re,os,json,glob

workdir = '/home/toban/documents/code/project/json-md-exporter'
laverndir = 'Laverna-tw'
dirnotebooks = 'notebooks'
dirnotes = 'notes'
outdir = 'md-output'

def main():
    try:
        os.mkdir(os.path.join(workdir,outdir))
    except FileExistsError:
        print('Output directory already exists.')

    for notebookjson in glob.iglob(os.path.join(workdir,laverndir,dirnotebooks,'*.json')):
        #import json file as dict
        with open(notebookjson,'r') as filestr:
            notebookdict = json.load(filestr)

        #create dir for notebook
        nbdirname = clean_dirname(notebookdict['name'].lower())
        outpath = os.path.join(workdir,outdir,nbdirname)
        try:
            os.mkdir(outpath)
        except FileExistsError:
            print('Notebook output directory already exists.')

        #process each notebook to own dir

        for notejson in glob.iglob(os.path.join(workdir,laverndir,dirnotes,'*.json')):
            with open(notejson,'r') as notestr:
                notedict = json.load(notestr)

            #if note belongs to notebook
            if notedict['notebookId'] == notebookdict['id']:
                notename = clean_filename(notedict['title'].lower(), 'md')
                notepath = os.path.join(outpath,notename)
                
                #create file, add header and content
                with open(notepath,'w') as notemd:
                    notemd.write('##{}\n\n{}'.format(notedict['title'],notedict['content']))

    print('Done!')

#filename utility functions
def clean_filename(namestr,ext):
    cleaned = strip_ends(namestr)
    cleaned = sep_to_dash(cleaned)
    cleaned = strip_special(cleaned)
    return cleaned + '.' + ext

def clean_dirname(namestr):
    cleaned = strip_ends(namestr)
    cleaned = sep_to_dash(cleaned)
    cleaned = strip_special(cleaned)
    return cleaned

def strip_ends(namestr):
    return re.sub('^\W+|\W+$','',namestr)

def sep_to_dash(namestr):
    #convert separator characters to dashes
    outstr = re.sub('[\s/\|;:,\.\+&]','-',namestr)
    return re.sub('-+','-',outstr) #compress multi-dash

def strip_special(namestr):
    #remove special characters
    return re.sub('[^a-zA-Z0-9-_]','',namestr)

#execute only if run as script
if __name__ == "__main__":
    main()
