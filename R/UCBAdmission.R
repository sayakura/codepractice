UCBAdmissions
str(UCBAdmissions)
plot(UCBAdmissions)
margin.table(UCBAdmissions,1)
margin.table(UCBAdmissions,3)

admit.dept <- margin.table(UCBAdmissions, 3)
str(admit.dept)
barplot(admit.dept)
View(UCBAdmissions)
prop.table(admit.dept)
round(prop.table(admit.dept),2)

admit1 <- as.data.frame.table(UCBAdmissions)
admit2 <- lapply(admit1, function(x)rep(x, admit1$Freq))
admit3 <- as.data.frame(admit2)
admit4 <- admit3[,-4]
??UCBAdmissions
head(admit4)

rm(list = ls())

