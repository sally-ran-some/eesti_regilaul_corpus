import os
from os.path import join
from praatio import textgrid
from praatio import praat_scripts
from praatio.data_classes import textgrid_tier
from praatio.data_classes.interval_tier import IntervalTier
from praatio.data_classes.textgrid_tier import TextgridTier
from praatio.utilities.constants import (Interval)
import pyphen

#sets up textgrids with tiers for ictus, phrases, syllabified phrases
#to prep for the forced-aligner
#you need: 
#   tempo map beats for each song
#   wav file of the song
#   txt file of the lyrics
#   

dic = pyphen.Pyphen(lang='et_EE')
def hyphen8(inputTG,output):
    for fn in os.listdir(inputTG):
        if ".txt" not in fn:
            continue
        lyrics = open(join(inputTG,fn),"r")
        lyricList = lyrics.readlines()
        lyrics.close()
        syllMommy = []
        for element in lyricList:
            line = element 
            wordList = line.split()
            syllBabies = []
            for element in wordList:
                word = element
                hyphen = dic.inserted(word)
                syllBabies.append(hyphen)
            glue = " "
            syllLine = glue.join(syllBabies)
            syllMommy.append(syllLine +'\n')
        f = open(join(output,fn),'w')
        for element in syllMommy:
            f.writelines(element)
        f.close()


        #print(syllMommy)

#for this you need tempo map wav files for each song
def markIctus(praatEXE, inputBeats, inputTG):
    for fn in os.listdir(inputBeats):
        if ".wav" not in fn:
            continue
        name = os.path.splitext(fn)[0]
        tgFn = name.strip("beat") + ".TextGrid"
        #print(tgFn)
        praat_scripts.annotateSilences(
            praatEXE, join(inputBeats, fn), join(inputTG, tgFn),100,0,-25,0.1,0.1,SILENCE_LABEL,SOUND_LABEL
        )

def addTier(inputTGTG, outputTG, tierName):
    for fn in os.listdir(inputTGTG):
        if ".TextGrid" not in fn:
            continue
        tg = textgrid.openTextgrid(join(inputTGTG, fn),True)
        newTier = textgrid.IntervalTier(tierName, entryList= [('0', tg.maxTimestamp,
        'test'),],minT=0,maxT=tg.maxTimestamp)
        tg.addTier(newTier)
        tg.save(join(outputTG,fn),'long_textgrid', True)

#makes one interval for every four beats 
#leaves refrain 
def addIntervalsfromIctusTier(inputTG,tierName):
    for fn in os.listdir(inputTG):
        if ".TextGrid" not in fn: 
            continue
        tg = textgrid.openTextgrid(join(inputTG, fn),True)
        tier1 = tg.tierDict["ictus"]
        tier2 = tg.tierDict[tierName]
        i = 0
        j = 8
        while j < len(tier1):
           
            newstart = tier1.entryList[i].start
            tmpIntervalDur = tier1.entryList[i].end 
            newEnd = tier1.entryList[j].end + tmpIntervalDur
            newLabel = " "
            tmpInterval = Interval(newstart,newEnd,newLabel)
            tmpPhraseTerval = Interval(newEnd+0.1, (tmpIntervalDur*8)," ")
            tier2.insertEntry(tmpInterval,'replace','warning')
            tier2.insertEntry(tmpPhraseTerval,'replace','warning')
            i = j + 1
            j += 9
        #tier2.insertEntry(Interval(start,tg.maxTimestamp,lyricList[line]),'replace','warning')
        tg.save(join(inputTG, fn),'long_textgrid',True)


def readLyricLines(inputTXT,inputTG,tierName):
    for fn in os.listdir(inputTG):
        if ".TextGrid" not in fn: 
            continue
        tg = textgrid.openTextgrid(join(inputTG, fn),True)
        tier = tg.tierDict[tierName]
        name = os.path.splitext(fn)[0]
        song = name+".txt"
        lyrics = open(join(inputTXT,song),"r")
        lyricList = lyrics.readlines()
        line = 0 
        while line < len(lyricList):
            newLabel = lyricList[line]
            tier.entryList[line].label = newLabel
            line += 1
        tg.save(fn,'long_textgrid',True)




inputTG = '/Users/sarah/Git/eesti_regilaul_corpus/audio/lyric_tier'
output = '/Users/sarah/Git/eesti_regilaul_corpus/audio/lyric_tier/done'
praatEXE = "/Applications/Praat.app/Contents/MacOS/Praat"
root = "/Users/sarah/Git/eesti_regilaul_corpus/audio"
inputTGWavPath = join(root,"clicks")
rawTGPath = join(root, "ictus_tier")
finalTGPath = join(root,"lyric_tier")
inputTXT = " "

SILENCE_LABEL = "x"
SOUND_LABEL = "ictus"
hyphen8(inputTG,output)   

#addTier1stsyll
#addTier2ndsyll
