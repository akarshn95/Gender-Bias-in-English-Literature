import numpy as np
import json
from scipy import stats
from filter_books import authors_c
from filter_books import non_fiction

with open('books_json_y_70.txt','r') as file:
    books = json.load(file)

books_f = {}

for name, books_dict in books.items():
    if (name.split("___")[1] not in non_fiction) & (name.split("___")[0] in authors_c) & (len(books_dict['characters']) > 5):
        if (int(books_dict['author_year']) >= 1800) & (int(books_dict['author_year']) <= 1950):
            books_f[name] = books_dict 

male_char_count = []
female_char_count = []
male_occ_count = []
female_occ_count = []
male_pro_count = []
female_pro_count = []

for name, books_dict in books_f.items():
    male_char_count.append(books_dict['character_count']['male'])
    female_char_count.append(books_dict['character_count']['female'])
    male_occ_count.append(books_dict['character_occurrence_count']['male'])
    female_occ_count.append(books_dict['character_occurrence_count']['female'])
    male_pro_count.append(books_dict['pronouns_count']['male'])
    female_pro_count.append(books_dict['pronouns_count']['female'])

h1_p1 = stats.ttest_ind(male_char_count, female_char_count, equal_var=False)[1]/2
h1_p2 = stats.ttest_ind(male_occ_count, female_occ_count, equal_var=False)[1]/2
h1_p3 = stats.ttest_ind(male_pro_count, female_pro_count, equal_var=False)[1]/2

print("\nCharacter Count\n")
print("Mean Male Count:", round(np.mean(male_char_count),0))
print("Mean Female Count: ", round(np.mean(female_char_count),0))
print("\nNull Hypothesis: Mean of Male Character Count is greater than that of Female Character Count")
print("p value, one-sided independent t-test: ", h1_p1)
print("---------------------------------------------------------------")
print("Character Occurrence Count \n")
print("Mean Male Count: ", round(np.mean(male_occ_count),0))
print("Mean Female Count: ", round(np.mean(female_occ_count),0))
print("\nNull Hypothesis: Mean of Male Character Occurrence Count is greater than that of Female Character Occurrence Count")
print("p value, one-sided independent t-test: ", h1_p2)
print("---------------------------------------------------------------")
print("Pronoun Count \n")
print("Mean Male Pronoun Count: ", round(np.mean(male_pro_count),0))
print("Mean Female Pronoun Count: ", round(np.mean(female_pro_count),0))
print("\nNull Hypothesis: Mean of Male Pronoun Count is greater than that of Female Pronoun Count")
print("p value, one-sided independent t-test: ", h1_p3, "\n")