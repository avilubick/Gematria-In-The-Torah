import pandas as pd
from googletrans import Translator
import unicodedata

translator = Translator()


def remove_nekudot(word):
    return ''.join(c for c in word if not unicodedata.combining(c))

gimdict = {"א":1,"ב":2,"ג":3,"ד":4,"ה":5,"ו":6,"ז":7,"ח":8,"ט":9,"י":10,"ך":20,"כ":20,"ל":30,"ם":40,"מ":40,"ן":50,"נ":50,"ס":60,"ע":70,"ף":80,"פ":80,"ץ":90,"צ":90,"ק":100,"ר":200,"ש":300,"ת":400}
while True:
    x = input("what word?: ")
    x = translator.translate(x, dest="he", src="en")
    x = x.text
    print(x)
    x = x.replace(" ", "").replace(".","").replace(".","")
    x = remove_nekudot(x)
    gimin = 0
    for i in x:
        gimin += gimdict[i]
    df = pd.read_csv("data.csv")

    for val5, i in enumerate(df.head(0).columns):
        if int(i) == gimin:
            hello = len(df[str(val5)])
            for h in range(hello):
                if type(df.iloc[h,val5]) == type("") and h !=0:
                    print(df.iloc[h, val5])
            break
