import pyttsx3
from PyDictionary import PyDictionary
from wordhoard import Antonyms, Synonyms

class Voice:
    def speak(self, sentence):
        pt = pyttsx3.init("sapi5")
        voice = pt.getProperty('voices')
        volume = pt.getProperty('volume')
        pt.setProperty('voices', voice[0].id)
        pt.setProperty('volume', 0.75)

        pt.say(sentence)
        pt.runAndWait()

class WordTinker:
    def Dictionary(self):
        speak = Voice()
        dic = PyDictionary()
        speak.speak("Please enter the word: ")

        word = str(input())
        mean = dic.meaning(word)
        for var in mean:
            key_list = list(mean.keys())
            val_list = list(mean.values())
            position = val_list.index(mean[var])
            print(mean[var])
            speak.speak(f"The meaning of the word {word} as {key_list[position]} is " + str(mean[var]))

    def synonyms(self):
        speak = Voice()
        speak.speak("Please enter the word: ")

        word = str(input())
        synonym = Synonyms(search_string=word)
        synonym_results = synonym.find_synonyms()
        speak.speak(f"The synonym of {word} are " )
        for syn in synonym_results:
            print(syn)
            speak.speak(str(syn))

    def antonyms(self):
        speak = Voice()
        speak.speak("Please enter the word: ")

        word = str(input())
        antonyms = Antonyms(search_string=word)
        antonym_result = antonyms.find_antonyms()
        speak.speak(f"The antonyms of {word} are ")
        for ant in antonym_result:
            print(ant)
            speak.speak(str(ant))
if __name__ == '__main__':
    WordTinker()
    voice = Voice()
    voice.speak("Please select your choice: ")
    voice.speak("1. Meaning ")
    voice.speak("2. Synonyms ")
    voice.speak("3. Antonyms ")
    choice = int(input())
    if(choice == 1):
        WordTinker.Dictionary(self=None)
    elif(choice == 2):
        WordTinker.synonyms(self=None)
    elif(choice == 3):
        WordTinker.antonyms(self=None)
    else:
        voice.speak("Please enter correct choice!")