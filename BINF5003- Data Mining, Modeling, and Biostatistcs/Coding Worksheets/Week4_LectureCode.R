library("ggplot2")
setwd("C:/Users/Delwar/Desktop/Humber/BINF5003- Data Mining, Modeling, and Biostatistcs")
mtcars<-force(mtcars)
#Histogram
ggplot(mtcars, aes(x=mpg))+
  geom_histogram(binwidth = 2) + #try 1, 2, 3
  labs(title = "Histogram of Miles per Gallon (mtcars)",
       x = "MPG", y = "Count")
