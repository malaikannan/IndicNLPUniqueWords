import re
import csv
import os
import argparse

def is_tamil(word):
    first_char = word[:1]
    lang_number = ord(first_char)
    if lang_number >=int(lower_unicode_value) and lang_number <=int(upper_uniocde_value):
        return True

def write_dict_csv(dict_tamil_word,file_name):
    with open(file_name,"w") as f:
        for word,count in dict_tamil_word.items():
            write_line = word + "," + str(count) + os.linesep
            f.write(write_line)


def parse_folders(folder_path,csv_file_path):
    print(folder_path)
    dict_tamil_word = {}
    print(lower_unicode_value)
    print(upper_uniocde_value)

    for root, dirs, files in os.walk(folder_path):
        print('Found directory: %s' % root)
        for file in files:
            if "wiki" in file:
                print("processing file",file)
                with open(os.path.join(root,file),'r') as xml_file:
                    for line in xml_file.readlines():
                        line = re.sub("[!@#$%&*.,<>:;|]", '', line)
                        line = line.replace('"'," ")
                        split_line = line.split(" ")
                        for word in split_line:
                            try:
                                if(is_tamil(word)):
                                    if word not in dict_tamil_word:
                                        dict_tamil_word[word.strip()] = 1
                                    else:
                                        dict_tamil_word[word.strip()] = dict_tamil_word[word.strip()] + 1  
                            except:
                                pass
    print("Number of unique words is",len(dict_tamil_word))
    write_dict_csv(dict_tamil_word,csv_file_path)


parser = argparse.ArgumentParser()
parser.add_argument('--wiki_dump_path')
parser.add_argument('--csv_file_path')
parser.add_argument("--lower_unicode_value")
parser.add_argument("--upper_unicode_value")
results = parser.parse_args()
global lower_unicode_value, upper_uniocde_value 
lower_unicode_value = results.lower_unicode_value
upper_uniocde_value = results.upper_unicode_value
parse_folders(results.wiki_dump_path,results.csv_file_path)

#Sample execution statement
# python3 wikiparser.py --wiki_dump_path "/Users/malaikannan/Documents/Work/opensource/TamilData" --csv_file_path "/Users/malaikannan/Documents/Work/opensource/TamilData/tamil_words.csv" --lower_unicode_value 2944 --upper_unicode_value 3071 


       


   