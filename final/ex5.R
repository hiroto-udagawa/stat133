# --------------------------------------------------------------
# EXERCISE 5
# --------------------------------------------------------------


#  Implement below the constructor of a class called 'dfDiagnosis' whose aim 
#  is to facilitate the cleaning of numeric data frames.
#  In particular, this class should help spot outlier values in columns,
#  as well as rows and columns having a proportion of NA 
#  value higher than certain specified thresholds.
#  
#  The class constructor below takes a numeric data frame (numeric data frame = the
#  data frame columns are numeric vectors) as its 'data' argument, as
#  well as two other arguments, 'naRow' and 'naCol', specifying
#  the proportions of NA values beyond which rows and columns, respectively,
#  are considered bad, and should be removed from the data frame. 
#  
#  The constructor returns a 'dfDiagnosis' object that has the 
#  following attributes:
#  
#  (1) an attribute named 'rawData' that contains the original data frame
#  
#  (2) an attribute named 'theesholds', which is a numeric vector whose
#  first element is 'naRow', and whose second element is 'naCol'
#  
#  (3) an attribute named 'badRows', which is a numeric vector 
#  containing the indices of the rows whose proportion 
#  of NA values is higher than the threshold specified by 'naRow'
#  
#  (4) an attribute named 'badCols', which is a numeric vector 
#  containing the indices of the columns whose NA value proportion 
#  is higher than 'naCol'
#  
#  (5) an attribute named 'outliers', which is a list of 
#  pairs of indices (i,j) (represented as numeric vectors with
#  two elements) indicating the matrix coordinates of potential outliers
#
#  (6) an attribute named 'cleanData' containing a clean data frame where
#  the rows and columns beyond threshold in data have been removed, along 
#  with the rows containing at least one outlier




dfDiagnosis  = function(data, naRow, naCol){

   # Write your code here!
	rawData = data.frame(data)
	thresholds = c(naRow, naCol)
	#figure out bad columns
	badCols = c()
	for(a in 1:(ncol(rawData))){
	if (sum(is.na(rawData[a]))/nrow(rawData)> naCol){badCols = c(badCols,a)
}
}	
	#figure out bad rows
	badRows = c()
	for(a in 1:(nrow(rawData))){
	if (sum(is.na(rawData[a,]))/ncol(rawData)> naRow){badRows = c(badRows,a)
}
}
	#figure out outliers
	summary = summary(rawData)
	outsum = c()
	for(a in 1:length(summary)){ 
	outsum = c(outsum, a[[3]]+(1.5*a[[5]]-a[[2]]))
	
	object = list(rawData = data.frame(data),
			thresholds = c(naRow, naCol),
			badCols = badCols,
			badRows=badRows,
			outliers = c(),
			cleanData= data.frame(data))
	class(object)='dfDiagnosis'

return(object)
}

# --------------------------------------------------------------
# TEST 5 
# --------------------------------------------------------------
source('test.R')

data = data.frame(X1=c(NA,NA,NA,100), 
		  X2=c(1,NA,1,100), 
		  X3=c(1,NA,1,100), 
		  X4=c(100,NA,0,1))

dfDiag = dfDiagnosis(data, naRow=0.5, naCol=0.6)


tryCatch(
         checkEquals(class(dfDiag), 'dfDiagnosis'),
	 error = function(err) errmsg(err)
)

tryCatch(
         checkEquals(length(dfDiag), 6),
	 error = function(err) errmsg(err)
)

tryCatch(
         checkEquals(dfDiag$rawData, data),
	 error = function(err) errmsg(err)
)


tryCatch(
         checkEquals(dfDiag$thresholds, c(0.5,0.6)),
	 error = function(err) errmsg(err)
)

tryCatch(
         checkEquals(dfDiag$badRows, 2),
	 error = function(err) errmsg(err)
)


tryCatch(
         checkEquals(dfDiag$badCols, 1),
	 error = function(err) errmsg(err)
)

tryCatch(
         checkEquals(dfDiag$outliers, list(c(1,4), c(4,2), c(4,3))),
	 error = function(err) errmsg(err)
)

tryCatch(
         checkEquals(dfDiag$cleanData, data.frame(X2=1, X3=1, X4=0)),
	 error = function(err) errmsg(err)
)
