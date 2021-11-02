#wavs need to be 24-bit to be read in without error
import os
from os.path import join
from praatio import textgrid
from praatio import audio

inputPath = join('..',"eesti_regilaul_corpus","audio")
outputPath = join(inputPath, "generated_textgrids")

if not os.path.exists(outputPath):
    os.mkdir(outputPath)

for fn in os.listdir(inputPath):
    name, ext = os.path.splitext(fn)
    if ext != ".wav":
        continue
    
    duration = audio.getDuration(join(inputPath, fn))
    wordTier = textgrid.IntervalTier('words', [], 0, duration)
    
    tg = textgrid.Textgrid()
    tg.addTier(wordTier)
    tg.save(join(outputPath, name + ".TextGrid"), format="short_textgrid", includeBlankSpaces=False)

# Did it work?
for fn in os.listdir(outputPath):
    ext = os.path.splitext(fn)[1]
    if ext != ".TextGrid":
        continue
    print(fn)