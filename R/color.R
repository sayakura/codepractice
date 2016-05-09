list1 = c(13,14,43,78,76,68,67,80)

barplot(list1)
barplot(list1, col = colors()[102])
#rgb color
barplot(list1, col = rgb(100,123,45, max=255))
barplot(list1, col = c("red","blue","green","yellow","white"))
palette()
barplot(list1, col = cm.colors(5))
install.packages("RColorBrewer")
require("RColorBrewer")
display.brewer.all()

barplot(list1, col = brewer.pal(57, "Blues"))
barplot(list1, horiz = TRUE, las = 1, border = NA, main = "Kura's Chart", xlab = "DUMA", col = brewer.pal(9, "Blues"))
rm(list = ls())

