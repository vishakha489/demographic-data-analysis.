import pandas as pd
import glob

# Column names
columns = ['age','workclass','fnlwgt','education','education-num','marital-status',
           'occupation','relationship','race','sex','capital-gain','capital-loss',
           'hours-per-week','native-country','salary']

# Combine all CSV files
csv_files = ['adult-data.csv', 'adult-test.csv']
print("CSV files found:", csv_files)

df_list = []
for file in csv_files:
    if file == 'adult-test.csv':
        df_temp = pd.read_csv(file, names=columns, skipinitialspace=True, skiprows=1)
    else:
        df_temp = pd.read_csv(file, names=columns, skipinitialspace=True)
    df_list.append(df_temp)
df = pd.concat(df_list, ignore_index=True)
print("Total rows after combining:", len(df))

# Clean the salary column
df['salary'] = df['salary'].str.rstrip('.')

# ---------- Demographic Analysis ----------

race_count = df['race'].value_counts()
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
total = len(df)
bachelors = len(df[df['education'] == 'Bachelors'])
percentage_bachelors = round((bachelors / total) * 100, 1)

advanced_edu = ['Bachelors', 'Masters', 'Doctorate']
higher_edu = df[df['education'].isin(advanced_edu)]
percentage_higher_edu_rich = round(
    (len(higher_edu[higher_edu['salary'] == '>50K']) / len(higher_edu)) * 100, 1
)

lower_edu = df[~df['education'].isin(advanced_edu)]
percentage_lower_edu_rich = round(
    (len(lower_edu[lower_edu['salary'] == '>50K']) / len(lower_edu)) * 100, 1
)

min_work_hours = df['hours-per-week'].min()
min_workers = df[df['hours-per-week'] == min_work_hours]
rich_min_workers = min_workers[min_workers['salary'] == '>50K']
percentage_rich_min_workers = round(
    (len(rich_min_workers) / len(min_workers)) * 100, 1
)

country_counts = df['native-country'].value_counts()
rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
highest_earning_country = (rich_country_counts / country_counts * 100).idxmax()
highest_percentage = round((rich_country_counts / country_counts * 100).max(), 1)

india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
top_india_occupation = india_rich['occupation'].value_counts().idxmax()

