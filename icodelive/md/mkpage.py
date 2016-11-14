import os
import sys
import subprocess

# USAGE:
# python md/mkpage.py templates/home/index.html md/home/header_index.md md/home/index.md
# python manage.py runserver
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if len(sys.argv) >2:
    target = sys.argv[1]
    source = ' '.join(sys.argv[2:])
else:
    #target = "../templates/home/index.html"
    #source = "home/header_index.md home/index.md"
    raise("usage: mkpage target source")

#print(target, source)

cmd="pandoc -t html5 -o {target} {source}".format(target=target, source=source)

# print(cmd)
subprocess.call(cmd, shell=True)

f = open(target,"r")
targs = f.read()
f.close()

b = open(BASE_DIR+'/md/bottom.md', 'r')
t = open(BASE_DIR+'/md/top.md', 'r')
f = open(target, "w")
f.write(t.read())
f.write(targs)
f.write(b.read())

f.close()
b.close()
t.close()

