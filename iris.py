#Aideen Byrne 26/02/2018
#Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns.

with open ('data/iris.csv') as f:#opens dataset in csv file iris.csv  
  for line in f:#for loop to apply through all lines of dataset
    print (line.split (',') [0:4])#splits contents of csv file indexes 0 to 4 with spaces and commas

    

 