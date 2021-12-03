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

char_count = [[] for _ in range(6)]
char_occ_count = [[] for _ in range(6)]
char_pro_count = [[] for _ in range(6)]

for name, books_dict in books_f.items():  
    year = books_dict['author_year']
    cc_ratio = books_dict['character_count']['male']/(books_dict['character_count']['male'] + books_dict['character_count']['female'])
    co_ratio = books_dict['character_occurrence_count']['male']/(books_dict['character_occurrence_count']['male'] + books_dict['character_occurrence_count']['female'])
    po_ratio = books_dict['pronouns_count']['male']/(books_dict['pronouns_count']['male'] + books_dict['pronouns_count']['female'])
    
    if year >= 1800 and year < 1825:
        char_count[0].append(cc_ratio)
        char_occ_count[0].append(co_ratio)
        char_pro_count[0].append(po_ratio)
    elif year >= 1825 and year < 1850:
        char_count[1].append(cc_ratio)
        char_occ_count[1].append(co_ratio)
        char_pro_count[1].append(po_ratio)
    elif year >= 1850 and year < 1875:
        char_count[2].append(cc_ratio)
        char_occ_count[2].append(co_ratio)
        char_pro_count[2].append(po_ratio)
    elif year >= 1875 and year < 1900:
        char_count[3].append(cc_ratio)
        char_occ_count[3].append(co_ratio)
        char_pro_count[3].append(po_ratio)
    elif year >= 1900 and year < 1925:
        char_count[4].append(cc_ratio)
        char_occ_count[4].append(co_ratio)
        char_pro_count[4].append(po_ratio)
    elif year >= 1925 and year <= 1950:
        char_count[5].append(cc_ratio)
        char_occ_count[5].append(co_ratio)
        char_pro_count[5].append(po_ratio)

year_dict = {
    0: 1825,
    1: 1850,
    2: 1875,
    3: 1900,
    4: 1925,
    5: 1950
}

print("\nProportion of Male Character Count\n")
print(f"Mean in 1825: {round(np.mean(char_count[0]),2)}")
print("Null Hypothesis: The proportion of Male Character Count to total Character Count is greater in each of the below years compared to 1825\n")

for i in range(1,len(char_count)):
    p = stats.ttest_ind(char_count[i], char_count[0], equal_var=False, alternative = 'greater')[1]
    print(f"Mean in {year_dict[i]}: {round(np.mean(char_count[i]),2)}; p-value: {p}")

print("\nProportion of Male Character Occurrence Count\n")
print(f"Mean in 1825: {round(np.mean(char_occ_count[0]),2)}")
print("Null Hypothesis: The proportion of Male Character Occurrence Count to total Character Occurrence Count is greater in each of the below years compared to 1825\n")

for i in range(1,len(char_occ_count)):
    p = stats.ttest_ind(char_occ_count[i], char_occ_count[0], equal_var=False, alternative = 'greater')[1]
    print(f"Mean in {year_dict[i]}: {round(np.mean(char_occ_count[i]),2)}; p-value: {p}")

print("\nProportion of Male Pronoun Count\n")
print(f"Mean in 1825: {round(np.mean(char_pro_count[0]),2)}")
print("Null Hypothesis: The proportion of Male Pronoun Count to total Pronoun Count is greater in each of the below years compared to 1825\n")

for i in range(1,len(char_pro_count)):
    p = stats.ttest_ind(char_pro_count[i], char_pro_count[0], equal_var=False, alternative = 'greater')[1]
    print(f"Mean in {year_dict[i]}: {round(np.mean(char_pro_count[i]),2)}; p-value: {p}")

print("\n")