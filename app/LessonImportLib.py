try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract as tess
import PyPDF2
import io
import json
import unicodedata
from youtube_transcript_api import YouTubeTranscriptApi
from pdf2image import convert_from_path
import os
# from translate import Translator
from langImport.models import *
from google_trans_new import google_translator
import re
from PyDictionary import PyDictionary
import requests

try:
    # python 3
    from urllib.parse import urlparse, parse_qs
except ImportError:
    # python 2
    from urlparse import urlparse, parse_qs


# pass image and language reference to create lesson
def image_to_string(image_file, imageLang):
    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image_string = tess.image_to_string(Image.open(image_file), lang=imageLang)

    os.remove(image_file)
    return image_string


def string_to_json_format(lesson_string, target_lang, native_lang, up_method, up_title):

    lesson_string = remove_control_characters(lesson_string)
    lesson_string = lesson_string.replace("\n", " ")
    lesson_string = lesson_string.replace("- ", ' ')
    lesson_string = lesson_string.replace(" - ", ' ')
    lesson_string = lesson_string.replace("—", ' ')
    lesson_string = lesson_string.replace("|", ' ')
    lesson_string = lesson_string.replace("(", ' ')
    lesson_string = lesson_string.replace(")", ' ')
    lesson_string = lesson_string.replace(":", ' ')
    lesson_string = lesson_string.replace(" .", '. ')
    lesson_string = lesson_string.replace("\\", ' ')
    lesson_string = lesson_string.replace(", ", " ")
    lesson_string = lesson_string.replace("«", " ")
    lesson_string = lesson_string.replace("»", " ")
    lesson_string = lesson_string.replace("›", " ")
    lesson_string = lesson_string.replace("©", " ")
    lesson_string = lesson_string.replace("„", " ")
    lesson_string = lesson_string.lower()

    # removes extra spaces within the text
    count = 0
    for x in lesson_string:
        if x == " ":
            count = count + 1
        if x != " " and count != 0:
            lesson_string = lesson_string.replace(" " * count, " ")
    lesson_string = lesson_string.split(". ")

    for m in lesson_string:
        for n in m:
            n.replace("/,", "")

    new_json = '{"up_title": "' + up_title + '", "up_method": "' + up_method + '", "target_lang": "' + target_lang + '", "native_lang": "' + native_lang + '", "lesson_sentences":['

    count = 1
    w_count = 0
    for i in lesson_string:
        new_string = i.split(" ")
        new_json = new_json + '{"sentence_'
        count = count + 1
        new_json = new_json + '":['
        sent_count = 0
        w_count = w_count + 1
        for k in new_string:

            sent_count = sent_count + 1
            if len(new_string) > sent_count:
                new_json = new_json + '{"' + target_lang + '":"' + k + '","' + native_lang + '": ""},'

            else:
                new_json = new_json + '{"' + target_lang + '":"' + k + '","' + native_lang + '": ""}'
        if len(lesson_string) > w_count:
            new_json = new_json + ']},'
        else:
            new_json = new_json + ']}]}'

    return new_json


def string_to_json(json_string):
    json_format = json.loads(json_string)

    return json.dumps(json_format, ensure_ascii=False)


# pass video code, target language and native language to create a json file
def youtube_to_json(urlString, targetLang, nativeLang, up_title):

    up_method = 'Youtube url'
    video_id = urlString
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[targetLang, nativeLang])

    transcript = str(transcript)
    transcript = remove_control_characters(transcript)

    transcript = transcript.replace("'", "")
    transcript = transcript.replace('"', '')
    transcript = transcript.replace('text: ', '"text": "')
    transcript = transcript.replace(', start:', '", "start":')
    transcript = transcript.replace(', duration:', ', "duration":')
    transcript = transcript.replace("\\", "")

    #change the language codes
    if(targetLang == 'ru'):
        targetLang = 'Russian'
    if(targetLang == 'en'):
        targetLang = 'English'
    if (targetLang == 'es'):
        targetLang = 'Spanish'
    if (targetLang == 'fr'):
        targetLang = 'French'

    if(nativeLang == 'ru'):
        nativeLang = 'Russian'
    if(nativeLang == 'en'):
        nativeLang = 'English'
    if (nativeLang == 'es'):
        nativeLang = 'Spanish'
    if (nativeLang == 'fr'):
        nativeLang = 'French'



    new_string = json.loads(transcript)

    new_json = '{ "up_title": "' + up_title + '", "up_method": "' + up_method + '", "target_lang": "' + targetLang + '", "native_lang": "' + nativeLang + '", "lesson_sentences":['





    w_count = 0;
    for x in new_string:
        sent_count = 0;

        w_count = w_count + 1
        new_json = new_json + '{"sentence_":['
        to_split = x['text']
        to_split = to_split.split(" ")
        for i in to_split:
            print(i)

            sent_count = sent_count + 1
            if len(to_split) > sent_count:
                new_json = new_json + '{"' + targetLang + '":"' + i + '","' + nativeLang + '": ""},'

            else:
                new_json = new_json + '{"' + targetLang + '":"' + i + '","' + nativeLang + '": ""}'

        if len(new_string) > w_count:
            new_json = new_json + ']},'
        else:
            new_json = new_json + ']}]}'

    new_json = json.loads(new_json)


    # new_json = json.loads(new_json)

    
    
    return json.dumps(new_json, ensure_ascii=False)




# converts a pdf to image then image to string
# depends on image_to_string method to work!!!
def pdf_to_string(pdf_file, target_lang):
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_file)
    newstring = ''
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('temp_images/_page' + str(i) + '.jpg', 'JPEG')

    for i in range(len(images)):
        newstring = newstring + image_to_string('temp_images/_page' + str(i) + '.jpg', target_lang)

    os.remove(pdf_file)

    return newstring


# checks to see if there are any missing translations among the languages for the new word
# if there is, add them, and then make a new master dictionary entry
# using whenever new word is added as it'll automatically populate all other languages
def check_trans(new_word, target_lang, native_lang):
    translator = google_translator()
   
    print(native_lang)
    if(native_lang == "English"):
        
        result = translator.translate(new_word, lang_tgt='en')
    
    if(native_lang == "Spanish"):
        
        result = translator.translate(new_word, lang_tgt='es')
    
    if(native_lang == "French"):
        
        result = translator.translate(new_word, lang_tgt='fr')
    
    if(native_lang == "Russian"):
       
        result = translator.translate(new_word, lang_tgt='ru')
    
    

    result = result.strip()
    result = result.replace(' ', '-')

    if isinstance(result, list):
        result = result[0]
    result = re.sub("[^a-zA-Z']+", '', result)

    # with this I'm assuming that since if a word is added there'll be an English translation,
    # that if it is missing then the word just doesn't exist
    if(native_lang == "English" and EnglishWord.objects.filter(word=result).exists()):
        print(result + " exists")
        return result

    if(native_lang == "Spanish" and SpanishWord.objects.filter(word=result).exists()):
        print(result + " exists")
        return result
    if(native_lang == "French" and FrenchWord.objects.filter(word=result).exists()):
        print(result + " exists")
        return result
    if(native_lang == "Russian" and RussianWord.objects.filter(word=result).exists()):
        print(result + " exists")
        return result
    


        


    # definition and word class hell
    elif not EnglishWord.objects.filter(word=result).exists() or SpanishWord.objects.filter(word=result).exists() or FrenchWord.objects.filter(word=result).exists() or RussianWord.objects.filter(word=result).exists():

        dictionary = PyDictionary(result)
        definition = ''
        wordClass = ''
        try:
            if dictionary.getMeanings()[result] is None:

                # backup using oxford dictionary
                # has a 1000 request limit so is ONLY to be used as a fallback in case PyDictionary doesn't work like it
                # sometimes does
                app_id = '357c2725'
                app_key = 'ec311ce6a30cde29b5a736a5301f0d9c'

                url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + 'en' + '/' + result.lower() + '?' + \
                      "fields=definitions"
                r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

                
                stage1 = json.dumps(r.json()).split('definitions')

                check = str(stage1).split('"')

                #error checking for if there's no translation
                if check[1] == 'error':
                    definition = 'None'
                    wordClass = "None"
                else:
                    wordStage1 = json.dumps(r.json()).split('lexicalCategory')
                    wordStage2 = str(wordStage1[1]).split('"text": ')
                    wordClass = str(wordStage2[1]).split('}')[0]
                    # stage1[1] = re.sub('[^\\w-]+', '', stage1[1])

                    stage2 = str(stage1).split('id')
                    defRes = stage2[0]

                    for char in defRes:
                        if char.isalnum():
                            definition += char
                        elif char == ' ':
                            definition += char

                    definition = definition[1:]

            else:
                definition = str(dictionary.getMeanings()).split('[')
                wordClass = definition[0]
                wordClass = wordClass.split(':')
                wordClass = str(wordClass).split('{')
                wordClass = wordClass[2]
                wordClass = str(wordClass).split('"')
                wordClass = wordClass[0]
                definition = definition[1].split('"')
                definition = definition[0]
                definition = str(definition).split(']')
                definition = definition[0]
                definition = definition[1:]
        except:
            ("Could not get definition")


        result = translator.translate(new_word, lang_tgt='en')
        if isinstance(result, list):
            result = result[0]
        # result = re.sub("[^a-zA-Z']+", '', result)
        en_word = EnglishWord(word=result, definition=definition, word_class=wordClass)
        # en_word.save()

        # spanish word processing
        result1 = translator.translate(new_word, lang_tgt='es')
        if isinstance(result1, list):
            result1 = result1[0]

        result1 = re.sub("[^a-zA-Z']+", '', result1)
        spa_word = SpanishWord(word=result1, definition=translator.translate(definition, 'es'),
                               word_class=translator.translate(wordClass, 'es'))
        # spa_word.save()

        # french word processing
        result2 = translator.translate(new_word, lang_tgt='fr')
        if isinstance(result2, list):
            result2 = result2[0]

        result2 = re.sub("[^a-zA-Z']+", '', result2)
        fr_word = FrenchWord(word=result2, definition=translator.translate(definition, 'fr'),
                             word_class=translator.translate(wordClass, 'fr'))
        # fr_word.save()

        # russian word processing
        result3 = translator.translate(new_word, lang_tgt='ru')
        if isinstance(result3, list):
            result3 = result3[0]

        rus_word = RussianWord(word=result3, definition=translator.translate(definition, 'ru'),
                               word_class=translator.translate(wordClass, 'ru'))
        # rus_word.save()

        add_master_dict(EnglishWord.objects.filter(word=result).first(),
                        SpanishWord.objects.filter(word=result1).first(),
                        FrenchWord.objects.filter(word=result2).first(),
                        RussianWord.objects.filter(word=result3).first())

        if native_lang == "English":
            print(result + " does not exist")
            return result
        if native_lang == "Spanish":
            return result1
        if native_lang == "French":
            return result2
        if native_lang == "Russian":
            return result3


# called whenever a new word is added. it will make a new dictionary entry for the one word using all languages
def add_master_dict(en_word, spa_word, fr_word, rus_word):
    add_word = Tdictionary(en_id=en_word, spa_id=spa_word, fr_id=fr_word, ru_id=rus_word)
    # add_word.save()




def text_to_string(text_file, target_lang, native_lang, up_method, up_title):
    # new_file_name = os.path.splitext(text_file)[0] + ''
    text = io.open(text_file, 'r', encoding="utf-8")
    text_json_obj = string_to_json(string_to_json_format(text.read(), target_lang, native_lang, up_method, up_title))
    text.close()
    os.remove(text_file)
    return text_json_obj


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


def extract_id(url):
    """Returns Video_ID extracting from the given url of Youtube

    Examples of URLs:
      Valid:
        'http://youtu.be/_lOT2p_FCvA',
        'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
        'http://www.youtube.com/embed/_lOT2p_FCvA',
        'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
        'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
        'youtube.com/watch?v=_lOT2p_FCvA',

      Invalid:
        'youtu.be/watch?v=_lOT2p_FCvA',
    """

    if url.startswith(('youtu', 'www')):
        url = 'http://' + url

    query = urlparse(url)

    if 'youtube' in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif 'youtu.be' in query.hostname:
        return query.path[1:]
    else:
        raise ValueError


# pass a string, the native language and target language to get the translated text
def translate_string(target_string, native_lang, target_lang):
    translated_text = translator(target_lang, native_lang, target_string)
    # print(translated_text[0][0][0])
    return translated_text[0][0][0]


# finds all the language codes that need to be translated to
def find_all_to_translate(native_lang):
    language_codes = ['en', 'ru', 'fr', 'es']
    codes_to_translate = []
    for x in language_codes:
        if x == native_lang:
            pass
        else:
            codes_to_translate.append(x)
    return codes_to_translate


# translates a word in all available lanuages
def translate_to_all(target_string, native_lang, lang_codes):
    for x in lang_codes:
        translate_string(target_string, native_lang, x)
