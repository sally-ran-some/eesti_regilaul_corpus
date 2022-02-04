

import os
from os.path import join
from praatio import textgrid
from praatio.data_classes import textgrid_tier
from praatio.utilities.constants import Interval

def pullTiers(input, output,tierName):
    for fn in os.listdir(input):
        if ".TextGrid" not in fn:
            continue
        tg = textgrid.openTextgrid(join(input,fn), False)
        wantTier = tg.tierDict[tierName]
        tgSolo = textgrid.Textgrid()
        tgSolo.addTier(wantTier)
        tgSolo.save(join(output,tierName+fn),"long_textgrid",True)
        
        
inputTG = "/Users/sarah/Git/eesti_regilaul_corpus/grids/outOut"
outPutTiers = "/Users/sarah/Git/eesti_regilaul_corpus/grids/separateTiers"


pullTiers(inputTG,outPutTiers,"secIck")
pullTiers(inputTG,outPutTiers,"firstOff")
pullTiers(inputTG,outPutTiers,"secOff")

