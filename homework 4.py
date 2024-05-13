# PPHA 30537
# Spring 2024
# Homework 4

# YOUR NAME HERE  Taiyu Liu

# YOUR CANVAS NAME HERE  Taiyu Liu
# YOUR GITHUB USER NAME HERE  tliu520

# Due date: Sunday May 12th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Explore the data APIs available from Pandas DataReader. Pick
# any two countries, and then 
#   a) Find two time series for each place
#      - The time series should have some overlap, though it does not have to
#        be perfectly aligned.
#      - At least one should be from the World Bank, and at least one should
#        not be from the World Bank.
#      - At least one should have a frequency that does not match the others,
#        e.g. annual, quarterly, monthly.
#      - You do not have to make four distinct downloads if it's more appropriate
#        to do a group of them, e.g. by passing two series titles to FRED.
import pandas as pd
from pandas_datareader import wb, data as pdr
import datetime
COUNTRIES = ['USA', 'GBR']
INDICATORS = {'World Bank': 'NY.GDP.PCAP.CD', 'FRED_USA': 'USACPIALLMINMEI', 'FRED_GBR': 'GBRCPIALLMINMEI'}
START_DATE = datetime.datetime(2010, 1, 1)
END_DATE = datetime.datetime(2020, 12, 31)
gdp_data = wb.download(indicator=INDICATORS['World Bank'], country=COUNTRIES, start=START_DATE.year, end=END_DATE.year)
gdp_data.reset_index(inplace=True)
#   b) Adjust the data so that all four are at the same frequency (you'll have
#      to look this up), then do any necessary merge and reshaping to put
#      them together into one long (tidy) format dataframe.
gdp_data['year'] = pd.to_datetime(gdp_data['year'], format='%Y').dt.to_period('Y').dt.to_timestamp()
cpi_data_usa = pdr.DataReader(INDICATORS['FRED_USA'], 'fred', START_DATE, END_DATE).resample('Y').mean().reset_index()
cpi_data_gbr = pdr.DataReader(INDICATORS['FRED_GBR'], 'fred', START_DATE, END_DATE).resample('Y').mean().reset_index()
#   c) Finally, go back and change your earlier code so that the
#      countries and dates are set in variables at the top of the file. Your
#      final result for parts a and b should allow you to (hypothetically) 
#      modify these values easily so that your code would download the data
#      and merge for different countries and dates.
#      - You do not have to leave your code from any previous way you did it
#        in the file. If you did it this way from the start, congrats!
#      - You do not have to account for the validity of all the possible 
#        countries and dates, e.g. if you downloaded the US and Canada for 
#        1990-2000, you can ignore the fact that maybe this data for some
#        other two countries aren't available at these dates.
COUNTRIES = ['USA', 'GBR'] 
INDICATORS = {
    'World Bank': 'NY.GDP.PCAP.CD',   
    'FRED_USA': 'USACPIALLMINMEI',    
    'FRED_GBR': 'GBRCPIALLMINMEI'     
}
START_DATE = datetime.datetime(2010, 1, 1)  
END_DATE = datetime.datetime(2020, 12, 31)  
gdp_data = wb.download(indicator=INDICATORS['World Bank'], country=COUNTRIES, start=START_DATE.year, end=END_DATE.year)
gdp_data.reset_index(inplace=True)
gdp_data['year'] = pd.to_datetime(gdp_data['year'], format='%Y').dt.to_period('Y').dt.to_timestamp()
cpi_data_usa = pdr.DataReader(INDICATORS['FRED_USA'], 'fred', START_DATE, END_DATE).resample('Y').mean().reset_index()
cpi_data_gbr = pdr.DataReader(INDICATORS['FRED_GBR'], 'fred', START_DATE, END_DATE).resample('Y').mean().reset_index()
#   d) Clean up any column names and values so that the data is consistent
#      and clear, e.g. don't leave some columns named in all caps and others
#      in all lower-case, or some with unclear names, or a column of mixed 
#      strings and integers. Write the dataframe you've created out to a 
#      file named q1.csv, and commit it to your repo.
gdp_usa = gdp_data[gdp_data['country'] == 'United States']
gdp_gbr = gdp_data[gdp_data['country'] == 'United Kingdom']
final_df = pd.DataFrame()
for (gdp, cpi, suffix) in [(gdp_usa, cpi_data_usa, 'USA'), (gdp_gbr, cpi_data_gbr, 'GBR')]:
    merged = pd.merge(gdp, cpi, how='left', left_on='year', right_on='DATE')
    merged.rename(columns={'NY.GDP.PCAP.CD': f'GDP_{suffix}', cpi.columns[1]: f'CPI_{suffix}'}, inplace=True)
    merged.drop(['country', 'DATE'], axis=1, inplace=True)
    final_df = pd.concat([final_df, merged], axis=1)
final_df.columns = [col.replace('_', ' ').title() for col in final_df.columns]
final_df.to_csv('q1.csv', index=False)

# Question 2: On the following Harris School website:
# https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics
# There is a list of six bullet points under "Required courses" and 12
# bullet points under "Elective courses". Using requests and BeautifulSoup: 
#   - Collect the text of each of these bullet points
#   - Add each bullet point to the csv_doc list below as strings (following 
#     the columns already specified). The first string that gets added should be 
#     approximately in the form of: 
#     'required,PPHA 30535 or PPHA 30537 Data and Programming for Public Policy I'
#   - Hint: recall that \n is the new-line character in text
#   - You do not have to clean up the text of each bullet point, or split the details out
#     of it, like the course code and course description, but it's a good exercise to
#     think about.
#   - Using context management, write the data out to a file named q2.csv
#   - Finally, import Pandas and test loading q2.csv with the read_csv function.
#     Use asserts to test that the dataframe has 18 rows and two columns.
import requests
from bs4 import BeautifulSoup
import pandas as pd
def extract_courses(soup, section_title):
    course_list = []
    heading = soup.find('h3', text=lambda t: t and section_title in t)
    if heading:
        for ul in heading.find_next_siblings():
            if ul.name == 'ul':
                course_list.extend([li.text.strip() for li in ul.find_all('li')])
            elif ul.name == 'h3':
                break
    return course_list
def main():
    url = 'https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics'
    response = requests.get(url)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')
    required_courses = extract_courses(soup, 'Required courses')
    elective_courses = extract_courses(soup, 'Elective courses')
    courses_data = [{'type': 'required', 'description': course} for course in required_courses]
    courses_data.extend({'type': 'elective', 'description': course} for course in elective_courses)
    df = pd.DataFrame(courses_data)
    csv_path = '/Users/liutaiyu/Desktop/Chicago /研一Spring/Python-I/q2.csv'
    df.to_csv(csv_path, index=False)
    try:
        df_test = pd.read_csv(csv_path)
        print(df_test)
    except Exception as e:
        print(f"An error occurred when reading the CSV file: {e}")
if __name__ == '__main__':
    main()