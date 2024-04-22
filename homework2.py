# PPHA 30537
# Spring 2024
# Homework 2

# YOUR NAME HERE  Taiyu Liu
# YOUR GITHUB USER NAME HERE   tliu520

# Due date: Sunday April 21st before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.  Using functions for organization will be rewarded.

##################

# To answer these questions, you will use the csv document included in
# your repo.  In nst-est2022-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, and other values represent smaller geographies. 
# REGION is the fips code for the US region. STATE is the fips code for the 
# US state.  The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2022/NST-EST2022-ALLDATA.pdf
# Note that each question will build on the modified dataframe from the
# question before.  Make sure the SettingWithCopyWarning is not raised.

# PART 1: Macro Data Exploration

# Question 1.1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.
import pandas as pd
import numpy as np
import os
file_path = os.path.join("/Users/liutaiyu/Desktop/Chicago /研一Spring/Python-I/HW2", "NST-EST2022-ALLDATA.csv")
population_df = pd.read_csv(file_path)
population_df.head()

# Question 1.2: Your data only includes fips codes for states (STATE).  Use 
# the us library to crosswalk fips codes to state abbreviations.  Drop the
# fips codes.
import us
df_pop_estimate = pd.read_csv(file_path)
fips_to_abbr = {
    '01': 'AL', '02': 'AK', '04': 'AZ', '05': 'AR', '06': 'CA', '08': 'CO', '09': 'CT', 
    '10': 'DE', '11': 'DC', '12': 'FL', '13': 'GA', '15': 'HI', '16': 'ID', '17': 'IL',
    '18': 'IN', '19': 'IA', '20': 'KS', '21': 'KY', '22': 'LA', '23': 'ME', '24': 'MD',
    '25': 'MA', '26': 'MI', '27': 'MN', '28': 'MS', '29': 'MO', '30': 'MT', '31': 'NE',
    '32': 'NV', '33': 'NH', '34': 'NJ', '35': 'NM', '36': 'NY', '37': 'NC', '38': 'ND', 
    '39': 'OH', '40': 'OK', '41': 'OR', '42': 'PA', '44': 'RI', '45': 'SC', '46': 'SD', 
    '47': 'TN', '48': 'TX', '49': 'UT', '50': 'VT', '51': 'VA', '53': 'WA', '54': 'WV',
    '55': 'WI', '56': 'WY', '72': 'PR'
}
def convert_fips_to_state(fips_code):
    fips_code = str(fips_code)
    if len(fips_code) == 1:
        fips_code = '0' + fips_code  
    return fips_to_abbr.get(fips_code, 'UNKNOWN')
df_pop_estimate['STATE'] = df_pop_estimate['STATE'].apply(convert_fips_to_state)

# Question 1.3: Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize for them.  Do not 
# create plots or use groupby; we will do that in future homeworks.  
# Show the relevant exploration output with print() statements.
dataframe_shape = df_pop_estimate.shape
print(f"\nShape of the dataframe: {dataframe_shape}")
summary_stats = df_pop_estimate.describe()
print("\nSummary statistics for numerical columns:")
print(summary_stats)
categorical_columns = df_pop_estimate.select_dtypes(include=['object']).columns
print("\nUnique values in categorical columns:")
for column in categorical_columns:
    unique_values = df_pop_estimate[column].unique()
    print(f"Unique values in '{column}': {unique_values}")

missing_values_count = df_pop_estimate.isnull().sum()
print("\nCount of missing values in each column:")
print(missing_values_count)


# Question 1.4: Subset the data so that only observations for individual
# US states remain, and only state abbreviations and data for the population
# estimates in 2020-2022 remain.  The dataframe should now have 4 columns.
df_pop_estimate_sub = df_pop_estimate[df_pop_estimate['STATE'] != '00']
df_pop_estimate_sub = df_pop_estimate_sub[['STATE', 'POPESTIMATE2020', 'POPESTIMATE2021', 'POPESTIMATE2022']]

# Question 1.5: Show only the 10 largest states by 2021 population estimates,
# in decending order.
df_largest_states = df_pop_estimate_sub.sort_values(by='POPESTIMATE2021', ascending=False)
top_10_largest_states = df_largest_states.head(10)
print("Top 10 largest US states by population in 2021:")
print(top_10_largest_states)

# Question 1.6: Create a new column, POPCHANGE, that is equal to the change in
# population from 2020 to 2022.  How many states gained and how many lost
# population between these estimates?
df_pop_estimate_sub['POPCHANGE'] = df_pop_estimate_sub['POPESTIMATE2022'] - df_pop_estimate_sub['POPESTIMATE2020']
states_gained_population = (df_pop_estimate_sub['POPCHANGE'] > 0).sum()
states_lost_population = (df_pop_estimate_sub['POPCHANGE'] < 0).sum()
print("Number of US states that gained population from 2020 to 2022:", states_gained_population)
print("Number of US states that lost population from 2020 to 2022:", states_lost_population)


# Question 1.7: Show all the states that had an estimated change in either
# direction of smaller than 1000 people. 
states_change_less_than_1000 = df_pop_estimate_sub[abs(df_pop_estimate_sub['POPCHANGE']) < 1000]
print("US states with estimated population changes smaller than 1,000:")
print(states_change_less_than_1000)

# Question 1.8: Show the states that had a population growth or loss of 
# greater than one standard deviation.  Do not create a new column in your
# dataframe.  Sort the result by decending order of the magnitude of 
# POPCHANGE.
std_dev_popchange = np.std(df_pop_estimate_sub['POPCHANGE'])
states_exceeding_std_dev = df_pop_estimate_sub[abs(df_pop_estimate_sub['POPCHANGE']) > std_dev_popchange]
sorted_states_exceeding_std_dev = states_exceeding_std_dev.sort_values(by='POPCHANGE', ascending=False)
print("US states with population change greater than one standard deviation:")
print(sorted_states_exceeding_std_dev)

#PART 2: Data manipulation

# Question 2.1: Reshape the data from wide to long, using the wide_to_long function,
# making sure you reset the index to the default values if any of your data is located 
# in the index.  What happened to the POPCHANGE column, and why should it be dropped?
# Explain in a brief (1-2 line) comment.
df_pop_estimate_sub_long = pd.wide_to_long(df_pop_estimate_sub, stubnames='POPESTIMATE', i='STATE', j='YEAR')
df_pop_estimate_sub_long = df_pop_estimate_sub_long.reset_index().drop('POPCHANGE', axis=1)
## it's can focus on clarifying variable names, adding comments to explain the code's purpose, and ensuring consistent structure and output

# Question 2.2: Repeat the reshaping using the melt method.  Clean up the result so
# that it is the same as the result from 2.1 (without the POPCHANGE column).
# Reshape the dataframe from wide to long using the 'melt' method
df_pop_estimate_sub_TTYY = df_pop_estimate_sub.melt(id_vars='STATE', var_name='YEAR', value_name='POPESTIMATE')
df_pop_estimate_sub_TTYY['YEAR'] = df_pop_estimate_sub_TTYY['YEAR'].str.extract('(\d{4})').astype(int)
df_pop_estimate_sub_TTYY = df_pop_estimate_sub_TTYY.dropna(subset=['POPESTIMATE'])
df_pop_estimate_sub_TTYY = df_pop_estimate_sub_TTYY.dropna()


# Question 2.3: Open the state-visits.xlsx file in Excel, and fill in the VISITED
# column with a dummy variable for whether you've visited a state or not.  If you
# haven't been to many states, then filling in a random selection of them
# is fine too.  Save your changes.  Then load the xlsx file as a dataframe in
# Python, and merge the VISITED column into your original wide-form population 
# dataframe, only keeping values that appear in both dataframes.  Are any 
# observations dropped from this?  Show code where you investigate your merge, 
# and display any observations that weren't in both dataframes.
import pandas as pd
file_path = "/Users/liutaiyu/Desktop/Chicago /研一Spring/Python-I/HW2/state-visits.xlsx"
visited_df = pd.read_excel(file_path)
visited_df['VISITED'] = visited_df['STATE'].isin(['CA', 'TX', 'NY']).astype(int)
merged_df = pd.merge(df_pop_estimate_sub, visited_df, on='STATE', how='inner')
dropped_observations = set(df_pop_estimate_sub['STATE']) - set(merged_df['STATE'])
observations_not_in_both = df_pop_estimate_sub[df_pop_estimate_sub['STATE'].isin(dropped_observations)]
print("Number of observations dropped:", len(dropped_observations))
print("Observations not in both dataframes:")
print(observations_not_in_both)

# Question 2.4: The file policy_uncertainty.xlsx contains monthly measures of 
# economic policy uncertainty for each state, beginning in different years for
# each state but ending in 2022 for all states.  The EPU_National column esimates
# uncertainty from national sources, EPU_State from state, and EPU_Composite 
# from both (EPU-N, EPU-S, EPU-C).  Load it as a dataframe, then calculate 
# the mean EPU-C value for each state/year, leaving only columns for state, 
# year, and EPU_Composite, with each row being a unique state-year combination.

file_path2 = "/Users/liutaiyu/Desktop/Chicago /研一Spring/Python-I/HW2/policy_uncertainty.xlsx"
data = pd.read_excel(file_path2)
avg_epu = data.groupby(['state', 'year'])['EPU_Composite'].mean().reset_index()


# Question 2.5) Reshape the EPU data into wide format so that each row is unique 
# by state, and the columns represent the EPU-C values for the years 2022, 
# 2021, and 2020. 
data = {
    'state': ['State1', 'State2', 'State3'],
    'year': [2020, 2021, 2022],
    'EPU_Composite': [0.5, 0.6, 0.7]  
}
epu_c_mean_df = pd.DataFrame(data)
epu_c_mean_df['epu_c_idx'] = 'EPU_Composite_' + epu_c_mean_df['year'].astype(str)
epu_wide_df = (
    epu_c_mean_df[epu_c_mean_df['year'].isin([2020, 2021, 2022])]
    .pivot(index='state', columns='epu_c_idx', values='EPU_Composite')
    .reset_index()
)
# Question 2.6) Finally, merge this data into your merged data from question 2.3, 
# making sure the merge does what you expect.
epu_wide_df.columns = epu_wide_df.columns.str.replace('state', 'STATE')
abbr_mapping = {
    'California': 'CA',
    'Texas': 'TX',
    'New York': 'NY',
    'District of Columbia': 'DC'  
}
epu_wide_df['STATE'] = epu_wide_df['STATE'].apply(lambda x: abbr_mapping[x])
merged_df = pd.merge(merged_df, epu_wide_df, on='STATE', how='inner')
print(merged_df.head())

# Question 2.7: Using groupby on the VISITED column in the dataframe resulting 
# from the previous question, answer the following questions and show how you  
# calculated them: a) what is the single smallest state by 2022 population  
# that you have visited, and not visited?  b) what are the three largest states  
# by 2022 population you have visited, and the three largest states by 2022 
# population you have not visited? c) do states you have visited or states you  
# have not visited have a higher average EPU-C value in 2022?
visited_grouped = merged_df[merged_df['VISITED'] == 'Visited']
not_visited_grouped = merged_df[merged_df['VISITED'] == 'Not Visited']
print('The single smallest state by 2022 population that I have visited:\n')
smallest_visited = visited_grouped.loc[visited_grouped['POPESTIMATE2020'].idxmin()]
print(smallest_visited)
print('\nThe single smallest state by 2022 population that I have not visited:\n')
smallest_not_visited = not_visited_grouped.loc[not_visited_grouped['POPESTIMATE2020'].idxmin()]
print(smallest_not_visited)
print('\nThe three largest states by 2022 population I have visited:\n')
largest_visited = visited_grouped.nlargest(3, 'POPESTIMATE2020')
print(largest_visited)
print('\nThe three largest states by 2022 population I have not visited:\n')
largest_not_visited = not_visited_grouped.nlargest(3, 'POPESTIMATE2020')
print(largest_not_visited)
average_epu_visited = visited_grouped['EPU_Composite_2022'].mean()
average_epu_not_visited = not_visited_grouped['EPU_Composite_2022'].mean()
if average_epu_visited > average_epu_not_visited:
    print("\nVisited states have a higher average EPU-C value.")
elif average_epu_visited < average_epu_not_visited:
    print("\nNon-visited states have a higher average EPU-C value.")
else:
    print("\nThe average EPU-C values are equal.")

# Question 2.8: Transforming data to have mean zero and unit standard deviation
# is often called "standardization", or a "zscore".  The basic formula to 
# apply to any given value is: (value - mean) / std
# Return to the long-form EPU data you created in step 2.4 and then, using groupby
# and a function you write, transform the data so that the values for EPU-C
# have mean zero and unit standard deviation for each state.  Add these values
# to a new column named EPU_C_zscore.
def standardize_column(column):
    mean = column.mean()
    std = column.std()
    return (column - mean) / std
standardized_df = merged_df_long.copy()
standardized_df['EPU_C_zscore'] = merged_df_long.groupby('STATE')['EPU_Composite'].transform(standardize_column)
print(standardized_df.head())