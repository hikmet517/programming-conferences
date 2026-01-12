#!/usr/bin/env python3

import json


PRE = "# Conferences\n\n" "A list of programming conferences.\n\n\n"
POST = (
    "# Other Collections\n\n"
    "- https://github.com/nighthawk017/conferences-with-online-videos\n"
    "- https://github.com/hellerve/programming-talks\n"
    "- https://github.com/jfrimmel/talks-and-sources\n"
)


with open("conferences.json") as fp:
    data = json.load(fp)


with open("README.md", "w") as fp_out:
    fp_out.write(PRE)
    for conf in data:
        if "title" not in conf or conf["title"] == "":
            continue
        fp_out.write(f'## {conf["title"]}\n\n')
        if "description" in conf:
            fp_out.write(f'{conf["description"]}\n\n')
        if "links" in conf:
            for link in conf["links"]:
                fp_out.write(f'- [{link["title"]}]({link["url"]})\n')
        if "tags" in conf:
            fp_out.write(
                "\nTags: " + ", ".join([f"`{t}`" for t in conf["tags"]]) + "\n"
            )
        fp_out.write("\n\n")
    fp_out.write(POST)
