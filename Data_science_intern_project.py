import statistics
file = open('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv', 'r')
file_data = file.read()
file.close()
file_data = file_data.split('\n')
formated_data = []
for data in file_data:
    data = data.split(',')
    formated_data += data

total_of_orders = 0
list_of_amounts = []
for i in range(10, 35007, 7):
    list_of_amounts.append(int(formated_data[i]))
    total_of_orders += int(formated_data[i])

average_order_value = total_of_orders / 5000

print('The current average order value is ${} but this does not seem reasonable because sneakers are \
relatively affordable. Based on some analysis of the data, there must have been some outliers.'.format(average_order_value))

list_of_amounts.sort()
new_average_order_value = statistics.median(list_of_amounts)
print('Based on finding the median, there is a more accurate answer for the average order value. The \
newly calculated AOV is ${}.'.format(new_average_order_value))