print("Greetings!")

#collecting data
def generate_profile(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    else:
        return "Adult"

user_name = input("please, write your full name:")
birth_year_str = input("write your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

hobbies = []
while True:
    hobby = input("enter you hobby: ")
    if hobby.lower() == "stop":
        break
    else:
        hobbies.append(hobby)

collected_data = [
    ("Name", user_name),
    ("Age", current_age),
    ("Life Stage", generate_profile(current_age)),
    ("Hobbies", hobbies),
]
# transforming list to dict
collected_data = dict(collected_data)

# console output
print("---")
print("Profile Summary:")
print(f"Full Name: {collected_data['Name']} ")
print(f"Age: {collected_data['Age']}")
print(f"Life Stage: {collected_data['Life Stage']}")
if len(collected_data['Hobbies']) <= 0:
    print("You didn't mention any hobbies")
else:
    num_of_hobbies = len(collected_data['Hobbies'])
    print(f"Favorite hobbies ({num_of_hobbies}):")
    for hobby in collected_data["Hobbies"]:
        print(f" - {hobby}")
print("---")
