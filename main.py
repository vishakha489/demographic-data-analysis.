from demographic_data_analyzer import *

print("----- Demographic Data Analysis -----\n")

print("1. Number of people of each race:")
print(race_count, "\n")

print("2. Average age of men:", average_age_men, "\n")

print("3. Percentage with Bachelor's degree:", percentage_bachelors, "%\n")

print("4. Percentage with advanced education earning >50K:", percentage_higher_edu_rich, "%")
print("5. Percentage without advanced education earning >50K:", percentage_lower_edu_rich, "%\n")

print("6. Minimum hours worked per week:", min_work_hours)
print("7. Percentage of people who work minimum hours and earn >50K:", percentage_rich_min_workers, "%\n")

print("8. Country with highest percentage of >50K earners:", highest_earning_country)
print("   Highest percentage:", highest_percentage, "%\n")

print("9. Most popular occupation for >50K earners in India:", top_india_occupation)
