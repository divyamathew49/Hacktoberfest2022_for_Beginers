import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
     print('SPEAK Anything ')
     audio = r.listen(source)
     try:
         text = r.recognize_google(audio)
         print('you said : {}'.format(text))
         a = format(text)
         return(a)
     except:
         a='sorry could not recognize your voice'
         return(a)
