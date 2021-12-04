import numpy as np
import json
from scipy import stats
from filter_books import authors_c
from filter_books import non_fiction

with open('books_json.txt','r') as file:
    books = json.load(file)

books_f = {}

for name, books_dict in books.items():
    if (name.split("___")[1] not in non_fiction) & (name.split("___")[0] in authors_c) & (len(books_dict['characters']) > 5):
        if (int(books_dict['author_year']) >= 1800) & (int(books_dict['author_year']) <= 1950):
            books_f[name] = books_dict 

male_char_count_m = []
female_char_count_m = []
male_occ_count_m = []
female_occ_count_m = []
male_pro_count_m = []
female_pro_count_m = []

male_char_count_f = []
female_char_count_f = []
male_occ_count_f = []
female_occ_count_f = []
male_pro_count_f = []
female_pro_count_f = []

for name, books_dict in books_f.items():
    if books_dict['author_male?'] == True:
        male_char_count_m.append(books_dict['character_count']['male'])
        female_char_count_m.append(books_dict['character_count']['female'])
        male_occ_count_m.append(books_dict['character_occurrence_count']['male'])
        female_occ_count_m.append(books_dict['character_occurrence_count']['female'])
        male_pro_count_m.append(books_dict['pronouns_count']['male'])
        female_pro_count_m.append(books_dict['pronouns_count']['female'])
    else:
        male_char_count_f.append(books_dict['character_count']['male'])
        female_char_count_f.append(books_dict['character_count']['female'])
        male_occ_count_f.append(books_dict['character_occurrence_count']['male'])
        female_occ_count_f.append(books_dict['character_occurrence_count']['female'])
        male_pro_count_f.append(books_dict['pronouns_count']['male'])
        female_pro_count_f.append(books_dict['pronouns_count']['female'])

h2_p1 = stats.ttest_ind(female_char_count_f, female_char_count_m, equal_var=False, alternative = 'greater')[1]
h2_p2 = stats.ttest_ind(female_occ_count_f, female_occ_count_m, equal_var=False, alternative = 'greater')[1]
h2_p3 = stats.ttest_ind(female_pro_count_f, female_pro_count_m, equal_var=False, alternative = 'greater')[1]

print("\nFemale Character Count \n")
print("Mean in Male-Authored Books: ", round(np.mean([x for x in female_char_count_m if x < np.percentile(female_char_count_m,99)]),0))
print("Mean in Female-Authored Books: ", round(np.mean([x for x in female_char_count_f if x < np.percentile(female_char_count_f,99)]),0))
print("\nAlternative Hypothesis: Mean of Female Character Count in female-authored books is greater than that in male-authored books")
print("p value, one-sided independent t-test: ", h2_p1)
print("---------------------------------------------------------------")
print("Female Character Occurrence Count \n")
print("Mean in Male-Authored Books: ", round(np.mean([x for x in female_occ_count_m if x < np.percentile(female_occ_count_m,99)]),0))
print("Mean in Female-Authored Books: ", round(np.mean([x for x in female_occ_count_f if x < np.percentile(female_occ_count_f,99)]),0))
print("\nAlternative Hypothesis: Mean of Female Character Occurrence Count in female-authored books is greater than that in male-authored books")
print("p value, one-sided independent t-test: ", h2_p2)
print("---------------------------------------------------------------")
print("Female Pronoun Count \n")
print("Mean in Male-Authored Books: ", round(np.mean([x for x in female_pro_count_m if x < np.percentile(female_pro_count_m,99)]),0))
print("Mean in Female-Authored Books: ", round(np.mean([x for x in female_pro_count_f if x < np.percentile(female_pro_count_f,99)]),0))
print("\nAlternative Hypothesis: Mean of Female Pronoun Count in female-authored books is greater than that in male-authored books")
print("p value, one-sided independent t-test: ", h2_p3, "\n")

h2_p4 = stats.ttest_ind(male_char_count_f, male_char_count_m, equal_var=False, alternative = 'two-sided')[1]
h2_p5 = stats.ttest_ind(male_occ_count_f, male_occ_count_m, equal_var=False, alternative = 'two-sided')[1]
h2_p6 = stats.ttest_ind(male_pro_count_f, male_pro_count_m, equal_var=False, alternative = 'two-sided')[1]

print("*******************************************************************************************************************************\n")
print("\nMale Character Count \n")
print("Mean in Male-Authored Books: ", round(np.mean([x for x in male_char_count_m if x < np.percentile(male_char_count_m,99)]),0))
print("Mean in Female-Authored Books: ", round(np.mean([x for x in male_char_count_f if x < np.percentile(male_char_count_f,99)]),0))
print("\nNull Hypothesis: Mean of Male Character Count in female-authored books is same as that in male-authored books")
print("p value, one-sided independent t-test: ", h2_p4)
print("---------------------------------------------------------------")
print("Male Character Occurrence Count \n")
print("Mean in Male-Authored Books: ", round(np.mean([x for x in male_occ_count_f if x < np.percentile(male_occ_count_f,99)]),0))
print("Mean in Female-Authored Books: ", round(np.mean([x for x in male_occ_count_f if x < np.percentile(male_occ_count_f,99)]),0))
print("\nNull Hypothesis: Mean of Male Character Occurrence Count in female-authored books is same as that in male-authored books")
print("p value, one-sided independent t-test: ", h2_p5)
print("---------------------------------------------------------------")
print("Male Pronoun Count \n")
print("Mean in Male-Authored Books: ", round(np.mean([x for x in male_pro_count_m if x < np.percentile(male_pro_count_m,99)]),0))
print("Mean in Female-Authored Books: ", round(np.mean([x for x in male_pro_count_f if x < np.percentile(male_pro_count_f,99)]),0))
print("\nNull Hypothesis: Mean of Male Pronoun Count in female-authored books is same as that in male-authored books")
print("p value, one-sided independent t-test: ", h2_p6, "\n")