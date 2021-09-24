import json


with open('hebreux.txt', 'r') as fichier:
# with open('Bible_transformed.txt', 'r') as fichier:
# with open('essai.txt', 'r') as fichier:
    contenu = fichier.read()
    as_list = list(contenu)
    print(contenu)

# print(contenu[0])
verse_dict = dict()
# verse_dict = {
#     'verse_pk':
#     {'book_name': [],
#     'part_name': [],
#     'section_name': [],
#     'chapter_number': [],
#     'verse_number': [],
#     'verse': []
#     }
# }

# list of characters/digits making up the name/number of...
book_chars = []
diminutive_chars = []
part_chars = []
section_chars = []
chapter_digits = []
verse_digits = []
verse_chars = []
indication = []


# initializing optional indication to none
optional_indication_ = None

j = 0
pk = 1

while j < 4861867: #4863230: #133813:#< 4863230:

    if (as_list[j] == "[" and as_list[j+1] == "{"):
        while as_list[j] != '}':
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

    elif  (as_list[j] == "[" and as_list[j+3] == "]"):
        # book diminutive
        while as_list[j] != '\n':
            diminutive_chars.append(as_list[j])
            j = j + 1
        book_diminutive_ = ('').join(diminutive_chars)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        diminutive_chars = []


    elif  (as_list[j] == "§" and as_list[j+1] == "|"):
        # part (subsectioas_list withias_list a book)
        while as_list[j] != '\n':
            part_chars.append(as_list[j])
            j = j + 1
        part_name_ = ('').join(part_chars)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        part_chars = []

    elif  as_list[j] == "§":
        # section name (may be the name of a chapter or 
        # the name of a subsection in a chapter)
        while as_list[j] != '\n':
            section_chars.append(as_list[j])
            j = j + 1    
            # as_list = as_list[j] 
        section_name_ = ('').join(section_chars)
        j = j + 1
        if as_list[j] == '\n':
            # case when there is an empty line below the section name
            # so two '\n' in a row
                j = j + 1
        if ( as_list[j] == '|' and as_list[j+1].isupper() ):
            # case when an optional indication immediately follows a section name
            j = j + 1
            while as_list[j] != '\n':
                indication.append(as_list[j])
                j = j + 1
                # as_list = as_list[j] 
            optional_indication_ = ('').join(indication)
            j = j + 1
            # as_list = as_list[j] 
            # cleanup
            indication = []
        # cleanup
        section_chars = []
    
    elif as_list[j] == "¤":
        j = j + 1
        # chapter number
        while as_list[j] not in [' ', '\n', '\t']:
            chapter_digits.append(as_list[j])
            j = j + 1
            # as_list = as_list[j] 
        chapter_number_ = ('').join(chapter_digits)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        chapter_digits = []

    elif  ( as_list[j] == "|" and as_list[j+1].isupper() ):
        # Indications such as '|ELLE' in Cantique des cantiques
        j = j + 1
        # chapter number
        while as_list[j] != '\n':
            indication.append(as_list[j])
            j = j + 1
            # as_list = as_list[j] 
        optional_indication_ = ('').join(indication)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        indication = []

    elif (as_list[j] == "P" and as_list[j+1] == "S" and 
        # Removing PSAUME indication in front of chapter / psalm number
        # Indication can always been added back before chapter number in online version
        # using the condition 'book_name' == 'PSAUMES'
        as_list[j+2] == "A" and as_list[j+3] == "U" and 
        as_list[j+4] == "M" and as_list[j+5] == "E" and
        as_list[j+6] == " " and as_list[j+7] == "¤"):
        j = j+7

        # copy paste from chapter number processing (consider coding functions...)
        j = j + 1
        # chapter number
        while as_list[j] not in [' ', '\n', '\t']:
            chapter_digits.append(as_list[j])
            j = j + 1
            # as_list = as_list[j] 
        chapter_number_ = ('').join(chapter_digits)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        chapter_digits = []

    elif  as_list[j] == "°":
        j = j + 1
        # verse number
        while as_list[j] not in [' ', '\t', '|']:
            verse_digits.append(as_list[j])
            j = j + 1
            # as_list = as_list[j] 
        verse_number_ = ('').join(verse_digits)
        j = j + 1
        # as_list = as_list[j] 
        # cleanup
        verse_digits = []

        # a verse
        # special case: Cantique des cantiques
        if book_name_ == 'LE CANTIQUE DES CANTIQUES':
            # RESUME HERE: NEED TO HANDLE THE OPTIONAL INDICATIONS: '|ELLE', '|LUI' etc.
            try:
                while ( as_list[j] not in ["°", "¤", "§", "{"]
                        or 
                        (
                            # case when an alternative verse number is 
                            # inserted in verse (e.g.: "{14c}")
                            as_list[j] == "{"
                            and
                            as_list[j+1].isnumeric()
                        )
                        or
                        # handling indication of who speaks in Cantique des Cantiques
                        ( 

                        )
                    ):
                    if (as_list[j] != '|'):
                        verse_chars.append(as_list[j])
                        j = j + 1



            except IndexError as err_msg:
                print(f'{err_msg}; index j = {j}')
        else:
            try:
                while ( as_list[j] not in ["°", "¤", "§", "{"]
                        or 
                        (
                            # case when an alternative verse number is 
                            # inserted in verse (e.g.: "{14c}")
                            as_list[j] == "{"
                            and
                            as_list[j+1].isnumeric()
                        )
                        or
                        # handling indication of who speaks in Cantique des Cantiques
                        ( 

                        )
                    ):
                    verse_chars.append(as_list[j])
                    j = j + 1
            except IndexError as err_msg:
                print(f'{err_msg}; index j = {j}')
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
        verse_dict[pk]['book_diminutive'] = book_diminutive_
        verse_dict[pk]['part_name'] = part_name_
        verse_dict[pk]['section_name'] = section_name_
        verse_dict[pk]['optional_indication'] = optional_indication_
        try:
            verse_dict[pk]['chapter_number'] = int(chapter_number_)
        except ValueError as erreur:
            print(f'chapter number error: {erreur} at verse with pk {pk}')
            verse_dict[pk]['chapter_number'] = chapter_number_
        try:
            verse_dict[pk]['verse_number'] = int(verse_number_)
        except ValueError as erreur:
            print(f'verse number error: {erreur} at verse with pk {pk}')
            verse_dict[pk]['verse_number'] = verse_number_
        verse_dict[pk]['verse'] = verse_

        print(f'Verse number {verse_number_} in chapter {chapter_number_} \
        in book {book_name_} has been processed.' )
        print(f'We are at character {j}')

        pk = pk + 1

    # print(f'cycle terminé; prochain verset: {pk}')
    # sentence = ''   
    # for k in range (-30, 1):
    #     sentence = ('').join([sentence, as_list[j+k]])
    # print(sentence)

print(f'halte du traitement; prochain verset: {pk}')

# Dumping dictionary to jsoas_list file
with open('hebreux.json', 'w') as json_file:
    json.dump(verse_dict, json_file, ensure_ascii=False, indent=4)#.encode('utf8')

arret = 'yof'