## BAR PLOT ONLY

library(ggplot2)
library(reshape2)

results <- read.csv("~/results.csv")
df <- data.frame(method = results['method'], wrr = results['wrr'], wcr = results['wcr'])
data.m <- melt(df, id.vars='method')

ggplot(data.m) +
  geom_bar(aes(method,value,fill = variable), width = 0.4, position = position_dodge(width=0.5), stat="identity") +
  theme(legend.position="top", legend.title = element_blank()) +
  labs(x="Speech Recognition engine",y="Rate") +
  scale_fill_discrete(breaks=c("wrr", "wcr"),
                      labels=c("Word Recognition Rate", "Word Correct Rate")) +
  scale_x_discrete(labels=c("DeepSpeech", "Google", "Houndify", "Sphinx", "Wit"))

## ADDING POINT PLOT

library(ggplot2)
library(reshape2)

results <- read.csv("~/results.csv")
df_accuracy <- data.frame(method = results['method'], wrr = results['wrr'], wcr = results['wcr'])
df_timing <- data.frame(method = results['method'], time = results['time'])
data.accuracy <- melt(df_accuracy, id.vars='method')
data.timing <- melt(df_timing, id.vars='method')

ggplot() +
  geom_bar(data=data.accuracy, aes(method,value,fill = variable), width = 0.45, position = position_dodge(width=0.5), stat="identity") +
  theme(legend.position="top", legend.title = element_blank()) +
  labs(x="Speech Recognition engine",y="Rate",sec.axis="Time (s)") +
  scale_fill_discrete(breaks=c("wrr", "wcr"),
                      labels=c("Word Recognition Rate", "Word Correct Rate")) +
  scale_x_discrete(labels=c("DeepSpeech", "Google", "Houndify", "Sphinx", "Wit")) +
  geom_point(data=data.timing,aes(method,value /5), size = 2) +
  scale_y_continuous(labels = function(x) paste0(x*100, "%"),
                     sec.axis = sec_axis(trans= ~.*5, name = "Inference time / phrase (s)"))
