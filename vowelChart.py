
import os
from os.path import join
import csv
from phonpy.phonpy import plot_vowels
from matplotlib import pyplot
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# finally, generate the graph. We're making use of matplotlib's colour cycle by
# only issuing one plot command per vowel. That way we won't have to deal with
# indicating colours ourselves, making our code flexible so it can deal with any
# number of occurring vowels




        
def makeCharts(input):
    for fn in os.listdir(input):
        if ".txt" not in fn:
            continue
        name = os.path.splitext(fn)[0] + ".png"
        f1 = []
        f2 = []
        singleThreecorners = []
        doubleS = []
        with open(join(input,fn),"r", encoding="utf-16",newline="")as tsv_file:
            subset = "i"
            tsv_reader = csv.DictReader(tsv_file,delimiter="\t")
            for row in tsv_reader:
                tmpVow = row["segment"]
                if len(tmpVow) == 1:
                    if (tmpVow == "i") or (tmpVow == "a")
                        f1.append(row["F1 (Hz)"])
                        f2.append(row["F2 (Hz)"])
                        singleThreecorners.append(tmpVow)
               #TODO: sort formants to diphthongs and doubles
                #cuts off '--' 
                # splIndex = tmpVow.find("-")
                # endEx = len(tmpVow)
                # tmpVow = tmpVow[splIndex+1:endEx]
        plot_vowels(f1,f2,singleThreecorners,standard=True)
        plt.savefig(name + subset)
        plt.show()
        


    

input = "/Users/sarah/Git/eesti_regilaul_corpus/formants"
makeCharts(input)
#makeCharts(input)
# phonpy.plot_vowels(f1,f2,standard=True)



