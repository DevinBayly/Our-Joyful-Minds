import os
os.getcwd()
os.chdir("testing_mkdocs/docs")
text = open("book.md","r").read()

chunks = text.split("\n## ")
toc =[]
for c in chunks:
    lines = c.split("\n")
    chap_title = lines[0].strip().replace("#","").replace(":","--")
    fname = chap_title.replace(" ","_")
    # os.remove(fname+".md")
    with open(f"{fname}.md","w") as phile:
        full = '\n'.join(lines)
        phile.write(f"## {full}")
    toc.append(f"{chap_title} : {fname}.md")

with open("../mkdocs.yml","w") as philw:
    philw.write(""" 
site_name: Our Joyful Minds
theme: readthedocs
nav:
  - """)
    philw.write("\n  - ".join(toc))

