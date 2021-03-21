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


# pass image and language reference to create lesson
def image_to_string(image_file, imageLang):
    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    return tess.image_to_string(Image.open(image_file), lang=imageLang)


# pass a string and create a json file
def string_to_json(lesson_string):
    lesson_string = lesson_string.replace("\n", " ")
    lesson_string = lesson_string.replace("- ", '')
    lesson_string = lesson_string.split(". ")
    new_json = ''

    for x in lesson_string:
        x = "{'text':" + "'" + x + "'},"
        print(x)
        new_json = new_json + x

    new_json = new_json.rstrip(new_json[-1])
    new_json = "[" + new_json + "]"
    new_json = new_json.replace("'", '"')  # replaces single quotes with double quotes
    new_json = remove_control_characters(new_json)
    print(json)
    trans_string = io.open('imports_json/ttj.json', 'w', encoding="utf-8")
    trans_string.write(new_json)
    trans_string.close()


# pass video code, target language and native language to create a json file
def youtube_to_json(urlString, targetLang, nativeLang):
    video_id = urlString
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[targetLang, nativeLang])

    transcript = str(transcript)

    new = transcript.replace('"', '')  # removes double quotes
    new = new.replace("'", '"')  # replaces single quotes with double quotes
    print(type(new))

    new_string = new.replace('\\xa0', '')  # removes \\XaO
    new_string = new_string.replace('\\n', ' ')  # replaces \n with a space
    json.dumps(new_string)
    print(new_string)

    transText = io.open(video_id + '.json', 'w', encoding="utf-8")
    transText.write(new_string)
    transText.close()


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
        os.remove('temp_images/_page' + str(i) + '.jpg')

    return newstring


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")



