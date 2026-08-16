#1. STRING CONCATENATION
# Take name as input
str1 = "Hello "
name = input("Enter your Name: ")

# Concatenate string 1 and name
str2 = str1 + name
print(str2)

# Concatenate string 3 to the existing string (str2)
str3 = ", welcome to Python programming"
final_str = str2 + str3
print(final_str)


#2. STRING SLICING AND INDEXING
s = final_str  #"Hello AKASH, welcome to Python programming"
# a. First character
print(s[0])
# b. Last character
print(s[-1])
# c. First 5 characters
print(s[:5])
# d. Last 11 characters
print(s[-11:])
# e. Reverse the string
print(s[::-1])
# f. Extract "Python" using slicing
print(s[24:30])


#3. STRING METHODS
strM = "Python beginner tutorial"
# a. Uppercase
print(strM.upper())
# b. Lowercase
print(strM.lower())
# c. Capitalize (returns to original form)
print(strM.capitalize())
# d. Count occurrences of 't'
print(strM.count('t'))
# e. Replace "Python" with "Machine Learning"
print(strM.replace("Python", "Machine Learning"))


#4. TUPLE
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# a. Concatenate the two tuples
t_combine = tuple1 + tuple2
print(t_combine)          # (10, 20, 30, 40, 50, 60)
# b. Repeat elements of t_combine 3 times
t_repeat = t_combine * 3
print(t_repeat)
# c. Access the 3rd element from t_combine
print(t_combine[2])       # 30
# d. Access the first three elements
print(t_combine[:3])      # (10, 20, 30)
# e. Access the last three elements
print(t_combine[-3:])     # (40, 50, 60)