import os
import json

f_list  = os.listdir("data")
print(f_list)
out = {}
regiony_gorskie = {
    "Pieniny": "Pieniny",
    "Magura Spiska": "Pieniny",
    "Gorce": "Gorce",
    "Beskid Sądecki": "Beskid Sądecki",
    "Kotlina Sądecka": "Beskid Sądecki",
    "Pogórze Popradzkie": "Beskid Sądecki",
    "Beskid Wyspowy": "Beskid Wyspowy",
    "Bieszczady": "Bieszczady",
    "Góry Sanocko-Turczańskie": "Bieszczady",
    "Pogórze Przemyskie": "Bieszczady",
    "Pogórze Bukowskie": "Bieszczady",
    "Beskid Niski": "Beskid Niski",
    "Obniżenie Gorlickie": "Beskid Niski",
    "Pogórze Jasielskie": "Beskid Niski",
    "Kotlina Jasielsko-Krośnieńska": "Beskid Niski",
    "Góry Świętokrzyskie": "Góry Świętokrzyskie",
    "Wyżyna Sandomierska": "Góry Świętokrzyskie",
    "Niecka Połaniecka": "Góry Świętokrzyskie",
    "Pogórze Szydłowskie": "Góry Świętokrzyskie",
    "Słowacki Raj": "Słowacki Raj",
    "Tatry":"Tatry"
}

for f in f_list:
    with open(f"data/{f}", encoding="utf8") as fd:
        #print(fd)
       # print(f)

        tmp = json.loads(fd.read())

        nodes = tmp.get("nodes")
        #print(nodes)

        for k in nodes.keys():
            #print(k)
            subregion = nodes[k].get("region")
            region = regiony_gorskie.get(subregion, "UNKNOWN")
            elm = {k:nodes[k]}
         #   print(region)
            if region in out.keys():
                #print(out[region])
                if subregion in out[region].keys():
                     out[region][subregion].append(elm)
                else:
                    out[region][subregion] = [elm]
            else:
                out[region] = {subregion:[elm]}
                
#print(out)

with open('output.json', 'w', encoding='utf-8') as plik:
    json.dump(out, plik, ensure_ascii=False, indent=4)


print(out.keys())
print("yaaay")








