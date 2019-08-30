#!flask/bin/python
from flask import Flask, jsonify
from bloomfilter import BloomFilter 

app = Flask(__name__)

tamil_items_count = 1386991
telugu_items_count = 1267283
falsepositive_probability = 0.001

bloom_tamil = BloomFilter(tamil_items_count,falsepositive_probability,"/home/ANANT/msankarasubbu/Documents/Work/opensource/Data/TamilData/tamil_words_filter.txt")
bloom_telugu = BloomFilter(telugu_items_count,falsepositive_probability,"/home/ANANT/msankarasubbu/Documents/Work/opensource/Data/TeluguData/telugu_words_filter.txt")

@app.route('/indicnlp/tamil/v1.0/<word>', methods=['GET'])
def check_tamil_word(word):
    if bloom_tamil.check(word):
        Flag = True
    else:
        Flag = False
    return jsonify({'Flag': Flag})


@app.route('/indicnlp/telugu/v1.0/<word>', methods=['GET'])
def check_telugu_word(word):
    if bloom_telugu.check(word):
        Flag = True
    else:
        Flag = False
    return jsonify({'Flag': Flag})



if __name__ == '__main__':
    app.run()