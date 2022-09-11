# Worked with Bikram Barua and Mathew Katz

## Q1 ##
# Can you debug and fix the output? The code should return the entire list

numbers = [1, 2, 3, 4, 5]
print(numbers[0:5])
print(numbers)

## Q2 ##
# Design a program that asks the user to enter a store’s sales
# for each day of the week. The amounts should be stored in a list. 
# Use a loop to calculate the total sales for the week and display the result.

#List for days of the week
days_of_the_week = ['Sunday', 'Monday', 'Tuesday','Wednesday','Thursday','Friday', 'Saturday']

#Empty list that can have values edited inside it
sales=[]

#For loop to collect sales values then to be stored in list
for day in range(0,7):
  value = int( input(" Sales for " + days_of_the_week[day] + " = "))
  sales.append(value)

# For loop to calcilate total of sales for the week 
total_sales = 0
for idx in range(0,7):
  total_sales += sales[idx]

print( f' The Total Sales for the week is {total_sales}') # f - string


#Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
#alphabetical order
# Print your list in its original order.
# Use the sort() function to arrange your list in order and reprint your list.
# Use the sort(reverse=True) and reprint your list.

#List of places to travel
travel_location = ['Paris', 'Maui', 'London', 'Rome', 'Tokyo']

#Sorting list
travel_location.sort()

print(travel_location)

#Sorting list in reverse order
travel_location.sort(reverse = True)

print(travel_location)


#Q4. Write a program that creates a dictionary containing course numbers and the room numbers
#of the rooms where the courses meet. The program should also create a dictionary containing course
#numbers and the names of the instructors that teach each course. After that, the program should let
#the user enter a course number, then it should display the course’s room number, instructor, and meeting time.

#Dictionary of course names
course_dict = { 'DATA101': { 'room': 203, 'intructor': 'Jones', 'meeting_time': '8:30 AM'},
                'MATH101': { 'room': 306, 'intructor': 'Mark', 'meeting_time': '9:00 AM'},
                'DATA131': { 'room': 224, 'intructor': 'Michael', 'meeting_time': '10:30 AM'},
                'DATA661': { 'room': 142, 'intructor': 'Brian', 'meeting_time': '11:00 AM'}
}

# print(course_dict) Just printing for testing

x = course_dict.keys()

print(x)


# Getting the input course number
i_course = input("Enter the course number ")
course_info = course_dict.get(i_course) #(.get dictionary method)

print(" Room Number is " + str(course_info.get('room')))
print(" Instructor is " + str(course_info.get('instructor')))
print(" Meeting Time is " + str(course_info.get('meeting_time')))

#Q5. Write a program that keeps names and email addresses in a dictionary as key-value pairs.
#The program should then demonstrate the four options:
#  ● look up a person’s email address,
#  ● add a new name and email address,
#  ● change an existing email address, and
#  ● delete an existing name and email address.

names_email = {  'Mary': 'rkdipqy701@gaduguda.xyz',
                 'Danial': 'danial_metz@gmail.com',
                 'Josiane': 'josiane_tillman@gmail.com'
               }

print(names_email)

# Display names in dictionary

x = names_email.keys()

print(x)


#Getting email from name
name = input( " Enter the person's name ")
print( f'Their email is {names_email[name]}')

#Adding a new name and email address
names_email["Emily"] = "emilio37@hotmail.com"

#Changing John's email address, 
names_email["Mary"] = "millie.konopelski69@gmail.com"

#Deleting an existing name and email address
del[names_email['Danial']]

print(names_email)













