
import os
from os.path import join
from praatio import textgrid
from praatio import praat_scripts
from praatio.utilities.constants import (
    Interval)


def markIctus(praatEXE, inputWavPath, rawTGPath):

    for fn in os.listdir(inputWavPath):
        if ".wav" not in fn:
            continue
        name = os.path.splitext(fn)[0]
        tgFn = name.strip("beat") + ".TextGrid"
        print(tgFn)
        praat_scripts.annotateSilences(
         praatEXE, join(inputWavPath, fn), join(rawTGPath, tgFn),100,0,-25,0.1,0.1,SILENCE_LABEL,SOUND_LABEL
        )

def addPhraseTier(rawTGPath, finalTGPath):
    for fn in os.listdir(rawTGPath):
        if ".TextGrid" not in fn:
            continue
        tg = textgrid.openTextgrid(join(rawTGPath, fn),True)
        phraseTier = textgrid.IntervalTier("syllable", entryList= [('0', tg.maxTimestamp,
        'test'),],minT=0,maxT=tg.maxTimestamp)
        tg.addTier(phraseTier)
        tg.save(join(finalTGPath,fn),'long_textgrid', True)
        
def addIntervalsLyrics(input):
    for fn in os.listdir(input):
        if ".TextGrid" not in fn: 
            continue
        name = os.path.splitext(fn)[0]
        song = name+".txt"
        tg = textgrid.openTextgrid(join(input, fn),True)
        tier2 = tg.tierDict["syllable"]
        lyrics = open(join(input,song),"r")
        lyricList = lyrics.readlines()
        dur = (tg.maxTimestamp/len(lyricList))
        start= 0.0
        length = start + dur
        line = 0
        while length <= tg.maxTimestamp:
            tmpInterval = Interval(start,length,lyricList[line])
            tier2.insertEntry(tmpInterval,'replace','warning')
            start = start+dur
            length = length +dur 
            line = line + 1
        #tier2.insertEntry(Interval(start,tg.maxTimestamp,lyricList[line]),'replace','warning')
        tg.save(join(input, fn),'long_textgrid',True)



        
   


praatEXE = "/Applications/Praat.app/Contents/MacOS/Praat"
root = "/Users/sarah/Git/eesti_regilaul_corpus/audio"
inputWavPath = join(root,"clicks")
rawTGPath = join(root, "ictus_tier")
finalTGPath = join(root,"lyric_tier")

SILENCE_LABEL = "x"
SOUND_LABEL = "ictus"

#autoSegmentSpeech(praatEXE, inputWavPath, rawTGPath)
#markIctus(praatEXE,inputWavPath,rawTGPath)
#addPhraseTier(rawTGPath, finalTGPath)
#addIntervalsLyrics(finalTGPath)
#getLyrics(rawTGPath)

inTG = "/Users/sarah/qp_final/txtgridtest/"
outTG = "/Users/sarah/qp_final/out/"
addPhraseTier(inTG,outTG)