# Density plot for one variable
png("density_comply.png", height = 600, width = 800)
plot(density(w$comply), lty = 1, lwd = 7,
     col = "darkgrey", main = "Density for COMPLY1 (positives only)")
dev.off()
png("density_supercomply.png", height = 600, width = 800)
plot(density(w$supercomply), lty = 1, lwd = 7,
     col = "red", main = "Density for COMPLY2 (positives - negatives)")
dev.off()


# Density plot for a few variables
png("density_indices.png", height = 600, width = 800)
plot(density(w$defy), lty = 1, lwd = 7, ylim = c(0, 5),
     col = "blue", main = "Density for Style Indices")
lines(density(w$supercomply), lty = 1, lwd = 7, col = "red")
lines(density(na.omit(w$impress)), lty = 1, lwd = 7, col = "black")
legend("topright", legend=c("DEFY", "IMPRESS", "COMPLY"),
       col=c("blue", "black", "red"), lty=1, lwd = 9, cex = 1.2)
dev.off()


# Correlation plots with significance
# Read code that allows making corrplots with significance
require(corrplot)
cor.mtest <- function(mat, conf.level = 0.95) {
  mat <- as.matrix(mat)
  n <- ncol(mat)
  p.mat <- lowCI.mat <- uppCI.mat <- matrix(NA, n, n)
  diag(p.mat) <- 0
  diag(lowCI.mat) <- diag(uppCI.mat) <- 1
  for (i in 1:(n - 1)) {
    for (j in (i + 1):n) {
      tmp <- cor.test(mat[, i], mat[, j], conf.level = conf.level)
      p.mat[i, j] <- p.mat[j, i] <- tmp$p.value
      lowCI.mat[i, j] <- lowCI.mat[j, i] <- tmp$conf.int[1]
      uppCI.mat[i, j] <- uppCI.mat[j, i] <- tmp$conf.int[2]
    }
  }
  return(list(p.mat, lowCI.mat, uppCI.mat))
}


# Prepare the refined version of data for correlations
ref <- w[c(57, 56, 55, 10, 13, 12, 15, 20, 23, 29, 41, 43)]
colnames(ref) <- c("DEFY", "IMPRESS","COMPLY","ess.rate","sex",
                   "citizen","par.inc","ACT","SAT","GPA","birthyear","CDI")


# Plot correlations
corvariables <- ref                     # define the variables
corvariables <- na.omit(corvariables)
M <- cor(corvariables)                # calculate correlation matrix
res1 <- cor.mtest(corvariables, 0.95)
res2 <- cor.mtest(corvariables, 0.99)
# ADAPT #################################################
plotname = "corr_indices.png"
png(plotname, height=500, width=500)
corrplot(M, p.mat = res1[[1]], sig.level = 0.05, type = "upper")
dev.off()


# Boxplots with ggplot2
require(ggplot2)
ggplot(w, aes(x=meanGPA, y=impress)) +
  geom_scatterplot(notch=TRUE) +
  #geom_dotplot(binwidth=.1, dotsize=.8, stackdir="center", binaxis="y", position="dodge", binpositions="all")+
  #stat_summary(fun.y=mean, colour="red", shape=18, geom="point", position=position_dodge(width=0.75), size=4) +
  ggtitle("w") +
  xlab("GPA") +
  ylab("IMPRESS score")


png("scatter_GPA.png", width = 800, height = 350)
ggplot(w, aes(x=meanGPA, y=impress)) +
  geom_point(shape=1) +    # Use hollow circles
  geom_smooth(method=lm) +
  ggtitle("IMPRESS by MeanGPA") +
  xlab("meanGPA") +
  ylab("IMPRESS score")
dev.off()


png("scatter_SAT.png", width = 800, height = 350)
ggplot(w, aes(x=meanGPA, y=impress)) +
  geom_point(shape=1) +    # Use hollow circles
  geom_smooth(method=lm) +
  ggtitle("IMPRESS by SAT-total") +
  xlab("SAT") +
  ylab("IMPRESS score")
dev.off()


xtabs(~impress + teaisd, data = w) -> isd
summary(isd)
