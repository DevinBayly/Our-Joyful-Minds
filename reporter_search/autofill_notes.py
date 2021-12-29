import yaml
res = yaml.load(open("notes.yml").read(),Loader=yaml.Loader)
for name in res["contacts"]:
    if res.get(name,-1) ==-1:
        res[name]=dict(notes=[],
        email=None,
        recipient_name=None,
        appeal_hook=None)

with open("notes.yml","w") as phile:
    phile.write(yaml.dump(res))

## things the class does
# expands new entries
# writes out templated versions of the article for each of the 