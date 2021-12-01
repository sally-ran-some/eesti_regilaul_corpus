"""
An example using TextgridTier set operations.
The following example is derived from real code.
The original code.  Suppose you have two tiers and want to use one tier to
filter the results of another tier.  In my case, I had textgrids with
stressed syllable and stressed vowels marked.  I wanted to extract pitch
information using this tier.  But the pitch contour contained some pitch
doubling and halving--afflicted areas were marked on a separate tier.
By taking the difference between the two tiers, we get the relevant regions,
minus areas affected by pitch halving and doubling.
I've added union and intersection here just to show their effect.
"""

import os
from os.path import join

from praatio import textgrid
from praatio.data_classes import textgrid_tier
from praatio.utilities.constants import Interval

def splitIctus(fromFN,toFN):
    for fn in os.listdir(fromFN):
        if ".TextGrid" not in fn:
            continue
        tg = textgrid.openTextgrid(join(fromFN,fn), False)
        #grab ictus tier
        ictusTier = tg.tierDict["ictus"]
        #make new copy for "off"
        offTier = ictusTier.new("off")
        tmpOff = []
        for start, end, label in offTier.entryList:
            if label == "x":
                tmpOff.append(Interval(start,end,"off"))
        offTier.entryList = tmpOff
        tmpOn = []
        for start, end, label in ictusTier.entryList:
            if label == "ictus": 
                tmpOn.append(Interval(start,end,"ictus"))
        ictusTier.entryList = tmpOn
        tg.addTier(offTier)
        tg.save(join(toFN,fn),'long_textgrid',True)
        

def getIntersection(fromFN, toFN):
    for fn in os.listdir(fromFN):
        if ".TextGrid" not in fn:
            continue
        tg = textgrid.openTextgrid(join(fromFN,fn), False)
        syll1 = tg.tierDict["s1"]
        syll2 = tg.tierDict["s2"]
        ictusTier = tg.tierDict["ictus"]
        offTier = tg.tierDict["off"]
      
   # filterTier = tg.tierDict["manually_labeled_pitch_errors"]

    # Intersection
        firstIctus = ictusTier.intersection(syll1)
        firstIctus.name = "firstIck"
        secIctus =ictusTier.intersection(syll2)
        secIctus.name = "secIck"
        firstOff =offTier.intersection(syll1)
        firstOff.name = "firstOff"
        secOff =offTier.intersection(syll2)
        secOff.name = "secOff"

       
        tg.addTier(firstIctus)
        tg.addTier(secIctus)
        tg.addTier(firstOff)
        tg.addTier(secOff)
        tg.save(join(toFN, fn), 'long_textgrid',True)

    



fromFN = "/Users/sarah/Git/eesti_regilaul_corpus/grids"
toFN = "/Users/sarah/Git/eesti_regilaul_corpus/grids/output"
lastFN = "/Users/sarah/Git/eesti_regilaul_corpus/grids/outOut"

#splitIctus(fromFN,toFN)

getIntersection(toFN,lastFN)


   # phoneTier1 = ictusTier.intersection(filterTier)
    #phoneTier1.name = "vowel_intersection"
  #  syll11 = syll1.intersection(filterTier)
    #syll11.name = "syllable_intersection"
    #
   # tg.addTier(phoneTier1)
   # tg.addTier(syll11)

    # Difference
#     phoneTier2 = ictusTier.difference(filterTier)
#     phoneTier2.name = "vowel_difference"
#     syll12 = syll1.difference(filterTier)
#     syll12.name = "syllable_difference"

#     tg.addTier(phoneTier2)
#     tg.addTier(syll12)

#     # Union
#     phoneTier3 = ictusTier.union(filterTier)
#     phoneTier3.name = "vowel_union"
#     syll13 = syll1.union(filterTier)
#     syll13.name = "syllable_union"

#     tg.addTier(phoneTier3)
#     tg.addTier(syll13)

#     tg.save(toFN, "short_textgrid", True)


# path = join(".", "files")

# fromFN = join(path, "damon_set_test.TextGrid")
# toPath = join(path, "set_output")
# toFN = join(toPath, "damon_set_test.TextGrid")

# if not os.path.exists(toPath):
#     os.mkdir(toPath)

# doSetOperations(fromFN, toFN)