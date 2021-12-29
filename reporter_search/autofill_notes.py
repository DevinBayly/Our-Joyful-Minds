import yaml
res = yaml.load(open("notes.yml").read(),Loader=yaml.Loader)
for name in res["contacts"]:
    if res.get(name,-1) ==-1:
        res[name]=dict(notes=[],email=None)

with open("notes.yml","w") as phile:
    phile.write(yaml.dump(res))

