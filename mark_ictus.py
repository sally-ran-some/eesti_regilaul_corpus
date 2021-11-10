import os
from os.path import join
import math
from praatio import textgrid
from praatio import praat_scripts
from praatio import audio

from praatio.utilities import utils
inputPath = "/Users/sarah/Git/eesti_regilaul_corpus/audio/055-24b_1.wav"
outputPath = "/Users/sarah/Git/eesti_regilaul_corpus/audio/generated_textgrids/"
praatEXE = os.system("/Applications/Praat.app/Contents/MacOS/Praat")
SILENCE_LABEL = "off"
SOUND_LABEL = "ictus"


def markIctus(praatEXE, inputPath, outputPath):
    for fn in os.listdir(inputPath):
        if ".wav" not in fn:
            continue
        name = os.path.splitext(fn)[0]
        tgFn = name + ".TextGrid"
        praat_scripts.annotateSilences(praatEXE, join(inputPath,fn),join(outputPath, tgFn),100,0,-25,0.1,0.1,SILENCE_LABEL,SOUND_LABEL) 
#open audio files and create blank texgrids: 
#one point tier with beat
#ictus interval tier? melody?
#one interval tier with utterance

#open textgrids, add one point for each beat to beatTier
#add one interval to utteranceTier for every phrase (eight beats) 

#open PRAAT, select each interval, run Estonian forced aligner


