# Polynomial Regression
rm(list=ls())
graphics.off()
# Importing the dataset
dataset = read_csv("C:/Users/anton/OneDrive/Escritorio/Óptica/elipse_optica.csv")

# Fitting Polynomial Regression to the dataset
dataset$y2 = dataset$y^2
dataset$y3 = dataset$y^3
dataset$y4 = dataset$y^4

poly_reg = lm(formula = x ~ .,
              data = dataset)
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$x, y = dataset$y),
             colour = 'red') +
  geom_point(aes(x = predict(poly_reg, newdata = dataset), y = dataset$y),
            colour = 'blue') +
  ggtitle('Dada y, x es') +
  xlab('Coord x') +
  ylab('Coord y')


y_grid = seq(min(dataset$y), max(dataset$y), 0.1)
ggplot() +
  geom_point(aes(x = dataset$x, y = dataset$y),
             colour = 'red') +
  geom_point(aes(x = predict(poly_reg,
                            newdata = data.frame(y = y_grid,
                                                 y2 = y_grid^2,
                                                 y3 = y_grid^3,
                                                 y4 = y_grid^4)), y = y_grid), colour = 'blue') +
  ggtitle('Dada y, x es') +
  xlab('coord x') +
  ylab('coord y')
