 df <- read.table("Results.csv", header = FALSE, sep=",",strip.white = TRUE)
 df2 <- read.table("Stats_Project_2016.csv", header = TRUE, sep=",", quote = "",strip.white = TRUE)
 responseTimeAvgsY <- c()
 responseTimeAvgsN <- c()
 responseTimeTot <- c()
 accuracysY <- c()
 accuracysN <- c()
 accuracyTot <- c()
 heightTot <- c()
 physTot <- c()
 responseTot <- c()
for(i in 1:nrow(df)){
  correct <- 0
  incorrect <- 0
  activity <- df2[i %/% 4, "Did.you.take.the.Warm.up.activity."]
  activity <- as.character(activity)
  
  responseTimes <- c()
  if((i %% 4) == 2){
    heightTot <- append(heightTot, as.numeric(df2[(i %/% 4) + 1, "Height.in.cm"]))
    physTot <- append(physTot, as.numeric(df2[(i %/% 4) + 1, "Average.Physical.Activity.in.a.Day"]))
    
    for(j in 1:ncol(df)){
      loc = df[i,paste0("V", j)]
      if(!is.null(loc) & loc != "" & as.numeric(as.character(loc)) > 0.5){
         #print(loc, max.levels = 0)
        responseTimes <- append(responseTimes, as.numeric(as.character(loc)))
      }
    }
    #print(responseTimes)
    avg <- mean(responseTimes)
    #cat(avg)
    #cat(" ")
    #print(activity)
    responseTot <- append(responseTot, as.numeric(avg))
    if(identical(activity,"Yes")){
      responseTimeAvgsY <- append(responseTimeAvgsY, as.numeric(avg))
    } else {
      responseTimeAvgsN <- append(responseTimeAvgsN, as.numeric(avg))
    }
    
    #cat("\n")
  }else if( i %% 4 == 3){
    for(j in 1:ncol(df)){
      loc = df[i,paste0("V", j)]
      if(identical(as.character(loc), "correct")){
        correct = correct + 1
      }else if(identical(as.character(loc), "incorrect")){
        incorrect = incorrect + 1
      }
      
    }
    accuracy <- correct/(correct + incorrect)
    accuracyTot <- append(accuracyTot, accuracy)
    if(identical(activity, "Yes")){
        accuracysY <- append(accuracysY, as.numeric(accuracy))
    } else{
        accuracysN <- append(accuracysN, as.numeric(accuracy))
    }
    
    
  }     
  
}
 RTAvgYes <- mean(responseTimeAvgsY)
 RTAvgNo <- mean(responseTimeAvgsN)
 RTVarYes <- var(responseTimeAvgsY)
 RTVarNo <- var(responseTimeAvgsN)
 AcAvgYes <- mean(accuracysY)
 AcAvgNo <- mean(accuracysN)
 AcVarYes <- var(accuracysY)
 AcVarNo <- var(accuracysN)
 print(RTAvgYes)
 print(RTVarYes)
 print(AcAvgYes)
 print(AcVarYes)
 print(RTAvgNo)
 print(RTVarNo)
 print(AcAvgNo)
 print(AcVarNo)
 fname = "C:/Users/Connal/Documents/,EngSciYear2/STA286/plots.pdf"
 pdf(fname)
 hist(responseTimeAvgsN, breaks=7,col = rgb(1, 0, 0, 0.5), main = "Average Response Times", xlab = "Response Time")
 hist(responseTimeAvgsY, breaks=6, col = rgb(0, 0, 1, 0.5),add = T)
 legend(1.05, 0.5, c("No RT Practice Test", "RT Practice Test"),lty = c(1, 1), lwd=c(2.5,2.5),col=c("red", "blue"), bg = "white")
 hist(accuracysN,breaks=7, col = rgb(1, 0, 0, 0.5), main = "Accuracy", xlab = "Accuracy")
 hist(accuracysY, breaks=6,col = rgb(0, 0, 1, 0.5),add = T)
 legend(0.5, 3, c("No RT Practice Test", "RT Practice Test"),lty = c(1, 1), lwd=c(2.5,2.5),col=c("red", "blue"))
 par(mfrow = c(1, 2))
 boxplot(responseTimeAvgsN, col = rgb(1, 0, 0, 0.5), ylim = c(1, 2),main = "Response Time Without \n RT Practice Test [s]")
 boxplot(responseTimeAvgsY,col = rgb(0, 0, 1, 0.5), ylim = c(1, 2),main = "Response Time With \n RT Practice Test [s]")
 
 boxplot(accuracysN, col = rgb(1, 0, 0, 0.5), ylim = c(0, 1),main = "Accuracy Without \n RT Practice Test [s]")
 boxplot(accuracysY,col = rgb(0, 0, 1, 0.5), ylim = c(0, 1),main = "Accuracy Time With \n RT Practice Test [s]")
 par(mfrow = c(1, 1))
 plot(accuracysY, responseTimeAvgsY, main = "Response Time Vs. Accuracy for Participants \n Who Took the RT Practice Test Activity", xlab = "Accuracy", ylab = "Response Time [s]")
 abline(lm(responseTimeAvgsY ~ accuracysY))
 print(cor.test(accuracysY, responseTimeAvgsY))
 plot(accuracysN, responseTimeAvgsN, main = "Response Time Vs. Accuracy for Participants \n Who did not Take the RT Practice Test Activity", xlab = "Accuracy", ylab = "Response Time [s]")
 abline(lm(responseTot ~ accuracyTot))
 print(cor.test(accuracyTot, responseTot))
 
 plot(accuracyTot, responseTot, main = "Response Time Vs. Accuracy for all Participants", xlab = "Accuracy", ylab = "Response Time [s]")
 abline(lm(responseTimeAvgsN ~ accuracysN))
 print(cor.test(accuracysN, responseTimeAvgsN))
 
 plot(heightTot, accuracyTot, main = "Participant Height Vs. Accuracy", xlab = "Height [cm]", ylab = "Accuracy")
 abline(lm(accuracyTot ~ heightTot))
 print(cor.test(heightTot, accuracyTot))
 
 plot(physTot, accuracyTot, main = "Physical Activity Vs. Accuracy", xlab = "Average Daily Physical Activity [h]", ylab = "Accuracy")
 abline(lm(accuracyTot ~ physTot))
 print(cor.test(physTot, accuracyTot))
 
 plot(heightTot, responseTot, main = "Participant Height Vs. Response Time", xlab = "Height [cm]", ylab = "Response Time [s]")
 abline(lm(responseTot ~ heightTot))
 print(cor.test(heightTot, responseTot))
 
 plot(physTot, responseTot, main = "Physical Activity Vs. Response Time", xlab = "Average Daily Physical Activity [h]", ylab = "Response Time [s]")
 abline(lm(responseTot ~ physTot))
 print(cor.test(physTot, responseTot))
 
 par(mfrow = c(1, 2))
 qqnorm(rnorm(30, mean = mean(responseTot), sd = sqrt(var(responseTot))), main = "Standard Normal Q-Q Plot with \n Mean and Variance of \n Response Time")
 qqResp = qqnorm(responseTot, main = "Q-Q Plot of Response Time")
 print(cor.test(qqResp$x, qqResp$y))
 
 qqnorm(rnorm(30, mean = mean(accuracyTot), sd = sqrt(var(accuracyTot))), main = "Standard Normal Q-Q Plot with \n Mean and Variance of \n Accuracy")
 qqAcc = qqnorm(accuracyTot, main = "Q-Q Plot of Accuracy")
 print(cor.test(qqAcc$x, qqAcc$y))
 
 dev.off()
 print(t.test(responseTimeAvgsY, responseTimeAvgsN))
 print(t.test(accuracysY, accuracysN))