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
from translate import translator

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


def string_to_json_format(lesson_string, target_lang, native_lang, up_method):
   
    lesson_string = remove_control_characters(lesson_string)
    lesson_string = lesson_string.replace("\n", " ")
    lesson_string = lesson_string.replace("- ", '')
    lesson_string = lesson_string.replace("-", '')
    lesson_string = lesson_string.replace("\\", '')
    lesson_string = lesson_string.replace(", ", " ")
    lesson_string = lesson_string.replace("«", "")
    lesson_string = lesson_string.replace("»", "")
    lesson_string = lesson_string.replace("›", "")
    lesson_string = lesson_string.replace("©", "")
    lesson_string = lesson_string.replace("„", "")
    lesson_string = lesson_string.lower()
    
    #removes extra spaces within the text
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
            

    new_json = '{"up_method": "'+ up_method + '", "target_lang": "'+ target_lang + '", "native_lang": "'+ native_lang +'", "lesson_sentences":['

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
                new_json = new_json + '{"'+ target_lang +'":"' + k + '","'+ native_lang +'": ""},'

            else:
                new_json = new_json + '{"'+ target_lang +'":"' + k + '","'+ native_lang +'": ""}'
        if len(lesson_string) > w_count:
            new_json = new_json + ']},'
        else:
            new_json = new_json + ']}]}'

    return new_json

def string_to_json(json_string):
    json_format = json.loads(json_string)
    return json.dumps(json_format, ensure_ascii=False)

# pass video code, target language and native language to create a json file
def youtube_to_json(urlString, targetLang, nativeLang):

    video_id = urlString
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[targetLang, nativeLang])
    transcript = str(transcript)
    
    for x in transcript:
        transcript = transcript.replace("'text'", '"text"')
        transcript = transcript.replace("'start'", '"start"')
        transcript = transcript.replace("'duration'", '"duration"')
        transcript = transcript.replace(" '", ' "')
        transcript = transcript.replace("',", '",')

    new_string = json.loads(transcript)

    return json.dumps(new_string, ensure_ascii=False)

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

def text_to_string(text_file, target_lang, native_lang):
    # new_file_name = os.path.splitext(text_file)[0] + ''
    text = io.open(text_file, 'r', encoding="utf-8")
    text_json_obj = string_to_json(string_to_json_format(text.read(), target_lang, native_lang))
    text.close()
    # os.remove(text_file)
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
    print(translated_text[0][0][0])
    return translated_text[0][0][0]

#finds all the language codes that need to be translated to
def find_all_to_translate(native_lang):
    language_codes = ['en', 'ru', 'fr', 'es']
    codes_to_translate = []
    for x in language_codes:
        if x == native_lang:
            pass
        else:
            codes_to_translate.append(x)
    return codes_to_translate

#translates a word in all available lanuages
def translate_to_all(target_string, native_lang, lang_codes):
    for x in lang_codes:
        translate_string(target_string, native_lang, x)