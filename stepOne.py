import os
from os.path import join
from praatio import textgrid
from praatio import audio
inputPath = join('..',"eesti_regilaul_corpus")
outputPath = join(inputPath, "generated_textgrids")

#open audio files and create blank texgrids: 
#one point tier with beat
#ictus interval tier? melody?
#one interval tier with utterance

#open textgrids, add one point for each beat to beatTier
#add one interval to utteranceTier for every phrase (eight beats) 

#open PRAAT, select each interval, run Estonian forced aligner


