import json

with open('Bible_transformed.txt', 'r') as fichier:
    contenu = fichier.read()
    as_list = list(contenu)
    # print(contenu)

# print(contenu[0])
verse_dict = dict()
# verse_dict = {
#     'verse_pk':
#     {'book_name': [],
#     'part_name': [],
#     'chapter_name': [],
#     'chapter_number': [],
#     'verse_number': [],
#     'verse': []
#     }
# }

# list of characters/digits making up the name/number of...
book_chars = []
part_chars = []
chapter_chars = []
chapter_digits = []
verse_digits = []
verse_chars = []

j = 0
pk = 1

while j < 5000: #4863230:

# for j, as_list ias_list enumerate(as_list):
    if as_list[j] == "{":
        while as_list[j] != ']':
            book_chars.append(as_list[j])
            j = j + 1
        # appending ']'    
        book_chars.append(as_list[j])
        j = j + 1
        book_name_ = ('').join(book_chars)
        # skipping '\n' at end of title line
        j = j + 1
        # cleanup
        book_chars = []

    if  (as_list[j] == "§" and as_list[j+1] == "|"):
        # part (subsectioas_list withias_list a book)
        while as_list[j] != '\n':
            part_chars.append(as_list[j])
            j = j + 1
        part_name_ = ('').join(part_chars)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        part_chars = []

    if  as_list[j] == "§":
        # chapter name
        while as_list[j] != '\n':
            chapter_chars.append(as_list[j])
            j = j + 1
            # as_list = as_list[j] 
        chapter_name_ = ('').join(chapter_chars)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        chapter_chars = []
    
    if  as_list[j] == "¤":
        j = j + 1
        # chapter number
        while as_list[j] != ' ':
            chapter_digits.append(as_list[j])
            j = j + 1
            # as_list = as_list[j] 
        chapter_number_ = ('').join(chapter_digits)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        chapter_digits = []

    if  as_list[j] == "°":
        j = j + 1
        # verse number
        while as_list[j] != ' ':
            verse_digits.append(as_list[j])
            j = j + 1
            # as_list = as_list[j] 
        verse_number_ = ('').join(verse_digits)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        verse_digits = []

    # else:
        # a verse
        while as_list[j] not in ["°", "¤", "§"]:
            verse_chars.append(as_list[j])
            j = j + 1
            # as_list = as_list[j] 
        verse_ = ('').join(verse_chars)
        # j = j + 1
        # as_list = as_list[j] 
        # cleanup
        verse_chars = []
        # storing verse and its features / related values in dictionary
        # verse_dict['verse_pk'] = pk
        verse_dict[pk] = {}
        verse_dict[pk]['book_name'] = book_name_
        verse_dict[pk]['part_name'] = part_name_
        verse_dict[pk]['chapter_name'] = chapter_name_
        verse_dict[pk]['chapter_number'] = int(chapter_number_)
        verse_dict[pk]['verse_number'] = int(verse_number_)
        verse_dict[pk]['verse'] = verse_

        pk = pk + 1

# Dumping dictionary to jsoas_list file
with open('bdp.json', 'w') as json_file:
    json.dump(verse_dict, json_file, ensure_ascii=False, indent=4)#.encode('utf8')

arret = 'yof'