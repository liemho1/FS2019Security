# pa01 - Bash Caesar

![Hail Caesar](huuugeCaesar.jpg)

* Your job on this assignment is to use the Python3 code from the book for the Caesar cracker while writing an almost identical program in bash.
* The source files to mimic or use for inspiration include the Caesar hacker and the detecting English module.
* We will use the exact same symbol set as the book code: 
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
* I have also included the `dictionary.txt` from class in this repo, so you don't forget to copy it in.
* This assignment should help you both learn python and bash a bit better, and cover the basics of cracking cryptography.

## Deliverables
`bash-caesar.sh`

## How your program will be run
```sh
bash bash-caesar.sh <sample_cipher_text.txt >sample_decrypted_text.txt
```

## How you should test your program
```sh
bash bash-caesar.sh <sample_cipher-text.txt >my_output.txt
diff sample_decrypted_text.txt my_output.txt
```
This should result in no diffs.
`<file and >file` are for redireting standard input and standard output:
https://en.wikipedia.org/wiki/Standard_streams

## Notes
* You CAN use the book code as guidance, just converting the algorithm there. 
* As always, this should be independent work!
* If you're going to copy elemental bash commands from the internet, make sure you UNDERSTAND them, and make sure it's not larger chunks of code!

## Due date
On Canvas.

