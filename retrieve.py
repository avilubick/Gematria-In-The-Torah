import requests
import pandas as pd


books = ["Genesis",50,"Exodus",40,"Leviticus",27,"Numbers",36,"Deuteronomy",34]
headers = {"accept": "application/json"}
gimdict = {"א":1,"ב":2,"ג":3,"ד":4,"ה":5,"ו":6,"ז":7,"ח":8,"ט":9,"י":10,"ך":20,"כ":20,"ל":30,"ם":40,"מ":40,"ן":50,"נ":50,"ס":60,"ע":70,"ף":80,"פ":80,"ץ":90,"צ":90,"ק":100,"ר":200,"ש":300,"ת":400}
idk,wordgim = "",0
torahgim=[]
data = {}


for val,i in enumerate(books):
    if val % 2 == 0:
        for y in range(books[val+1]):
            url = f"https://www.sefaria.org/api/v3/texts/{books[val]}%20{y+1}?version=hebrew&return_format=text_only"
            response = requests.get(url, headers=headers)
            hebstr = response.text[2504:].split("]}]")[0].replace("־"," ").replace(",","").replace("׃","").replace("}","").replace("{","").replace('"',"").replace("]","").replace("[","").replace("׀ ","")
            for i in hebstr.split(" "):
                if len(i)>1:
                    for x in i:
                        if x in gimdict:
                            wordgim+=int(gimdict[x])
                            idk = f"{idk}{x}"
                    if wordgim not in torahgim:
                        torahgim.append(wordgim)
                        torahgim.append([idk])
                    else:
                        for val2, d in enumerate(torahgim):
                            if d == wordgim:
                                if idk not in torahgim[val2+1]:
                                    torahgim[val2+1].append(idk)
                    wordgim=0
                    idk = ""

for val4,x in enumerate(torahgim):
    if val4 % 2 == 0:
        data[str(x)]=torahgim[val4+1]

print("Data Retrieved")
longest = 0
for key, value in data.items():
    if len(value)>longest:
        longest = len(value)

for key, value in data.items():
    while len(value)<longest:
        data[key].append("")
int_list = [int(s) for s in data.keys()]
sorted_keys=sorted(int_list)
sorted_dict = {key:data[str(key)] for key in sorted_keys}

df = pd.DataFrame(sorted_dict)
print("Dataframe Created")

df.to_csv('data.csv', index=False)

print("Created File")
