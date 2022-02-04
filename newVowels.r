
library(dplyr)
library(broom)
library(ggplot2)
library(AICcmodavg)
library(ggstatsplot)
library(httpgd)



formant.data <- read.csv("/Users/sarah/Git/eesti_regilaul_corpus/formants/formants.csv", header = TRUE, colClasses = c("factor","factor","factor","factor","factor","numeric","numeric","numeric","factor")) # nolint
summary(formant.data)



ictus_vowels <- filter(formant.data, position == "ictus")
off_vowels <- filter(formant.data, position == "off")



means_ick <- ictus_vowels %>%
  group_by(segment_id) %>%
  summarise(F1 = mean(F1),
            F2 = mean(F2)) %>%
print(n = 11)

means_off <- off_vowels %>%
  group_by(segment_id) %>%
  summarise(F1 = mean(F1),
            F2 = mean(F2)) %>%
print(n = 11)

ggplot(ictus_vowels, aes(x = F2, y = F1, color = segment_id, label = segment_id)) + # nolint
geom_point() +
geom_label(data = means_ick) +
scale_x_reverse() + scale_y_reverse() +
  guides(color = "none") +
theme_classic()


ggplot(off_vowels, aes(x = F2, y = F1, color = segment_id, label = segment_id)) + # nolint
geom_point() +
geom_label(data = means_off) +
scale_x_reverse() + scale_y_reverse() +
  guides(color = "none") +
theme_classic()

first_vowels <- filter(formant.data, syllable == "1")
second_vowels <- filter(formant.data, syllable == "2")


means_stress <- first_vowels %>%
  group_by(segment_id) %>%
  summarise(F1 = mean(F1),
            F2 = mean(F2)) %>%
print(n = 11)

means_weak <- second_vowels %>%
  group_by(segment_id) %>%
  summarise(F1 = mean(F1),
            F2 = mean(F2)) %>%
print(n = 11)

ggplot(first_vowels, aes(x = F2, y = F1, color = segment_id, label = segment_id)) + # nolint
geom_point() +
geom_label(data = means_stress) +
scale_x_reverse() + scale_y_reverse() +
  guides(color = "none") +
theme_classic()

ggplot(second_vowels, aes(x = F2, y = F1, color = segment_id, label = segment_id)) + # nolint
geom_point() +
geom_label(data = means_weak) +
scale_x_reverse() + scale_y_reverse() +
  guides(color = "none") +
theme_classic()

