# IndicNLPParser
Indic NLP Unique Words

Program is meant to get unique list of words and the frequency in which it has occurred in Wikipedia. There is a bloom filter implementation to return a flag whether the word is valid in a language or not. Current implementation has bloom filter for Tamil, Telugu, Malayalam and Bengali. 

1. For Tamil get the latest dump from  http://dumps.wikimedia.org/tawiki/latest/ . Telugu will be like  http://dumps.wikimedia.org/tewiki/latest/
2. File to be downloaded is tawiki-latest-pages-articles.xml.bz2
3. Extract the file using the following command bunzip2 tawiki-latest-pages-articles.xml.bz2
4. Clone Attardi Wiki Extractor Tool https://github.com/attardi/wikiextractor
5. An example on how to run WikiExtractor python3 WikiExtractor.py -o /Users/malaikannan/Documents/Work/opensource/TamilData /Users/malaikannan/Documents/Work/opensource/tawiki-latest-pages-articles.xml
6. Clone the IndicNLPParser repo 
7. To run python3 wikiparser.py --wiki_dump_path "/home/ANANT/msankarasubbu/Documents/Work/opensource/Data" --csv_file_path "/home/ANANT/msankarasubbu/Documents/Work/opensource/Data/tamil_words.csv"  --bloomfilter_file_path "/home/ANANT/msankarasubbu/Documents/Work/opensource/Data/tamil_words_filter.txt" --lower_unicode_value 2944 --upper_unicode_value 3071 
8. lower_unicode_value and upper_unicode_value are Decimal values
9. For Tamil lower_unicode_value = 2944 and upper_unicode_value = 3071
10. For Telugu lower_unicode_value = 3072 and upper_unicode_value = 3199
11. For Malaylam lower_unicode_value = 3328 and upper_unicode_value = 3455
12. Output from the program will be written into a csv file and bloom filter file. 
13. Tamil bloomfilter file https://www.dropbox.com/s/3bibyzccjkdkh86/tamil_words_filter.txt?dl=0
14. Telugu bloomfilter file https://www.dropbox.com/s/qdc0a7ueqowyw2z/telugu_words_filter.txt?dl=0
15. Malayalam bloomfilter file https://www.dropbox.com/s/aqienzy351i1420/malayalam_words_filter.txt?dl=0
16. Bengali bloom filter file https://www.dropbox.com/s/okskp4skl2tbsqn/bengali_words_filter.txt?dl=0
17. Update bloomservice.py with the correct path and items_count for respective languages. I have updated it for the runs that I did. 
18. Run gunicorn --bind 0.0.0.0:5000 bloomservice:app to serve the REST Service
19. Tamil can be accessed in http://localhost:5000/indicnlp/tamil/v1.0/<word>. Replace <word> with actual tamil word.
20. Telugu can be accessed in http://localhost:5000/indicnlp/telugu/v1.0/<word>. Replace <word> with actual telugu word.
21. Malayalam can be accessed in http://localhost:5000/indicnlp/malayalam/v1.0/<word>. Replace <word> with actual Malayalam word.
22. Bengali can be accessed in http://localhost:5000/indicnlp/bengali/v1.0/<word>. Replace <word> with actual Bengali word. 
  
  
## Current URL 

### Tamil 
https://7b2c652e.ngrok.io/indicnlp/tamil/v1.0/மதுரை

### Telugu
https://7b2c652e.ngrok.io/indicnlp/telugu/v1.0/ఆహార

### Malayalam
https://7b2c652e.ngrok.io/indicnlp/malayalam/v1.0/ഭക്ഷണം

### Bengali 
https://7b2c652e.ngrok.io/indicnlp/bengali/v1.0/খাদ্য

### Negative Test 
https://7b2c652e.ngrok.io/indicnlp/tamil/v1.0/hello




## Previous Work 

T Shrinivasan has done some earlier work on this area 
https://github.com/tshrinivasan/tamil-wikipedia-word-list

Muthunedumaran of Murasu Anjal fame has a bash script to do it one line 

bzcat archive.bz2 | grep -v '<[a-z]*\s' | grep -v '&[a-z0-9]*;' | tr '[:punct:][:blank:][:digit:]' '\n' | tr 'A-Z' 'a-z' | tr 'ÆØÅŜĴĤĜŬ' 'æøåŝĵĥĝŭ' | uniq | sort -f | uniq -c | sort -nr | head -50000 | tail -n +2 | awk '{print "<w f=\""$1"\">"$2"</w>"}' > dict.xml * Or for output without accents characters: bzcat archive.bz2 | grep -v '<[a-z]*\s' | grep -v '&[a-z0-9]*;' | tr '[:punct:][:blank:][:digit:]' '\n' | tr 'A-Z' 'a-z' | uniq | grep -o '^[a-z]*$' | sort -f | uniq -c | sort -nr | head -50000 | awk '{print "<w f=\""$1"\">"$2"</w>"}' > en.xml

https://code.google.com/archive/p/softkeyboard/wikis/BinaryDictionaries.wiki?fbclid=IwAR0efckl3qpqeRBuAK9pc7MGZx1ZcFjgcdHa_FIRStLf46fEiAYo3pl8kjg
