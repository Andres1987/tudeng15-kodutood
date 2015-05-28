pdf(file='E:/Google Drive/Doktrorantuur/Õppeained/Bioinformaatika/Too_10_hist.pdf')
hist(as.numeric(unlist(tudengid[2])), labels = TRUE ,main = "Vanuse jaotus", xlab = "Aastat vana", ylab = "Sagedus",ylim = range(0,550))
Pikkus <- tudengid[,17]
Kaal <- tudengid[,18]
x2 <- (150:200)
y2 <- 18.5*x2^2/10000
y3 <- 25*x2^2/10000
y4 <- 15*x2^2/10000
y5 <- 40*x2^2/10000
plot(Pikkus,Kaal, col = grey(0,alpha =0.4), pch = 16, main = "Pikkus vs Kaal",ylim = range(40,130),xlab = "Pikkus (cm)", ylab = "Kaal (kg)")
lines(x2,y2,lwd = 2,)
lines(x2,y3,col="gray53", lwd = 2)
lines(x2,y4,col="red", lwd = 2)
lines(x2,y5,col="firebrick", lwd = 2)
legend('topright',c("KMI = 40","KMI = 25","KMI = 18.5","KMI = 15"),lty=1, lwd=2,col=c("firebrick","gray53","black","red"))

dev.off()
