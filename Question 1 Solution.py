# Importing the required module
import statistics

# Reading the csv file with all the data
file = open('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv', 'r')
file_data = file.read()
file.close()

# Splitting the data after every line
file_data = file_data.split('\n')
formated_data = []
# Splitting the data into it's columns
for data in file_data:
    data = data.split(',')
    formated_data += data

# Defining variables for total order value and a list for each of the seperate amounts
total_of_orders = 0
list_of_amounts = []
# Looks through each order amount
for i in range(10, 35007, 7):
    list_of_amounts.append(int(formated_data[i]))
    total_of_orders += int(formated_data[i])

# Finding the average given in the question
average_order_value = total_of_orders / 5000

# Explain thought process
print('The current average order value is ${} but this does not seem reasonable because sneakers are \
relatively affordable. Based on some analysis of the data, there are some outliers.'.format(average_order_value))

# Using another method to find a resonable estimate of the average order value
new_average_order_value = statistics.median(list_of_amounts)

# Describe solution
print('The median seems like a more reasonable answer for the average order value for sneakers. The \
newly calculated AOV is ${}.'.format(new_average_order_value))
