import argparse
import sys
import text as toSpeech
import sys
import speech_recognition as sr


def speech(args):
    text = args.text
    is_file = args.file
    voice = args.voice or "gb"
    speed = args.speed or 160
    show_text = args.echo
    toSpeech.textToSpeech(text, is_file, voice, speed, show_text)


def main():
    try:
        if not len(sys.argv) > 1:
            raise Exception("Arguments missing, no arguments were passed")
        parser = argparse.ArgumentParser(
            description='🛠️ Description to come here 🛠️', formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument(
            'text', type=str, help='file path or text string to transform as speech')
        parser.add_argument(
            '-f', '--file', action='store_false', help='to pass a text string as argument')
        parser.add_argument(
            '-s', '--speed', metavar='', type=int, help='set the reading speed. (the number of words per minute)')
        parser.add_argument(
            '-v', '--voice',
            type=str,
            metavar='',
            choices=[
                'gb', 'gb-female', 'gb-grandpa', 'gb-grandma',
                'us', 'us-female', 'us-grandma',
                'fr', 'fr-female', 'fr-grandpa', 'fr-grandma',
                'it', 'it-female', 'it-grandpa', 'it-grandma',
                'es', 'es-female',
                'ru',
                'jp',
                'robot', 'robot-2', 'robot-3', 'robot-4', 'robot-5',
                'bells', 'bubbles', 'cellos', 'albert', 'whisper'
            ],
            help='''voice selection:
                english  - gb, gb-female, gb-grandpa, gb-grandma,
                           us, us-female, us-grandpa, us-grandma,
                french   - fr, fr-female, fr-grandpa, fr-grandma,
                italian  - it, it-female, it-grandpa, it-grandma,
                spanish  - es, es-female,
                russian  - ru,
                japanese - jp,
                
                other    - robot, robot-2, robot-3, robot-4, bells,
                           bubbles, cellos, albert, whisper
            ''')
        parser.add_argument(
            '-e', '--echo', action='store_true', help='echo the text content of the given file')

        args = parser.parse_args()

        speech(args)
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
