# -*- coding: utf-8 -*-

# SI 507 - Homework 4
# Note the changed name (Lab -> Homework)

# Instructions all provided in this file.
# IMPORTANT: Please read ALL of the instructions for each part before starting on it.

# Submit this edited code file (only) to HW 4 on Gradescope via Canvas to see test results!

## Your import statements for use in the program (both things installed wih pip & things that come default with Python) should go here!
import pandas as pd
import csv
from datetime import datetime
import numpy as np
import random
import string
import itertools


#####################

## [PART 1]
# Provided is a dataset: movies_dataset_group.csv
# Your first goal is to write code to "clean" this dataset a little bit and produce a cleaned version of the dataset in a file called movies_clean.csv.

# NOTE that there are MANY ways to clean up a dataset programmatically. Many common ways will use a module to do so -- pandas is a common one.
# If you take SI 618, you will use/are using the Pandas module in that course! You are welcome to use that here. (Just make sure you indicate in imports and requirements everything you need.)
# However, you do not NEED to use Pandas to do this. Think carefully about what it is you need to achieve for these specific goals, and then try some things out.
# You MAY (but do NOT have to) use any of the following modules, but NOT others, for this particular lab:
# pandas, xlrd, scipy, numpy
# HINT: The CSV module (built into Python) is probably going to be very useful , and using list and/or dictionary methods may also be useful!

# The following things should be true of movies_clean.csv:

# - Every missing cell should no longer be blank -- instead, anything missing should contain the string "NA"
## NOTE: "Not Rated" IS information about rating, and should remain; don't get rid of that information.

# - Dates should be considered missing (and become "NA" values) if they are not in the format DD-Month-YY (e.g. 23-Apr-98). Any date in the format D-Month-YY (e.g. 3-Apr-94) should have a 0 at the front.
### ***NOTE - it is possible for a starting 0 to exist and not show up in certain display options/software -- so if it's not showing up and you're SURE it's there, test by opening the .CSV in a text editor or the command prompt first!

# You may achieve these goals and create movies_clean.csv in any way you like, as long as it's done with Python code.

# Tests for this part are testing movies_clean.csv, which *should have been generated by the program* -- do NOT submit that file, only submit your program file.

csv_file = "movies_dataset_group.csv"
df = pd.read_csv(csv_file)
df["Release Date"] = pd.to_datetime(df["Release Date"], format = '%d-%b-%y', errors='coerce')
df["Release Date"] = df["Release Date"].dt.strftime('%d-%b-%y')
df.replace({'NaT': 'NA'}, inplace=True)
df = df.fillna(value='NA')
df.to_csv('movies_clean.csv')

## [PART 2]

# If you take all the movie ratings available in the dataset (G, PG, PG-13, R, NC-17 .. do not count Not Rated movies here) -- what is the *median* rating of the rated movies? Save the result in a variable median_rating (whose value should be a string representing a rating, e.g. "G" or "PG-13" or "R" or whatever it is).

# To do this, you should convert the ratings to numbers,  starting at 1 for G rating and counting up (1,2,3,4,5), where 5 represents NC-17.
# HINT: Creating a dictionary may be useful in this process!
# If you find that the median result is a decimal in between two of these integers, round to the closest one to find your answer. (And if you do not know what a median is, check this out: https://en.wikipedia.org/wiki/Median )


# You may use one of the modules listed in part 1 to help you with this, but you do not necessarily need to.

# Use code to compute this (by opening the data file and manipulating the data in some way) and to assign the median_rating variable correctly, which we will test.

# G = 1
# PG = 2
# PG-13 = 3
# R = 4
# NC-17 = 5

## Create a dictionary of rating
rating = {1:'G', 2:'PG', 3:'PG-13', 4:'R', 5:'NC-17'}
## Replace the original rating with number 1 to 5
df['MPAA Rating'] = df['MPAA Rating'].replace({'G':1, 'PG':2, 'PG-13':3, 'R':4, 'NC-17':5})

## Create a list of all the validate rating
rating_list = []
for r in df['MPAA Rating']:
    if r in [1,2,3,4,5]:
        rating_list.append(r)
# print(rating_list)
## Use numpy.median(list) to get the median
median_rating_int = np.median(rating_list)
# print(median_rating_int)
## Conver back to string
median_rating = rating[median_rating_int]
# print(median_rating)


## [PART 3]
# We want to play a "game" (sort of) about making up new movies. Use the itertools library and the clean movies_clean.csv data you've created to have your program repeatedly create 10 new movie titles and ratings, print them out neatly (see below for an example), and save a string with all of them (like below) in a variable called sample_fake_movies.

# NOTE that this part of the lab may NOT be graded entirely by tests (it may be sat least partially graded by humans). So you should make sure you test it yourself to see that it does what it should.

# We're grading on whether you achieved the objectives listed below for the results of running this program.

# Requirements:
# - The 10 fake movie titles & ratings this game prints out should differ in some way each time you run the program -- e.g. randomness (via the random library, perhaps?) should be introduced somewhere.
# - Each of your new movie titles should be no more than six words long OR no more than 45 characters long. (Pick either one of those two constraints.)
# - The resulting string saved in sample_fake_movies should have at least 10 lines, and each line should have 1 movie title and rating in it -- no blank lines. See the EXAMPLE below for formatting guidelines/example.
# - This "game" should be something that happens on running this program -- it should NOT be something that depends on any user input. (A file with user input won't run in Gradescope!)
# - Combination of information must be more creative than existing movie titles with new ratings. Think along the lines of mixing up words in movie titles somehow. (It's OK if they don't make sense to us humans!)
# At least one tool/function from the itertools library must be used.
# It is okay to use more than one itertools function in different ways, or to create more than 10 movies on each run, but each time, at least 10 new movies + ratings must be created and printed.

# For example, here's one of millions of possible/reasonable outputs in the below string. The value of your sample_fake_movies variable should be something like this:

"""
Say Seabiscuit - G
The Real Romeo - R
Rescue American The - PG-13
Damned Queen of the - PG
Perrier's Peter - R
Getaway I Pink You The Once - PG
Eleven Twelve Thirteen - PG-13
Wild Novocaine - PG
My With the of Why Narc Into - Not Rated
My My My The - G
"""

print("\n\nNEW FAKE MOVIE TITLES CREATED BELOW...\n\n")
# Write your code to enact all of this below

## Create a list of words from Title
words_lst = []
## read csv file
with open('movies_clean.csv', newline='') as csvfile:
    row_reader = csv.reader(csvfile)
    for row in row_reader:
        words_lst = words_lst + row[1].split(" ")
words_lst.remove('Title')
# print(words_lst)


## Generate a random rating
def generate_a_rating():
    rating = ['G', 'PG','PG-13','R','NC-17','Not Rated'] ## Create a list of rating
    fake_movies_rating = random.choice(rating) ## Randomly choose a rating from list
    return fake_movies_rating

# print(generate_a_rating())


## Generate a random movie name
def generate_a_movie_name():
    length_movie_name = random.choice([1,2,3,4,5,6]) ## Generate a random length of the movie name
    fake_movies_lst = random.choices(words_lst, k = length_movie_name) ## Pick words from word_lst randomly
    fake_movies_name = itertools.combinations(fake_movies_lst, length_movie_name) ## With the choosen word, generate the movie name with combinations method
    ## The type of fake_moives_name is <class 'itertools.combinations'>
    ## So here I convert the tuple to string
    for i in list(fake_movies_name):
        fake_movies_name_str = ' '.join(i)
    return fake_movies_name_str

# print(generate_a_movie_name())


## Output
sample_fake_movies = ""
for i in range(10):
    sample_fake_movies += generate_a_movie_name() + " - " + generate_a_rating() + "\n"

print(sample_fake_movies)
