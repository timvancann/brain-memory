# brain-memory

Practice and reference the [Mnemonic major system](https://en.wikipedia.org/wiki/Mnemonic_major_system)

Requires python>=3.6

### Convert
Convert any one or two digit number to a wordlist
```
>>> from brain_memory.majorsystem import number_to_words
>>> number_to_words(34)
['amor', 'hammer', 'hummer', 'mare', 'maria', 'marry', 'mixer', 'moor', 'mower']
```

Convert any English word to a number, the word has to be in the CMU dictionary to receive proper phonetic translations, otherwise it'll be a direct conversion; an asterisk is added if that happens.
```
from brain_memory.majorsystem import word_to_number
>>> word_to_number('cheese')
'60'
>>> word_to_number('philanthropist')
'85214901'
>>> word_to_number('doesnotexist')
'102101*'
```

### Practice
Practice converting a word to a number. For this, an internal word list is used to randomly pick a word. This is the same wordlist as the `number_to_words` function. Therefore all numbers should be between 0 and 99
```
>>> from brain_memory.train import practice_to_number, practice_to_word
>>> practice_to_number()
convert: bunny
the number: 92
correct!
```

Practice converting a one or two digit number to a word. This uses the same CMU dictionary to validate if the word is proper English. Any valid word can be used and is not restricted to the internal wordlist.
```
>>> practice_to_word()
convert: 65
a word: jail
correct!
```