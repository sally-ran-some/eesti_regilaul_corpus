
import os
import phonpy
from os.path import join
import csv
from phonpy.phonpy import plot_vowels
from matplotlib import pyplot as plt

def makeCharts(input):
    for fn in os.listdir(input):
        if ".txt" not in fn:
            continue
        name = os.path.splitext(fn)[0] + ".png"
        f1 = []
        f2 = []
        vowel = []
        with open(join(input,fn),"r", encoding="utf-16",newline="")as tsv_file:
            tsv_reader = csv.DictReader(tsv_file,delimiter="\t")
            for row in tsv_reader:
                f1.append(row["F1 (Hz)"])
                f2.append(row["F2 (Hz)"])
                tmpVow = row["Segment label"]
                splIndex = tmpVow.find("-")
                endEx = len(tmpVow)
                tmpVow = tmpVow[splIndex+1:endEx]
                vowel.append(tmpVow + "\n")
        plot_vowels(f1,f2,vowel,standard=False)
        plt.savefig(name)
        plt.show()
        


input = "/Users/sarah/Git/eesti_regilaul_corpus/formants"
makeCharts(input)
# phonpy.plot_vowels(f1,f2,standard=True)



