# speakEasy
Text-to-speech CLI tool

#### Table of contents
- [usage](#usage)
- [arguments](#arguments)
- [options](#options)
- [voice list](#%EF%B8%8F-voice-list)
- [some examples](#examples)

## Usage

main.py [-h] [-f] [-s] [-v] [-e] text

##### Basic example
```bash
main.py 'hello world!'
```

## Arguments

Takes one positional argument:
```bash
main.py [text]    # file path or text string to transform into speech
```

## Options

Available options:
```bash
-h, --help           # show this help message and exit
-c, --clear          # set flag to have no output, won't impact [-e, --echo]
-e, --echo           # echo the text content of the given file
-f, --file           # to pass a text string as argument
-l, --listen         # to make the script listen for inputs, when listening press "q" to stop
-s , --speed [INT]   # set the reading speed. (the number of words per minute)
-v , --voice [VOICE] # voice selection. [see list](#%EF%B8%8F-voice-list)
```

## 🗣️ Voice list
```bash
english     # gb, gb-female, gb-grandpa, gb-grandma,
            # us, us-female, us-grandpa, us-grandma,
french      # fr, fr-female, fr-grandpa, fr-grandma,
italian     # it, it-female, it-grandpa, it-grandma,
spanish     # es, es-female,
russian     # ru,
japanese    # jp,

other       # robot, robot-2, robot-3, robot-4, bells,
            # bubbles, cellos, albert, whisper
```

## Examples

```bash
# Setting up speed, default is 160 (word/m)
main.py 'Hello world!' -s 50

# Setting a specific output voice, default is gb
main.py 'Hello world!' -v robot

# Giving a file path
main.py -f file.txt -v robot -s 50
```


[table of contents](#table-of-contents)
