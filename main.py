import argparse
import textwrap
import sys
import text as toSpeech


class Action:
    def __init__(self, args):
        self.args = args


class Version(Action):
    @staticmethod
    def run():
        print("Version 1.0")


class ToSpeech(Action):
    def run(self):
        text = self.args.file_path
        string = self.args.string
        voice = self.args.voice or "gb"
        speed = self.args.speed or 160
        show_text = self.args.echo

        toSpeech.textToSpeech(text, string, voice, speed, show_text)


def main():
    try:
        if not len(sys.argv) > 1:
            raise Exception("Arguments missing, no arguments were passed")
        parser = argparse.ArgumentParser(
            description='🛠️ Description to come here 🛠️')
        sub_parsers = parser.add_subparsers(dest='action')
        test_parser = sub_parsers.add_parser(
            'test', help="Display version for now, work in progress, see test --help")

        to_speech_parser = sub_parsers.add_parser(
            'to-speech', help="Transform text to speech, see to-speech --help", formatter_class=argparse.RawTextHelpFormatter)
        to_speech_parser.add_argument(
            'file_path', type=str, help='File path or text string to transform as speech')
        to_speech_parser.add_argument(
            '-s', '--string', action='store_true', help='To pass a text string as argument')
        to_speech_parser.add_argument(
            '-sp', '--speed', metavar='', type=int, help='Set the reading speed. (the number of words per minute)')
        to_speech_parser.add_argument(
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
            help='''Voice selection:
                English  - gb, gb-female, gb-grandpa, gb-grandma,
                           us, us-female, us-grandpa, us-grandma,
                French   - fr, fr-female, fr-grandpa, fr-grandma,
                Italian  - it, it-female, it-grandpa, it-grandma,
                Spanish  - es, es-female,
                Russian  - ru,
                Japanese - jp,
                
                Other    - robot, robot-2, robot-3, robot-4, bells,
                           bubbles, cellos, albert, whisper
            ''')
        to_speech_parser.add_argument(
            '-e', '--echo', action='store_true', help='Echo the text content of the given file')

        args = parser.parse_args()

        function_map = {
            'to-speech': ToSpeech,
            'test': Version,
        }

        operation_class = function_map[args.action]
        operation = operation_class(args)
        operation.run()
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
