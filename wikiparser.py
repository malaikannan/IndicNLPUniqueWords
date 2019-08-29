import re
import csv
import os
import argparse
from bloomfilter import BloomFilter 

class wikiparser:

    def __init__(self,wiki_dump_path,csv_file_path,bloomfilter_file_path,lower_unicode_value,upper_unicode_value):
        self.wiki_dump_path = wiki_dump_path
        self.csv_file_path = csv_file_path
        self.bloomfilter_file_path = bloomfilter_file_path
        self.lower_unicode_value = lower_unicode_value
        self.upper_unicode_value = upper_unicode_value


    @classmethod
    def is_tamil(self,word,lower_unicode_value,upper_unicode_value):
        first_char = word[:1]
        lang_number = ord(first_char)
        if lang_number >=int(lower_unicode_value) and lang_number <=int(upper_unicode_value):
            return True

    def create_csv_bloomfilter_files(self):
        items_count = len(self.dict_tamil_word) 
        falsepositive_probability = 0.001
        bloomf = BloomFilter(items_count,falsepositive_probability) 

        with open(self.csv_file_path,"w") as f:
            for word,count in self.dict_tamil_word.items():
                write_line = word + "," + str(count) + os.linesep
                bloomf.add(word)
                f.write(write_line)

        bloomf.writetofile(self.bloomfilter_file_path)



    def parse_folders(self):

        self.dict_tamil_word = {}

        for root, dirs, files in os.walk(self.wiki_dump_path):
            for file in files:
                if "wiki" in file:
                    with open(os.path.join(root,file),'r') as xml_file:
                        for line in xml_file.readlines():
                            line = re.sub("[!@#$%&*.,<>:;|]", '', line)
                            line = line.replace('"'," ")
                            split_line = line.split(" ")
                            for word in split_line:
                                try:
                                    if(self.is_tamil(word,self.lower_unicode_value,self.upper_unicode_value)):
                                        if word not in self.dict_tamil_word :
                                            self.dict_tamil_word [word.strip()] = 1
                                        else:
                                            self.dict_tamil_word [word.strip()] = self.dict_tamil_word [word.strip()] + 1  
                                except:
                                    pass
        print("Number of unique words is",len(self.dict_tamil_word ))




parser = argparse.ArgumentParser()
parser.add_argument('--wiki_dump_path')
parser.add_argument('--csv_file_path')
parser.add_argument("--bloomfilter_file_path")
parser.add_argument("--lower_unicode_value")
parser.add_argument("--upper_unicode_value")
results = parser.parse_args()

parser = wikiparser(results.wiki_dump_path,results.csv_file_path,results.bloomfilter_file_path,results.lower_unicode_value,results.upper_unicode_value)
parser.parse_folders() 
parser.create_csv_bloomfilter_files()


#Sample execution statement
# python3 wikiparser.py --wiki_dump_path "/home/ANANT/msankarasubbu/Documents/Work/opensource/Data" --csv_file_path "/home/ANANT/msankarasubbu/Documents/Work/opensource/Data/tamil_words.csv"  --bloomfilter_file_path "/home/ANANT/msankarasubbu/Documents/Work/opensource/Data/tamil_words_filter.txt" --lower_unicode_value 2944 --upper_unicode_value 3071 


       


   