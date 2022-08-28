# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
alphabet_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato_list():
    word = input("Enter a word: ").upper()
    # print(word_list)
    try:
        phonetic_list = [alphabet_dict[letter] for letter in word ]
    except KeyError:
        print("Sorry, only letter in alphabet are accepted")
        nato_list()
    else:
        print(phonetic_list)


nato_list()