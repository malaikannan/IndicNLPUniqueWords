# IndicNLPParser
Indic NLP Unique Words

Program is meant to get unique list of words and the frequency in which it has occurred in Wikipedia. 

1. For Tamil get the latest dump from  http://dumps.wikimedia.org/tawiki/latest/ . Telugu will be like  http://dumps.wikimedia.org/tewiki/latest/
2. File to be downloaded is tawiki-latest-pages-articles.xml.bz2
3. Extract the file using the following command bunzip2 tawiki-latest-pages-articles.xml.bz2
4. Clone Attardi Wiki Extractor Tool https://github.com/attardi/wikiextractor
5. An example on how to run WikiExtractor python3 WikiExtractor.py -o /Users/malaikannan/Documents/Work/opensource/TamilData /Users/malaikannan/Documents/Work/opensource/tawiki-latest-pages-articles.xml
6. Clone the IndicNLPParser repo 
7. To run python3 wikiparser.py --wiki_dump_path "/Users/malaikannan/Documents/Work/opensource/TamilData" --csv_file_path "/Users/malaikannan/Documents/Work/opensource/TamilData/tamil_words.csv" --lower_unicode_value 2944 --upper_unicode_value 3071 
8. lower_unicode_value and upper_unicode_value are Decimal values
9. For Tamil lower_unicode_value = 2944 and upper_unicode_value = 3071
10. For Telugu lower_unicode_value = 3072 and upper_unicode_value = 3199
11. For Malaylam lower_unicode_value = 3328 and upper_unicode_value = 3455
12. Output from the program will be written into a csv file 


