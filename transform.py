import os
import json

f_list  = os.listdir("data")
print(f_list)
out = {}


for f in f_list:
    with open(f"data/{f}", encoding="utf8") as fd:
        #print(fd)
       # print(f)

        tmp = json.loads(fd.read())

        nodes = tmp.get("nodes")
        #print(nodes)

        for k in nodes.keys():
            #print(k)
            region = nodes[k].get("region")
            print(region)
            if region in out.keys():
                #print(out[region])
                out[region].append(nodes[k])
            else:
                out[region] = [nodes[k]]
#print(out)

with open('output.json', 'w', encoding='utf-8') as plik:
    json.dump(out, plik, ensure_ascii=False, indent=4)

print("yaaay")








