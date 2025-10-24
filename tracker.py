""" Name - Ditya Manral
Date - 17/10/2025
Project Title - Building a Calorie Tracking Console app"""
print("Welcome to the Daily Calorie Tracker")
print("This program helps to log meals , track total calories and compare against a personal daily limit")
meal_count = int(input("How many meals do you want to enter for today : "))
meals = []
calories = []
count = 1 
while count <= meal_count:
    meal = input("Enter meal name : ")
    cal = float(input("Enter calories for " + meal+ ": "))
    meals.append(meal)
    calories.append(cal)
    count += 1
total = sum(calories)
avg = total / meal_count
limit = int(input("Enter you daily calorie limit : "))
print("\n------------------------------")
print("    Calorie Summary    ")
print("------------------------------")
index = 0 
while index < meal_count:
    print(meals[index], "\t", calories[index])
    index += 1 
print("------------------------------")
print("Total : " , "\t" , total)
print("Average : " , "\t" , round(avg,2))
if(total > limit):
    print("\n ⚠️ You have eaten more than your daily limit !!!")
else:
    print("\n You are within your daily limit !!!")
