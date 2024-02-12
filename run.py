import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def record_text():

    while(1):
        try:

            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source , duration=0.2)

                ses = r.listen(source)

                txt = r.recognize_google(ses , language="tr-TR")

                return txt

        except sr.RequestError as e:
            print("sonuç istenemedi; {0}".format(e))

        except sr.UnknownValueError:
            print("bilinmeyen hata oluştu.")

    return

def output_text(text):
    f = open("txt.txt" , "a" , encoding="utf-8")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    output_text(text)

    print("Yazdırıldı")
