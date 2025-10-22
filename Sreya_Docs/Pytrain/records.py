fobj = open("records.txt","r")

male_salaries = []
female_salaries = []

for line in fobj:
    columns = line.split()

    gender = columns[1]
    salary = int(columns[3])

    if gender == "m":
        male_salaries.append(salary)
    else:
        female_salaries.append(salary)

print(sum(male_salaries)/len(male_salaries))
print(sum(female_salaries)/len(female_salaries))