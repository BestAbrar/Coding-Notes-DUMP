# ========== Week2.1 =========
# Create a vector named my_vector containing four numbers
my_vector = c(11,232,3,45)

# Access the 4th element in the vector
my_vector[4]  # This will return the value 45, which is the 4th element

# Check the dimensions of my_vector (since it's a vector, this will return NULL)
dim(my_vector)  # Vectors don’t have dimensions, so this will return NULL

# Create a data frame named my_df with three columns: name, score, and var
my_df <- data.frame(name = c("a", "b", "c"),
                    score = c(1, 2, 3),
                    var = c(1:3))

# Set custom row names for the data frame
rownames(my_df) <- c("row1", "row2", "row3")

# Check the dimensions of the data frame (returns number of rows and columns)
dim(my_df)  # This will return 3 rows and 3 columns

# Accessing specific rows and columns of the data frame
# Replace "row" and "column" with specific indices
my_df[row, column]  # This is a general format to access elements in the data frame

# Attempting to access the 4th row and 2nd column (out of bounds since my_df has only 3 rows)
my_df[4,2]  # This will return an error since there's no 4th row

# Adding a new column named "student" with values 3, 4, 5
my_df$student <- c(3:5)

# Adding another new column named "new_col" with values "aa", "cc", and "VV"
my_df$new_col <- c("aa", "cc", "VV")

# Accessing data in the data frame

# Access the 'score' column using the dollar sign ($)
my_df$score  # Returns the entire 'score' column

# Access the 2nd column using indexing
my_df[,2]  # Returns all values in the 2nd column, which is 'score'

# Access the 2nd row
my_df[2,]  # Returns all columns for the 2nd row

# Access the 'score' column by column name
my_df[,"score"]  # Same as my_df$score, returns the 'score' column

# Access the entire 'row3'
my_df["row3",]  # Returns all columns for 'row3'

# Access the 'score' value for 'row3'
my_df["row3","score"]  # Returns the value of 'score' in 'row3'

# Access the value in the 3rd row and 3rd column
my_df[3,3]  # Returns the value in row 3, column 3 (value is 3)

# Access the 'name' column
my_df[,"name"]  # Returns the 'name' column

# Access the 1st row
my_df[1,]  # Returns all columns for the 1st row

# Reading data from a CSV file into a data frame
my_data = read.csv(file.path("path_to_the_file", "binf5003.csv"))

# Reading data from a text file with tab delimiters into a data frame
my_data = read.delim(file.path("path_to_the_file", "binf5003.txt"))


# --------- Week2.2 ----------
x <- 9
x*8

x = c(1:3)
x

x*8

first5 <- c(1:5)
c(1,2,3,4,5)

# three students
student1 <- rep("student", 3)

student2 <- c( "student","student","studentss")

student1 == student2

test <- identical(student1, student2) #determine if 2 objects are identical
test

fruits <- c("apple", "banana", "grapefruit", "starfruit")
which(fruits == "starfruit") #show index(s) where condition is TRUE

evaluate <- 64 == 46

64 < 46

nums <- c(1, 2, 3)
class(nums)

num_and_char <- c(1, 2, 3, "three")
class(num_and_char) #R will store all elements as characters

num_and_char[2]
as.numeric(num_and_char[2]) #numeric values stored as characters can be converted back into numeric objects
as.numeric(num_and_char[4]) #characters values that cannot be converted to numeric objects will output NA

length(num_and_char) #number of items in object
length(num_and_char[4])
nchar(num_and_char[4]) #number of letters in a character value

which(nchar(num_and_char) == 5) #functions can be combined to create novel tasks

num_and_char <- c(1, 2, 3, 12, 11, 234, 657, "three")

num_and_char[8] 

#Filtering data with conditions is called data wrangling, pull only a section of the entire data

# index
which(nchar(num_and_char) >=2) #which elements have 2 or more letters

num_and_char[ which(nchar(num_and_char) >=2 ) ] 



my_vector <- c("apple", "banana", "grapefruit", "starfruit", "c", "h")
class(my_vector)

which(my_vector == "grapefruit")
my_vector[3]

my_vector[which(my_vector == "grapefruit")]

nchar(my_vector)

my_vector[which(nchar(my_vector) >=2 )]


# dataframe
students_data <- data.frame(
  student_id = 1:5,               # Numeric vector
  name = c("Alice", "Bob", "Carol", "David", "Eva"),  # Character vector
  age = c(21, 22, 20, 23, 21),    # Numeric vector
  major = c("Biology", "Math", "Physics", "Chemistry", "Art"), # Character vector
  gpa = c(3.8, 3.5, 3.9, 3.3, 3.7) # Numeric vector
)

class(students_data)

colnames(students_data)
rownames(students_data)

colnames(students_data) = c ("a", "b", "c", "x", "l", "bv")

dim(students_data)
dim(my_vector)

students_data[row, column]
students_data[1, 2]

# import a dataset
setwd("~/Documents/Humber/OneDrive/Nikta/Week2")
abalone <- read.csv("abalone.csv", header = TRUE)
dim(abalone)


summary(abalone)
str(abalone)

head(abalone, n = 2)
rm(alone)

abalone[row, columns]
f_ablone = abalone[abalone$Sex == "F", ]
f_ablone_which = abalone[which(abalone$Sex == "F"), ]

m_ablone = abalone[abalone$Sex == "M", ]
dim(m_ablone)

identical(f_ablone, f_ablone_which)


abalone$Sex == "F"


f_abalone = abalone[abalone$Sex == "F", ]
f_abalone_which = abalone[which(abalone$sex == "F"), ]




