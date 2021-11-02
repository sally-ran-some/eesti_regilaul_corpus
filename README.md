# eesti_regilaul_corpus
first, run step one. this will create textgrids with the following tiers:

a point tier of beats
an interval tier of phrases(eight beats)
an interval tier of ictus/off-ictus (???)
then the respective lyrics file will be read in and added to each interval
on the phrase tier

once this is done, it will open PRAAT and run the Estonian forced aligner on each phrase iteratively

STEP TWO IS MANUALLY CHECKING THE WORD AND SEGMENT TIER RESULTS OF THE FORCED ALIGNER. 

then go on to step three, which adds new interval tiers for
syllable position (1st or 2nd) for disyllabic words containing a single beat. this then outputs a .csv of the relevant vowels and their data points. 
