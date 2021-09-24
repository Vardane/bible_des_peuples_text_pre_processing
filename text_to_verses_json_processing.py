import json


with open('Mt_verses.txt', 'r') as fichier:
    contenu = fichier.read()
    as_list = list(contenu)
    print(contenu)


verse_dict = dict()

fragment_chars = []
verse_digits = []
verse_chars = []

j = 0
pk = 1

# while j < 137494: # 4861867: #4863230: #133813:#< 4863230:
for j in range(138769):

    if  as_list[j] == "§":
        ignore_one_more = 0
        if as_list [j+1] == ' ':
            # if space after §, then need to ignore an additional 
            # character before storing title
            ignore_one_more = 1 
        # fragment title
        while as_list[j] != '\n':
            fragment_chars.append(as_list[j])
            j = j + 1    
            # as_list = as_list[j]
        # number of characters to skip before actual title starts
        skip_char_count = 1 + ignore_one_more 
        fragment_title_ = ('').join(fragment_chars[skip_char_count:])
        j = j + 1
        # cleanup
        fragment_chars = []
    

    elif  as_list[j] == "°":
        # skipping the superscript round 
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
        # if book_name_ == 'LE CANTIQUE DES CANTIQUES':
        #     # RESUME HERE: NEED TO HANDLE THE OPTIONAL INDICATIONS: '|ELLE', '|LUI' etc.
        try:
            while ( as_list[j] not in ["°", "§"]):
                        # or 
                        # (
                        #     # case when an alternative verse number is 
                        #     # inserted in verse (e.g.: "{14c}")
                        #     as_list[j] == "{"
                        #     and
                        #     as_list[j+1].isnumeric()
                        # )
        #                 or
        #                 # handling indication of who speaks in Cantique des Cantiques
        #                 ( 

        #                 )
                # ):
                if (as_list[j] != '|'):
                    verse_chars.append(as_list[j])
                j = j + 1



        except IndexError as err_msg:
            print(f'{err_msg}; index j = {j}')

        verse_ = ('').join(verse_chars)
        verse_chars = []

        # storing verse and its features / related values in dictionary

        verse_dict[pk] = {}
        verse_dict[pk]['fragment_title'] = fragment_title_

        try:
            verse_dict[pk]['verse_number'] = int(verse_number_)
        except ValueError as erreur:
            print(f'verse number error: {erreur} at verse with pk {pk}')
            verse_dict[pk]['verse_number'] = verse_number_
        verse_dict[pk]['verse'] = verse_

        print(f'Verse number {verse_number_} in fragment {fragment_title_} \
        has been processed.' )
        print(f'We are at character {j}')

        pk = pk + 1

print(f'halte du traitement; prochain verset: {pk}')

# Dumping dictionary to jsoas_list file
with open('Mt.json', 'w') as json_file:
    json.dump(verse_dict, json_file, ensure_ascii=False, indent=4)#.encode('utf8')

arret = 'yof'
