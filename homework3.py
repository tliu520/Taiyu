# PPHA 30537
# Spring 2024
# Homework 3

# YOUR NAME HERE  Taiyu Liu

# YOUR CANVAS NAME HERE  Taiyu Liu
# YOUR GITHUB USER NAME HERE   tliu520

# Due date: Sunday May 5th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_1_plot.png" (for 1.1), "q1_2_plot.png" (for 1.2),
# etc. using fig.savefig. If a question calls for more than one plot, name them
# "q1_1a_plot.png", "q1_1b_plot.png",  etc.

# Question 1.1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis tick labels are legible.  Add a title that reads "HW3 Q1.1".

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]


plt.figure(figsize=(10, 5))
plt.scatter(x, y1, color='blue', label='y1')
plt.plot(x, y2, color='red', label='y2')
plt.title("HW3 Q1.1")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Question 1.2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.
plt.figure(figsize=(8, 6))
x = range(10, 19)
y_blue = [20 - i for i in x]  
y_red = [i - 8 for i in x]  
plt.plot(x, y_blue, label='Blue', color='blue')
plt.plot(x, y_red, label='Red', color='red')
plt.title('X marks the spot')
plt.legend()
plt.show()
# Question 1.3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.
path = '/Users/liutaiyu/Desktop/Chicago /研一Spring/Python-I/HW-3/mpg.csv'
df = pd.read_csv(path)
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
axes[0].scatter(df['displacement'], df['mpg'])
axes[0].set_title('Displacement vs. MPG')
axes[0].set_xlabel('Displacement')
axes[0].set_ylabel('MPG')
axes[1].scatter(df['horsepower'], df['mpg'])
axes[1].set_title('Horsepower vs. MPG')
axes[1].set_xlabel('Horsepower')
axes[1].set_ylabel('MPG')
axes[2].scatter(df['weight'], df['mpg'])
axes[2].set_title('Weight vs. MPG')
axes[2].set_xlabel('Weight')
axes[2].set_ylabel('MPG')

plt.tight_layout()
plt.show()

# Question 1.4: Continuing with the data from question 1.3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.
plt.figure(figsize=(8, 6))
plt.scatter(df['cylinders'], df['mpg'])
plt.title('Scatter Plot: MPG vs Cylinders')
plt.xlabel('Cylinders')
plt.ylabel('MPG')
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(x='cylinders', y='mpg', data=df)
plt.title('Box Plot: MPG by Cylinders')
plt.xlabel('Cylinders')
plt.ylabel('MPG')
plt.show()

##The scatter plot is not ideal for displaying the relationship between cylinders (a categorical variable) and mpg (a continuous variable). 
##The categorical nature of 'cylinders' causes overlapping of data points at fixed x positions, which doesn't provide clear insights into distribution or variance within cylinder groups.  


# Question 1.5: Continuing with the data from question 1.3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:
#   - Remove the y-axis tick labels (the values) on the right two subplots - 
#     the scale of the ticks will already be aligned because the mpg values 
#     are the same in all axis.  
#   - Add a title to the figure (not the subplots) that reads "Changes in MPG"
#   - Add a y-label to the figure (not the subplots) that says "mpg"
#   - Add an x-label to each subplot for the x values
# Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Changes in MPG', fontsize=16)
axs[0, 0].scatter(df['displacement'], df['mpg'])
axs[0, 0].set_xlabel('Displacement')
axs[0, 0].set_ylabel('MPG')
axs[0, 1].scatter(df['horsepower'], df['mpg'])
axs[0, 1].set_xlabel('Horsepower')
axs[0, 1].set_ylabel('MPG')
axs[0, 1].set_yticklabels([]) 
axs[1, 0].scatter(df['weight'], df['mpg'])
axs[1, 0].set_xlabel('Weight')
axs[1, 0].set_ylabel('MPG')
axs[1, 1].scatter(df['acceleration'], df['mpg'])
axs[1, 1].set_xlabel('Acceleration')
axs[1, 1].set_ylabel('MPG')
axs[1, 1].set_yticklabels([])
fig.text(0.5, 0.04, 'Vehicle Characteristics', ha='center', va='center')
fig.text(0.04, 0.5, 'MPG', ha='center', va='center', rotation='vertical')
plt.tight_layout(rect=[0.03, 0.03, 0.97, 0.95])
plt.savefig('/Users/liutaiyu/Desktop/Chicago /研一Spring/Python-I/HW-3/Changes_in_MPG.png')
plt.show()
# Question 1.6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.
avg_mpg = df.groupby('origin')['mpg'].mean()
plt.figure(figsize=(8, 6))
avg_mpg.plot(kind='bar', color=['red', 'blue', 'green'])
plt.title('Average MPG by Car Origin')
plt.xlabel('Origin')
plt.ylabel('Average MPG')
plt.xticks(rotation=0) 
plt.show()
### The plot visually indicates that cars from the USA are the least fuel efficient on average compared to those from Japan and Europe.

# Question 1.7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
# Explain in a one-line comment what this plot says about the results of 
# question 1.6.

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='displacement', y='mpg', hue='origin')
plt.title('MPG vs. Displacement by Country of Origin')
plt.xlabel('Displacement')
plt.ylabel('MPG')
plt.show()

# Question 2: The file unemp.csv contains the monthly seasonally-adjusted unemployment
# rates for US states from January 2020 to December 2022. Load it as a dataframe, as well
# as the data from the policy_uncertainty.xlsx file from homework 2 (you do not have to make
# any of the changes to this data that were part of HW2, unless you need to in order to 
# answer the following questions).
#    2.1: Merge both dataframes together
import pandas as pd
unemp_path = '/Users/liutaiyu/Desktop/Chicago /研一Spring/Python-I/HW-3/unemp.csv'
unemp_df = pd.read_csv(unemp_path)
unemp_df['DATE'] = pd.to_datetime(unemp_df['DATE']) 
policy_path = '/Users/liutaiyu/Desktop/Chicago /研一Spring/Python-I/HW2/policy_uncertainty.xlsx'
policy_df = pd.read_excel(policy_path)
policy_df['date'] = pd.to_datetime(policy_df[['year', 'month']].assign(day=1))
merged_df = pd.merge(unemp_df, policy_df, left_on='DATE', right_on='date', how='inner')
print(merged_df.head())
#    2.2: Calculate the log-first-difference (LFD) of the EPU-C data
#    2.2: Select five states and create one Matplotlib figure that shows the unemployment rate
#         and the LFD of EPU-C over time for each state. Save the figure and commit it with 
#         your code.
merged_df['EPU_C_log'] = np.log(merged_df['EPU_Composite'])
merged_df['EPU_C_LFD'] = merged_df['EPU_C_log'].diff()
states = ['California', 'Texas', 'Florida', 'New York', 'Illinois']
fig, axs = plt.subplots(5, 1, figsize=(10, 20), sharex=True)
for i, state in enumerate(states):
    state_data = merged_df[merged_df['state'] == state]
    axs[i].plot(state_data['date'], state_data['unemp_rate'], label='Unemployment Rate', color='blue')
    axs[i].set_ylabel('Unemployment Rate')  # Proper indentation
    axs[i].legend(loc='upper left')
    ax2 = axs[i].twinx()  # Create a twin axis for the second variable
    ax2.plot(state_data['date'], state_data['EPU_C_LFD'], label='EPU-C LFD', color='green')
    ax2.set_ylabel('EPU-C Log-First-Difference')  # Proper indentation
    ax2.legend(loc='upper right')
    axs[i].set_title(state) 
fig.suptitle('Unemployment and EPU-C LFD by State')
fig.text(0.5, 0.04, 'Date', ha='center')
fig.text(0.04, 0.5, 'Metrics', va='center', rotation='vertical')
plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig('/Users/liutaiyu/Desktop/Chicago /研一Spring/Python-I/HW-3/figure.png')  # Specify your path
plt.show()
#    2.3: Using statsmodels, regress the unemployment rate on the LFD of EPU-C and fixed
#         effects for states. Include an intercept.
import statsmodels.api as sm
import statsmodels.formula.api as smf
merged_df['intercept'] = 1
model = smf.ols('unemp_rate ~ EPU_C_LFD + C(state) + intercept', data=merged_df)
results = model.fit()
print(results.summary())
#    2.4: Print the summary of the results, and write a 1-3 line comment explaining the basic
#         interpretation of the results (e.g. coefficient, p-value, r-squared), the way you 
#         might in an abstract.
merged_df['intercept'] = 1
model = smf.ols('unemp_rate ~ EPU_C_LFD + C(state) + intercept', data=merged_df)
results = model.fit()
print(results.summary())
print("\nThe regression results indicate that the coefficient for EPU_C_LFD is [coefficient], "
      "with a p-value of [p-value]. This suggests that the effect of EPU_C_LFD on unemployment "
      "rate is [statistically significant/not significant]. The R-squared value is [R-squared], "
      "indicating that [percentage]% of the variance in the unemployment rates is explained by "
      "the model.")