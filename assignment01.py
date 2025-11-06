# Daily Calorie Tracker
#author: [Ayush Kumar Thakur]
#date: [08 oct 2025]

print("Welcome to the Daily Calorie Tracker")
print("This program helps you record your meals and calories for the day.\n")

# Ask how many meals
num_meals = int(input("How many meals did you have today? "))

# Create empty lists to store meal names and calories
meals = []
calories = []

# Get user input for each meal
for i in range(num_meals):
    meal_name = input(f"\nEnter the name of meal {i+1}: ")
    meal_calories = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(meal_calories)

#Calculate total and average calories
total_calories = sum(calories)
average_calories = total_calories / len(calories)

#Ask for daily calorie limit
daily_limit = float(input("\nEnter your daily calorie limit: "))

#Compare and display results
print("\n------ Daily Calorie Report ------")
print("Meal Name\tCalories")
print("----------------------")

for i in range(num_meals):
    print(f"{meals[i]}\t\t{calories[i]}")

print("------------------")
print(f"Total Calories:\t{total_calories}")
print(f"Average per Meal:\t{average_calories:.2f}")

if total_calories > daily_limit:
    print("You have exceeded your daily calorie limit.")
else:
    print("You are within your daily calorie limit.")

# Step 7: Option to save data (bonus)
save = input("\nDo you want to save this report? (yes/no): ").lower()

if save == "yes":
    with open("calorie_log.txt", "a") as f:
        f.write("\n------ Daily Calorie Report ------\n")
        for i in range(num_meals):
            f.write(f"{meals[i]}\t{calories[i]}\n")
        f.write("---------------\n")
        f.write(f"Total: {total_calories}\n")
        f.write(f"Average: {average_calories:.2f}\n")
        f.write(f"Daily Limit: {daily_limit}\n")
        if total_calories > daily_limit:
            f.write("Status: Exceeded limit\n")
        else:
            f.write("Status: Within limit\n")
        f.write("---------------\n")
    print("Report saved to calorie_log.txt")
else:
    print("Report not saved.")