from googletrans import Translator

def translate(text):
    t = Translator()
    translated = t.translate(text, src='en', dest='ru')
    return translated.text

print(translate("how are you"))
