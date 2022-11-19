import yaml
import collections
import os

print("read mkdocs.yml")
flatList = []


def gen(a):
    for e in a:
        print(e)
        if isinstance(e,dict):
            print("its ein dict")
            for v in e.values():
                if isinstance(v,str):
                    print("****found: "+v)
                    flatList.append(v)
                else:
                    print("Ein weiteres Dict")
                    gen(v)

def copyMaster(file,folders):
    f = open("docs/master.md", "r")                
    content=f.read()
    f.close()
    content=content.replace("<!--bildungsgang-->", folders[1])
    content=content.replace("<!--Lernfeld-->", folders[2])
    content=content.replace("<!--nrLernsituiation-->", file[file.rfind("/")+1:-3])
    f2 = open(file, "x")
    f2.write(content)


with open("mkdocs.yml", "r") as stream:
    try:
        data =yaml.safe_load(stream) 
        nav=data["nav"]
        #print(nav)
        gen(nav)
        print(flatList)
        for filename in flatList:
            if os.path.exists("docs"+os.sep+filename):
                print("File "+filename+" exists!")
            else:
                print("File "+filename+" wird erzeugt!")
                dirs = "docs"+os.sep+filename[:filename.rfind("/")]
                try:
                    os.makedirs(dirs)
                    print("Erzeuge "+dirs)
                except FileExistsError:
                    print("Verzeichnis "+dirs+" existiert bereits")
                copyMaster("docs"+os.sep+filename,dirs.split("/"))

    except yaml.YAMLError as exc:
        print(exc)