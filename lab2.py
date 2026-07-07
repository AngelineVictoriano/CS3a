#/*****************************************************/
#/* CS03A - Summer 2026
#/* Lab 2
#/* Student Name: Angeline Victoriano
#/* SID: 20528831
## /***************************************************/

# CHALLENGE 1

## AGE CLASSIFIER

age = int(input("Enter your age: "))

if age <= 1:
    print("You are an infant.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

## CALORIES BURNED

print("\n")
print("\n")
for i in range(10, 31, 5):
    print(f"Calories burned in {i} minutes: {4.2*i}")