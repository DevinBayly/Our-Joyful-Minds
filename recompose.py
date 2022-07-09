import yaml

data = yaml.load(open("mkdocs.yml").read(),Loader=yaml.Loader)

data["nav"]

with open("all.md","w") as ophile:
    for item in data["nav"]:
        print(item.values())
        fname = list(item.values())[0]
        with open(f"docs//{fname}","r") as ifile:
            ophile.write(ifile.read())
