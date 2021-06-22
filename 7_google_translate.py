from googletrans import Translator

translator = Translator()
print("Enter the text(in English) to translate =>", end =" ")
str=input()
results = translator.translate(str,dest='kn',src='en')
print("Translated text in Kannada =>", end =" ")
print(results.text)