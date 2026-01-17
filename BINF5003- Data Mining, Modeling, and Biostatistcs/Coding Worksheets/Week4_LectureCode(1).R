library(ggplot2)
head(mtcars)
head(iris)

ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl))) + 
  geom_point(size=3)+
  geom_smooth(method="lm", se =FALSE)+
  labs(title="",
       x="Weight",
       y="Miles per gallon",
       color = "Cylinder")

ggplot(iris, aes(x = Sepal.Length, fill = Species)) +
  geom_histogram(binwidth=0.3, color="black", alpha=0.7) +
  labs(title="Distribution of Sepal Length",
       x="Sepal Length", y="Count")

ggplot(iris, aes(x = Species, y = Sepal.Length, fill = Species)) +
  geom_boxplot() +
  geom_jitter (width=0.1, alpha = 0.6, color = "black")
  labs(title="Sepal Length by Species",
       x="Species", y="Sepal Length") +
  theme_classic()


