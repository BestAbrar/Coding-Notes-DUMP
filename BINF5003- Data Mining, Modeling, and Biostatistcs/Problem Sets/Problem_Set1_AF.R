#Section 1: Vectors
# 1. Create a vector with the numbers: 5, 10, 15, 20, 25.
myVector<-c(5, 10, 15, 20, 25)
# o Access the 1st, 3rd, and 5th elements.
myVector[1] 
myVector[3] 
myVector[5] 
# o What happens if you try to access the 6th element?
myVector[6] #print 'NA' in console
# 2. Create a vector of the first 8 even numbers.
evenVec = (1:8)*2
# o Multiply all values by 3.
print(evenVec*3)
# o Add 5 to each element.
print(evenVec+5)
# 3. Create a vector of fruits: "apple", "orange", "grape", "pear".
fruits = c("apple", "orange", "grape", "pear")
# o Find which fruit has 5 letters.
which(nchar(fruits) >=5 )
# o Replace "pear" with "peach".
fruits[which(fruits == "pear")]<-"peach"
#Section 2:Data Frames
# 1. Create a data frame with the following columns:
# o student_id: numbers 1 to 4
# o name: "John", "Sara", "Ali", "Eva"
# o age: 20, 21, 19, 22
# o grade: "A", "B", "C", "A"
myDataFrame <- data.frame(student_id = (1:4),
                    name = c("John", "Sara", "Ali", "Eva"),
                    age = c(20, 21, 19, 22),
                    grade= c("A", "B", "C", "A"))
# Tasks:
# o Access the 2nd row.
myDataFrame[2,]
# o Access the name column.
myDataFrame$name
# o Find the grade of "Eva".
myDataFrame[which(myDataFrame$name=="Eva"),"grade"]

# 2. Add a new column called passed to the data frame.
# o If grade is "A" or "B", mark "Yes". Otherwise mark "No".
passed = (1:length(myDataFrame[1,]))
passed [(which(myDataFrame$grade=="A" | myDataFrame$grade=="B"))]="Yes"
passed [(which(myDataFrame$grade!="A" & myDataFrame$grade!="B"))]="No"
myDataFrame$passed <- passed
# 3. What happens if you try to access row 10 of this data frame?
myDataFrame[10,] 
# receive following message:
#   student_id name age grade passed
# NA         NA <NA>  NA  <NA>   <NA>

# Section 3: Logical Comparisons
# 1. Create two vectors:
#   o v1 <- c(1, 2, 3)
#   o v2 <- c(1, 2, 4)
v1 <- c(1, 2, 3)
v2 <- c(1, 2, 4)
# Tasks:
#   o Compare them using ==.
v1 == v2
# o Use identical() — what is the difference?
identical(v1,v2)
# 'V1 == v2' compares objects in v1 and v2 at the same index, 'identical(v1,v2)' 
# compares the whole the whole vector
#   2. Create a vector of numbers from 1 to 20.
myVector = (1:20)
# o Which numbers are greater than 10?
print(which (myVector>10))
#   o Which numbers are divisible by 2?
print(which (myVector%%2==0))

# Section 4: Working with Characters
# 1. Create a vector of names: "Alex", "Robert", "Mia", "Anna".
nameVector = c("Alex", "Robert", "Mia", "Anna")
# o Find the length of each name (nchar()).
nchar(nameVector) #
# o Which names have 4 letters?
nameVector[which(nchar(nameVector)==4)] #"Alex" "Anna"
#   2. Combine numbers and characters in one vector: c(1, 2, "three", 4).
combinedVector = c(1, 2, "three", 4)
# o What class is this vector?
class(combinedVector) #character
#   o Convert "3rd element" back to numeric. What happens?
as.numeric(combinedVector[3]) #Output is "NA"
#In addition following message is given:
# Warning message:
# NAs introduced by coercion

# Section 5: Importing & Exploring Data
# (If you don’t have your own file, create a CSV with 3–4 rows in Excel and read it in R.)
# 1. Import a dataset using read.csv().
setwd("C:/Users/Delwar/Desktop/Humber/BINF5003- Data Mining, Modeling, and Biostatistcs")
myDataSet<-read.csv("myDataSet.csv", header = TRUE)
# o Check how many rows and columns it has (dim()).
dim(myDataSet) #8 rows 4 columns
dim(read.csv("myDataSet.csv", header = TRUE))
# o Show the first 5 rows (head()).
head(myDataSet,5) 
head(read.csv("myDataSet.csv", header = TRUE))
#prints the following:
# V1 V2 V3 V4
# 1  1  1  1  1
# 2  2  2  2  2
# 3  3  3  3  3
# 4  4  4  4  4
# 5  5  5  5  5
# 6  6  6  6  6
# 2. Use summary() and str() to explore your dataset.
summary(myDataSet)
#produce the following message:
# ALPHA          BRAVO         CHARLIE         DELTA     
# Min.   :1.00   Min.   :1.00   Min.   :1.00   Min.   :1.00  
# 1st Qu.:2.75   1st Qu.:2.75   1st Qu.:2.75   1st Qu.:2.75  
# Median :4.50   Median :4.50   Median :4.50   Median :4.50  
# Mean   :4.50   Mean   :4.50   Mean   :4.50   Mean   :4.50  
# 3rd Qu.:6.25   3rd Qu.:6.25   3rd Qu.:6.25   3rd Qu.:6.25  
# Max.   :8.00   Max.   :8.00   Max.   :8.00   Max.   :8.00  
str(myDataSet)
#produce the following message:
# 'data.frame':	8 obs. of  4 variables:
# $ ALPHA  : int  1 2 3 4 5 6 7 8
# $ BRAVO  : int  1 2 3 4 5 6 7 8
# $ CHARLIE: int  1 2 3 4 5 6 7 8
# $ DELTA  : int  1 2 3 4 5 6 7 8
summary(read.csv("myDataSet.csv", header = FALSE))
# V1                 V2                 V3                 V4           
# Length:9           Length:9           Length:9           Length:9          
# Class :character   Class :character   Class :character   Class :character  
# Mode  :character   Mode  :character   Mode  :character   Mode  :character 
str(read.csv("myDataSet.csv", header = FALSE))
#produce the following message:
# 'data.frame':	9 obs. of  4 variables:
# $ V1: chr  "ALPHA" "1" "2" "3" ...
# $ V2: chr  "BRAVO" "1" "2" "3" ...
# $ V3: chr  "CHARLIE" "1" "2" "3" ...
# $ V4: chr  "DELTA" "1" "2" "3" ...
# o Which variables are numeric?
# myDataSet(read.csv("myDataSet.csv", header = TRUE)) are numeric variables
# o Which are character?
# read.csv("myDataSet.csv", header = FALSE) produces character variables

# Section 6: Filtering Data Frames
# Using the built-in dataset mtcars:
# 1. Load it by typing data(mtcars).
mtcars = force(mtcars)
# o How many rows and columns does it have?
dim(mtcars) #mtcars has 32 rows and 11 columns
# 2. Select only cars with mpg > 25.
carsMPG = mtcars[which(mtcars$mpg>25),]
force(carsMPG)
#Following Cars have >25 mph
#                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
# Fiat 128       32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
# Honda Civic    30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
# Toyota Corolla 33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
# Fiat X1-9      27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
# Porsche 914-2  26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
# Lotus Europa   30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
# 3. Select only cars with cyl == 6.
carsCYL = mtcars[which(mtcars$cyl==6),]
force(carsCYL)
#Following Cars have 6 cylinders
#                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
# Mazda RX4      21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
# Mazda RX4 Wag  21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
# Hornet 4 Drive 21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
# Valiant        18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
# Merc 280       19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
# Merc 280C      17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
# Ferrari Dino   19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
# 4. Which cars have both mpg > 20 and hp > 100?
carsMPGandHP= mtcars[which(mtcars$mpg>20&mtcars$hp>100),]
force(carsMPGandHP)
#Following cars have >20mpg and >100 hp
#               mpg cyl disp  hp drat    wt qsec vs am gear carb
# Lotus Europa 30.4   4 95.1 113 3.77 1.513 16.9  1  1    5    2

# Challenge Problems (Optional, for deeper practice)
# 1. Create a vector of 10 random numbers between 1 and 100.
myVector <- sample (1:100, 10, replace = TRUE)
# o Find the maximum and minimum values
max = max(myVector)
min = min(myVector)
# o Find the position (index) of the maximum value.
which(myVector==max)
# 2. Create a data frame for a mini class:
#   o Name: "Alice", "Bob", "Charlie", "Diana"
# o Math: 90, 80, 70, 95
# o Science: 85, 88, 75, 98
myDataFrame = data.frame(Name = c("Alice", "Bob", "Charlie", "Diana"),
                         Math = c(90, 80, 70, 95),
                         Science = c(85, 88, 75, 98))

# Tasks:
#   o Add a new column Average with the mean of Math and Science.
Average = (1:length(myDataFrame$Name))
for(x in (1:length(myDataFrame$Name))){
  Average[x] = mean(as.numeric(myDataFrame[x,-1]))
}
myDataFrame$Average=Average
# o Which student has the highest average?
myDataFrame[which(myDataFrame$Average==max(myDataFrame$Average)),] #Diana
#   3. From the abalone dataset:
#   o How many rows correspond to "M" (male)?
abalone = read.csv("abalone.csv",header=TRUE)
length(which(abalone$Sex=="M")) #1528 rows correspond to "M"
#   o How many to "F" (female)?
length(which(abalone$Sex=="F")) #1307 rows correspond to "F"
#   o Find the average length (Length) of "F".
mean(abalone[which(abalone$Sex=="F"),"Length"])

