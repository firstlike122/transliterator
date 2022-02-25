# Welcome to Transliterator!

Hi! I'm your first Markdown file in **Transliterator**. If you want to learn about Transliterator, you can read me. 

# Installition
```bash
$ pip install transliteration
```
## Download files

**https://github.com/firstlike122/transliterator**

## Configuring
``` sh
>>> from transliterator.transliterator import Transliteration as tr*
```

## Transliterate any 'text'
```sh
>>> tr('Hello').tr_text  # Ҳэлло
>>> tr('Hello').text     # Hello
```

# Functions
for use functions in transliteration you must get Transliteration object.
For example:
```sh
>>> from transliterator.transliterator import Transliteration as tr
>>> trnsltr = tr()
```  

## transliterate
```sh
>>> trnsltr.transliterate('Hello') # Ҳэлло
```
## transliterator
```sh
>>> trnsltr.transliterator('Hello', c2l, c2l_compounds) # Hello
```
>c2l_compounds and c2l are dictioanries which contains alphabets.
## isLang
```sh
>>> trnsltr.isLang('Hello', c2l) # True
```
## from_file
```sh
>>> trnsltr.from_file('test.txt') # Hello
```
## to_file
```sh
>>> trnsltr.to_file('Hello', 'test.txt') # Ҳэлло (in test.txt)
```
## f2f
```sh
>>> trnsltr.f2f('test.txt', 'test2.txt') # Hello(in test.txt) to Ҳэлло (in test2.txt)
```
## to_self 
```sh
>>> trnsltr.to_self('test.txt') # Hello(in test.txt) to Ҳэлло (in test.txt which to itself)
```