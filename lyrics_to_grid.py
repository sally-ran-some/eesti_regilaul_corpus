
import os
from os.path import join
from praatio import textgrid
from praatio import audio


#probably want to put this in main, call to variables
inputPath = join('..',"eesti_regilaul_corpus","texts")
outputPath = join(inputPath, "generated_textgrids")
for fn in os.listdir(inputPath):
    name, ext = os.path.splitext(fn)
    if ext != ".wav":
        continue


#will need to change direct name to filename variable
inputFN = join('..',"eesti_regilaul_corpus","audio","generated_textgrids","055-24b_1.TextGrid")
tg = textgrid.openTextgrid(inputFN, includeEmptyIntervals=False)
#wordsTier = textgrid.IntervalTier(name='words', entryList=[('0',tg.maxTimestamp,'words I need'),],
 #                                minT=0, maxT=tg.maxTimestamp)
# Ok, what were our tiers?
#print(tg.tierNameList)
#import txt file corresponding to audio file name, one line per phrase


# We've already seen how to add a new tier to a TextGrid
# Here we add a new tier, 'utterance', which has one entry that spans the length of the textgrid
utteranceTier = textgrid.IntervalTier(name='utterance', entryList=[('0', tg.maxTimestamp, 'mary rolled the barrel'), ],
                                  minT=0, maxT=tg.maxTimestamp)
tg.addTier(utteranceTier)
print(tg.tierNameList)
print(utteranceTier.entryList)


#read in txt file with corresponding file name
#split by line
#add one line to each interval


# The entryList, which holds the tier point or interval data, is the heart of the tier.
# Recall the 'new()' function, if you want to modify all of the entries in a tier at once

#newEntryList = [(start, stop, 'bloop') for start, stop, label in wordsTier.entryList]
#newWordTier = wordsTier.new(entryList=newEntryList)
#print(wordsTier.entryList)
#print(newWordTier.entryList)


