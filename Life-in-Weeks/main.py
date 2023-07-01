age = input("What is your current age? ")
one_year_days = 365
one_year_months = 12
one_year_weeks = 52
max_years = 90
int_age = int(age)
number_left_days = (max_years  - int_age)*one_year_days
number_left_months = (max_years - int_age)*one_year_months
number_left_weeks = (max_years - int_age) * one_year_weeks
#by using fstrings
print(f"You have {number_left_days} days, {number_left_weeks} weeks, and {number_left_months} months left.")

