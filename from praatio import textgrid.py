from praatio import textgrid

# Textgrids take no arguments--it gets all of its necessary attributes from the tiers that it contains.
tg = textgrid.Textgrid()

# IntervalTiers and PointTiers take four arguments: the tier name, a list of intervals or points,
# a starting time, and an ending time.
wordTier = textgrid.IntervalTier('words', [], 0, 1.0)
maxF0Tier = textgrid.PointTier('maxF0', [], 0, 1.0)

tg.addTier(wordTier)
tg.addTier(maxF0Tier)

tg.save("empty_textgrid.TextGrid", format="short_textgrid", includeBlankSpaces=False)