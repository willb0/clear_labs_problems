import googletrans
import json
import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('language')

args = parser.parse_args()
print(args.filename,args.language)
if(args.language not in googletrans.LANGUAGES.keys()):
    raise ValueError("Invalid Language")

translator = googletrans.Translator() 

with open('./'+args.filename,'r') as f:
    data = json.load(f)
    dumpie=["Words with translations",{}]
    print('translating from english to %s' % googletrans.LANGUAGES[args.language])
    for word in data['words']:
        translated_word = translator.translate(word, dest = args.language).text
        print("word: %s \t translated_word: %s" % (word,translated_word))
        dumpie[1].update({word:translated_word})
    json.dump(dumpie,open('dump.json','w+'))
    print("dumped to dump.json")





