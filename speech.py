# import speech_recognition as sr

# # initialize recognizer class (for recognizing the speech)
# r = sr.Recognizer()

# # Reading Microphone as source
# # listening the speech and store in audio_text variable
# with sr.Microphone() as source:
#     print("Talk")
#     audio_text = r.listen(source)
#     print("Time over, thanks")
#     print("Text: "+r.recognize_sphinx(audio_text))


# import speech_recognition as sr

# # Initialiser le recognizer
# r = sr.Recognizer()

# # Fonction de reconnaissance de la parole


# def recognize_speech_from_mic(recognizer, microphone):
#     # Vérifiez que le microphone est connecté
#     if not microphone.list_microphone_names():
#         print("Aucun microphone n'a été trouvé.")
#         return

#     # Utiliser le microphone par défaut
#     with microphone as source:
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     # Reconnaître la parole à partir du flux audio
#     transcript = None
#     try:
#         transcript = recognizer.recognize_sphinx(audio, language="fr-FR")
#         print("Vous avez dit: {}".format(transcript))
#     except sr.UnknownValueError:
#         print("La reconnaissance vocale n'a pas pu comprendre ce que vous avez dit.")
#     except sr.RequestError as e:
#         print("Erreur de reconnaissance vocale; {0}".format(e))

#     return transcript


# # Initialiser un microphone
# microphone = sr.Microphone()

# # Lancer la reconnaissance vocale
# recognize_speech_from_mic(r, microphone)

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

# text = r.recognize_sphinx(audio)
# text = r.recognize_google(audio, language="fr-FR")
text = r.recognize_sphinx(audio)

print("This is what I understood.. : {}".format(text))
