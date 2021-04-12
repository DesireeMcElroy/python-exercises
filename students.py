# 20 Python Data Structure Manipulation Exercises

students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

print(students)


# 1. How many students are there?

print(len(students))

# 2. How many students prefer light coffee? For each type of coffee roast?
light = 0
medium = 0
dark = 0
for stu in students:
    if stu['coffee_preference'] == 'light':
        light += 1
    elif stu['coffee_preference'] == 'medium':
        medium += 1
    elif stu['coffee_preference'] == 'dark':
        dark += 1
print('Light drinkers: ', light)
print('Medium drinkers: ', medium)
print('Dark drinkers: ', dark)


# 3. How many types of each pet are there?

pet_types = []
for stu in students:
  pet_total = len(stu['pets'])
  for i in range(0, pet_total):
    if stu['pets'][i]['species'] not in pet_types:
      pet_types.append(stu['pets'][i]['species'])
print(pet_types)
print(len(pet_types))


# 4. How many grades does each student have? Do they all have the same number of grades?

grade_amount_per_student = 0
allstudents_grade_count = []
for stu in students: #for loop to check each student
    grade_amount_per_student = len(stu['grades']) #len returns the number of entries each student has in their 'grades' list
    allstudents_grade_count.append(grade_amount_per_student) #appends the current amount of grades for student to list containing counts for all students
print(allstudents_grade_count)



# 5. What is each student's grade average?

list_of_stu_grade_avg = []
for stu in students:
    student_grade_amount = len(stu['grades'])
    sum_of_grades = sum(stu['grades'])
    grade_average = sum_of_grades / student_grade_amount
    list_of_stu_grade_avg.append(grade_average)
print(list_of_stu_grade_avg)


# 6. How many pets does each student have?

students



# 7. How many students are in web development? data science?

webdev_students = 0
datasci_students = 0
for stu in students:
  if stu['course'] == 'web development':
    webdev_students += 1
  elif stu['course'] == 'data science':
    datasci_students += 1
print("Students in web development: ", webdev_students)
print("Students in data science: ", datasci_students)

# 8. What is the average number of pets for students in web development?

avg_num_pets = 0
total_pets = 0
num_students = 0
for stu in students:
  if stu['course'] == 'web development':
    student_pets = len(stu['pets'])
    total_pets = total_pets + student_pets
    num_students += 1
avg_num_pets = total_pets / num_students
print("Average number of pets per student in web development: ", avg_num_pets)

# 9. What is the average pet age for students in data science?
pet_count = 0
age_count = 0
for stu in students:
    if stu['course'] == 'data science':
        pet_count = pet_count + len(stu['pets'])
        for i in range(0, len(stu['pets'])):
            age_count = age_count + stu['pets'][i]['age']
avg_pet_age = age_count / pet_count
print("Average pet age is: ", avg_pet_age)


# 10. What is most frequent coffee preference for data science students?

light_drinkers = 0
medium_drinkers = 0
dark_drinkers = 0
for stu in students:
  if stu['course'] == 'data science':
    if stu['coffee_preference'] == 'light':
      light_drinkers += 1
    elif stu['coffee_preference'] == 'medium':
      medium_drinkers += 1
    elif stu['coffee_preference'] == 'dark':
      dark_drinkers += 1
  if light_drinkers > medium_drinkers and dark_drinkers:
    print("Light roast is the most frequent coffee preference.")
  elif medium_drinkers > light_drinkers and dark_drinkers:
    print("Medium roast is the most frequent coffee preference.")
  elif dark_drinkers > light_drinkers and medium_drinkers:
    print("Dark roast is the most frequent coffee preference.")

# 11. What is the least frequent coffee preference for web development students?
# 12. What is the average grade for students with at least 2 pets?
# 13. How many students have 3 pets?
# 14. What is the average grade for students with 0 pets?
# 15. What is the average grade for web development students? data science students?
# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# 17. What is the average number of pets for medium coffee drinkers?
# 18. What is the most common type of pet for web development students?
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?




