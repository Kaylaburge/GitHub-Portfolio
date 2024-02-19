#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# Kayla Burge
"""
import os
import pandas as pd
from dotenv import load_dotenv
from dotenv import find_dotenv

os.getcwd()
os.chdir("/Users/kaylaburge/Downloads") 
load_dotenv(find_dotenv())

OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')
print(OPENAI_API_KEY)

from openai import OpenAI 
client=OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a marketing assistant, skilled in making sales slogans based on given information."},
    {"role": "user", "content": "Compose an advertising slogan that sells a professional fraternity called 'Pi Sigma Epsilon'. This fraternity builds colleges students' skills in marketing, saes, and management through real professional development scenarios. Also, we are located at the University of Florida and our mascot is a gator."}
  ]
)

print(completion.choices[0].message.content)
# save that output from ChatGPT to an object
text = (completion.choices[0].message.content)
# The output was: "Pi Sigma Epsilon at the University of Florida - Gator Power Boosting Your Sales, Marketing, and Management Prowess!"

# This block is saving the GPT output to a txt file on my device (where I told it in the path).
# https://blog.enterprisedna.co/python-write-to-file/
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
file_handle = open('output1.txt', 'w+')
file_handle.write(text)
file_handle.close()


#This block of code is acting as a GPT prompt also where the system/content is giving the siuational context and the user/content is giving it the query prompt.
# This is creating a more comprehensivequery. I used a prompt similar to the one used in class.
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a data scientist"},
        {"role": "user", "content": "Explain how to use ChatGPT to automate data cleaning and preprocessing tasks for machine learning models with Python examples."}
    ]
 )

# This block prints a step by step rpocess in which I can use Chat GPT and machine learning models to clean and process data with sample python code.
# https://platform.openai.com/docs/guides/text-generation/json-mode
print(completion.choices[0].message.content)
text = (completion.choices[0].message.content)

# This block is again saving the GPT txt file output to my computer in the specified path.
file_handle = open('output2.txt', 'w+')
file_handle.write(text)
file_handle.close()


# This block reads in the CSV file, create and prints the dataframe, and lists of the column names.
df = pd.read_csv('beststates.csv')
column_names = df.columns.tolist()
column_names = ', '.join(column_names)
print(df)

# This block takes the list of column names and adds them into the context portion of the query language to give context to the GPT.
Instructions = ' The column headings in a database are ' + column_names + '. '
file_handle = open('Instructions.txt', 'w+')
file_handle.write(Instructions)
file_handle.close()

# The txt file has been set up, now we can create a complex query.

# This prompt is creating a query statement looking at the CSV file and drawing a conclusion.
query_text = "Create a SQL statement to identify the top 5 most dangerous states."
file_handle = open('query_text.txt', 'w+')
file_handle.write(query_text)
file_handle.close()


# This block of code is from class. It is positively reinforcing the GPT to make it motivated to do a better job.
#It references the Instructions and query_text txt files that we made to act as the GPT query prompt like in the previous examples.
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a really good data engineer."},
        {"role": "user", "content": Instructions},
        {"role": "user", "content": query_text}
    ]
 )

print(completion.choices[0].message.content)

# save that output from ChatGPT to an object
text = (completion.choices[0].message.content)


#This is saving the GPT output to a txt file. The GPT is explaining/confirming what it is going to do with the data to answer the query.
file_handle = open('output3.txt', 'w+')
file_handle.write(text)
file_handle.close()


# This is coverting the query language into python code that it can run to figure out the result.
Instructions = "The column headings in a dataframe are " + column_names + '. '
query_text = "Create python code to identify the 5 most dangerous states"
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a really good data scientist."},
        {"role": "user", "content": Instructions},
        {"role": "user", "content": query_text},
        {"role": "user", "content": "Run the python code query and return the result."}
        ]
    )

print(completion.choices[0].message.content)

text = (completion.choices[0].message.content)


# This converts the data frame into sentences in a text file so that Chat GPT can correctly read the data.
# https://saturncloud.io/blog/how-to-write-a-pandas-dataframe-to-a-txt-file/
df.to_csv('stateinfo.txt', sep='\t', index=False)

# This finally converts the query into python code.
Instructions = "The text information represents data about U.S. States. A higher total score is better. For the other variables like 'Safety', a lower score is better."
query_text = "Write a summary and indicate which 5 states are the most dangerous. Then make a short summary of each of the 5 states on there characteristics shown in the other columns."
stateinfo = open('stateinfo.txt', 'r').read()
completion = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": "You are a really good marketer."},
        {"role": "user", "content": Instructions},
        {"role": "user", "content": stateinfo},
        {"role": "user", "content": query_text},
        ]
    )

# I didn't find the directions online.
# This query would be important from a marketing perspective if this was a home security company.
# A home security company is wanting to predict their most profitable markets to expand into. They would look at this list choose one of the most dangerous states.
# Additionally, it explains the other characteristics of the states like a market profile.
# You could draw marketing conclusions from these profiles like the less affordable states will be more affluent to afford a security systems.
# Other characteristics can help create marketing strategies that would fit that state citizen. 
# The company would of course, need more demographic information from the people in that states and create customer personas, but this is a start.

print(completion.choices[0].message.content)

text = (completion.choices[0].message.content)


file_handle = open('output4.txt', 'w+')
file_handle.write(text)
file_handle.close()






