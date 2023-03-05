import pyttsx3
import sys
import termios
import tty
import threading
import curses

voices = {
    "fr": "com.apple.voice.compact.fr-FR.Thomas",
    "fr-female": "com.apple.eloquence.fr-FR.Flo",
    "fr-grandma": "com.apple.eloquence.fr-FR.Grandma",
    "fr-grandpa": "com.apple.eloquence.fr-FR.Grandpa",
    "gb": "com.apple.voice.compact.en-GB.Daniel",
    "gb-female": "com.apple.eloquence.en-GB.Shelley",
    "gb-grandma": "com.apple.eloquence.en-GB.Grandma",
    "gb-grandpa": "com.apple.eloquence.en-GB.Grandpa",
    "us": "com.apple.eloquence.en-US.Eddy",
    "us-female": "com.apple.voice.compact.en-US.Samantha",
    "us-grandma": "com.apple.eloquence.en-US.Grandma",
    "ru": "com.apple.voice.compact.ru-RU.Milena",
    "es": "com.apple.eloquence.es-ES.Reed",
    "es-female": "com.apple.eloquence.es-ES.Flo",
    "it": "com.apple.eloquence.it-IT.Eddy",
    "it-female": "com.apple.eloquence.it-IT.Flo",
    "it-grandma": "com.apple.eloquence.it-IT.Grandma",
    "it-grandpa": "com.apple.eloquence.it-IT.Grandpa",
    "jp": "com.apple.voice.compact.ja-JP.Kyoko",
    "bells": "com.apple.speech.synthesis.voice.Bells",
    "robot": "com.apple.speech.synthesis.voice.Boing",
    "robot-2": "com.apple.speech.synthesis.voice.BadNews",
    "robot-3": "com.apple.speech.synthesis.voice.Zarvox",
    "robot-4": "com.apple.speech.synthesis.voice.Trinoids",
    "bubbles": "com.apple.speech.synthesis.voice.Bubbles",
    "cellos": "com.apple.speech.synthesis.voice.Cellos",
    "albert": "com.apple.speech.synthesis.voice.Albert",
    "whisper": "com.apple.speech.synthesis.voice.Whisper"
}


def textToSpeech(text: str, is_string: bool, voice: str, speed: int, show_text: bool, listen: bool, clear: bool):
    engine = pyttsx3.init()
    engine.setProperty('voice', voices[voice])
    engine.setProperty('rate', speed)

    def on_press():
        try:
            # Set terminal to raw mode to read key presses
            old_settings = termios.tcgetattr(sys.stdin)
            tty.setcbreak(sys.stdin)
            print("Press 'q' to stop.")
            while True:
                ch = sys.stdin.read(1)
                if ch == 'q':
                    engine.stop()
                    if not clear:
                        print("SpeakEasy stopped")
                    break
        except termios.error as e:
            # if the termios operation fails, fall back to a simpler method
            print("Failed to read input with termios:", e)
            while True:
                try:
                    # read keypress using curses
                    ch = chr(curses.inch())
                    if ch == 'q':
                        engine.stop()
                        if not clear:
                            print("SpeakEasy stopped")
                        break
                except:
                    pass
        finally:
            # Restore terminal settings when finished
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    if text:
        to_read = text if is_string else open(text, 'r').read().rstrip()

        if show_text:
            print(to_read)
        engine.say(to_read)
        if engine.isBusy():
            if not clear:
                print("Currentrly speaking")
        if listen:

            t = threading.Thread(target=on_press)
            t.daemon = True
            t.start()
        engine.runAndWait()
        if not clear:
            print("Done speaking")
        return
    else:
        error = "No file_path given" if is_string else "No text string given"
        raise Exception(error)


# t = threading.Thread(target=on_press) :
# Create a new thread to listen for key presses while the engine is speaking
# The target parameter specifies the callable object to be invoked when the
# thread starts. In this case, the on_press function will be run in the new thread.

# t.daemon = True :
# The daemon attribute is set to True for the new thread, which means that
# it will run in the background and won't prevent the Python interpreter
# from exiting when the main thread finishes.

# t.start() :
# the start() method is called on the new thread object
