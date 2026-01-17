# Load necessary libraries
library(tidyverse)  # For data manipulation and piping
library(dplyr)      # For advanced data manipulation functions

# Data Preparation Section ----------------

# Create a custom dataframe
df <- data.frame(
  student_id = c(101, 102, 103, 104),
  name = c("Alice", "Bob", "Charlie", "David"),
  course = c("Math", "Science", "Math", NA),  # NA for missing course
  grade = c(85, 90, 78, 88)
)

# Round numeric values
round(88.08908, digits = 2)   # Round a standalone number to 2 decimal places

# Calculate standard deviation and round
sd(df$grade) %>% round(digits = 2)  # Using pipe for chaining
round(sd(df$grade), digits = 2)     # Standard base R approach

# Different ways to access standard deviation
sd(df[,"grade"])  # Access via column name
sd(df[,4])        # Access via column index
df$grade %>% sd() # Using pipe operator

# Base R Indexing Section ----------------

df[3, ]           # Get the entire 3rd row
df[, 2]           # Get the 2nd column by index
df[, "name"]      # Get the 'name' column by name
df$name           # Access 'name' column using $ operator

# Tidyverse (Pipe) Indexing Section --------

mean(df$grade)             # Base R: calculate the mean of 'grade' column
df$grade %>% mean()        # Using pipe to calculate the same

df[which(df$name == "Alice"), 1:2]  # Base R: Filter rows for 'Alice' and select columns 1:2
subset(df, name == "Alice", select = c(student_id, name))  # Using subset function
df %>% subset(name == "Alice")     # Using pipe with subset

df %>% filter(name == "Alice") %>% select(c(student_id, name))  # Using pipe: filter and select
filter(df, name == "Alice")  # dplyr filter only

# Reshaping Data Section ----------------

# Create a new dataframe in wide format
df_wide <- data.frame(
  student_id = c(101, 102, 103, 104),
  math = c(85, NA, 78, NA),
  science = c(NA, 90, NA, NA),
  history = c(NA, NA, NA, 88)
)

# Reshape wide to long format using tidyverse (pipe)
df_long1 = df_wide %>% pivot_longer(cols = c(math, science), names_to = "course", values_to = "grade")

# Alternative method to reshape
df_long2 = pivot_longer(df_wide, cols = c(math, science), names_to = "course", values_to = "grade")

# Check if both methods give identical results
identical(df_long1, df_long2)

