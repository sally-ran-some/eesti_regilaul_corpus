import os
from os.path import join
from praatio import textgrid
from praatio import praat_scripts
from praatio.data_classes import textgrid_tier
from praatio.data_classes.interval_tier import IntervalTier
from praatio.data_classes.textgrid_tier import TextgridTier
from praatio.utilities.constants import (
    Interval)
import pyphen

dic = pyphen.Pyphen(lang='et_EE')
def hyphen8(input,output):
    for fn in os.listdir(input):
        if ".txt" not in fn:
            continue
        lyrics = open(join(input,fn),"r")
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

input = '/Users/sarah/Git/eesti_regilaul_corpus/audio/lyric_tier'
output = '/Users/sarah/Git/eesti_regilaul_corpus/audio/lyric_tier/done'
hyphen8(input,output)   


# def doubleFort(input):
#     for fn in os.listdir(input):
#         if ".txt" not in fn:
#             continue
#         lyrics = open(join(input,fn),"r")
#         lyricList = lyrics.readlines()
#         lyrics.close()
#         line = 0
#         while line <  len(lyricList):
#             phrase = lyricList[line]
#             wordList = phrase.split()
#             count = 0     
#             while count < len(wordList):
#                 word = wordList[count]  
#                 word = word[0] + word[1:len(word)].replace("p","pp")
#                 word = word[0] + word[1:len(word)].replace("t","tt")
#                 word = word[0] + word[1:len(word)].replace("k","kk")
#                 wordList[count] = word
#                 count += 1
#             glue = " "
#             words = glue.join(wordList)
#             lyricList[line] = (words + "\n")
#             line += 1 
#         lyrics = open(join(input,fn),"w")
#         for element in lyricList:
#             lyrics.writelines(element)
#         lyrics.close()
    

# def replacePhrases(inputTG): 
#     for fn in os.listdir(inputTG):
#         if ".TextGrid" not in fn:
#             continue
#         name = os.path.splitext(fn)[0]
#         song = name+".txt"
#         tg = textgrid.openTextgrid(join(input,fn), True)
#         myEntries = tg.tierDict["phrase"].entryList
#         lyrics = open(join(input,song),"r")
#         lines = lyrics.readlines()
#         index = 0 
#         tmpEntryList = []
#         while index < len(lines):
#             entry = myEntries[index]
#             if entry.__getattribute__#
#             #get label, if not "x or blank"
#             tmpEntryList.append(Interval(entry.start,entry.end,lines[index]))
#             index += 1 
#         myEntries = tmpEntryList
#         newTier = textgrid.IntervalTier("phrase2", myEntries, 
#         tg.minTimestamp,tg.maxTimestamp)
#         tg.replaceTier("phrase", newTier, "warning")
#         tg.save(join(input,fn),'long_textgrid', True)

# def replaceWords(inputTG): 
#     for fn in os.listdir(inputTG):
#         if ".TextGrid" not in fn:
#             continue
#         name = os.path.splitext(fn)[0]
#         song = name+".txt"
#         tg = textgrid.openTextgrid(join(input,fn), True)
#         myEntries = tg.tierDict["phrase/word"].entryList
#         lyrics = open(join(input,song),"r")
#         lines = lyrics.readlines()
#         words = lines.split()
#         index = 0 
#         tmpEntryList = []
#         while index < len(lines):
#             index2 = 0
#             while index < len(words):
#                 entry = myEntries[index]
#                 tmpEntryList.append(Interval(entry.start,entry.end,lines[index]))
#                 index2 += 1
#             index += 1 
#         myEntries = tmpEntryList
#         newTier = textgrid.IntervalTier("words2", myEntries, 
#         tg.minTimestamp,tg.maxTimestamp)
#         tg.replaceTier("phrase/word", newTier, "warning")
#         tg.save(join(input,fn),'long_textgrid', True)
            

            




            
 



#     """ def combineDicts(lex, syll,root):
#     syllDict = []
#     with open(lex, encoding='utf-16') as f:
#         lexiList = f.readlines()

#     with open(syll,encoding='utf-16') as f:
#         syllilist = f.readlines()
#     index = 0
#     while index < 5:
#         syllDict.append(lexiList[index]+syllilist[index])
#         index += 1 
#     with open(root,'w') as f:
#         for element in syllDict:
#             f.write(element +"\n")
#     print(syllDict) """
    

# input = "/Users/sarah/Git/eesti_regilaul_corpus/audio/lyric_tier"

# #doubleFort(input)
# #replacePhrases(input)
# replaceWords(input)

