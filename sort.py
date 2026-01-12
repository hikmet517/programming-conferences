#!/usr/bin/env python3

import json
import os


with open("conferences.json") as fp:
    data = json.load(fp)

data.sort(key=lambda x: x["title"].lower())

with open("conferences.json", "w") as fp:
    json.dump(data, fp, indent=2, ensure_ascii=False)
    fp.write("\n")
