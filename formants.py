
import numpy as np
import pandas as pd
#import plotnine
import matplotlib.pyplot as plt


input = "/Users/sarah/Git/eesti_regilaul_corpus/formants/formants.csv"


formants = pd.read_csv(input)

# fig = ggplot(, aes(x=F2,y=F1,color = segment, label = segment)) +
#   geom_point() +
#   geom_label(data = meansOff)+
#   scale_x_reverse() + scale_y_reverse() +
#   guides(color="none")+
#   theme_classic()
#formants["vowel"] = formants["segment"].astype("category")

#graph = formants.plot.scatter(x='F1 (Hz)',y='F2 (Hz)')

#print(formants)



