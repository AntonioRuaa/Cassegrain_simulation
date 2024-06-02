# Polynomial Regression
rm(list=ls())
graphics.off()
# Importing the dataset
library(tidyverse)
dataset = read_csv("C:/Users/anton/OneDrive/Escritorio/Óptica/elipse_optica3.csv")

# Fitting Polynomial Regression to the dataset
dataset$yi2 = dataset$yi^2
dataset$yi3 = dataset$yi^3
dataset$yi4 = dataset$yi^4

poly_reg = lm(formula = x ~ yi + yi2 + yi3 + yi4,
              data = dataset)
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$x, y = dataset$yi),
             colour = 'red') +
  geom_point(aes(x = predict(poly_reg, newdata = dataset), y = dataset$yi),
             colour = 'blue') +
  ggtitle('Dada y, x es') +
  xlab('Coord x') +
  ylab('Coord y del haz inicial')


yi_grid = seq(min(dataset$yi), max(dataset$yi), 0.1)
ggplot() +
  geom_point(aes(x = dataset$x, y = dataset$yi),
             colour = 'red') +
  geom_point(aes(x = predict(poly_reg,
                             newdata = data.frame(yi = yi_grid,
                                                  yi2 = yi_grid^2,
                                                  yi3 = yi_grid^3,
                                                  yi4 = yi_grid^4)), y = yi_grid), colour = 'blue') +
  ggtitle('Dada y, x es') +
  xlab('coord x') +
  ylab('coord y del haz inicial')