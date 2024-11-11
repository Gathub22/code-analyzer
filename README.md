# code-analyzer
A simple code analysis tool to get language use statistics about your coding project.

![imagen](https://github.com/user-attachments/assets/8ce5109b-4932-44c1-a392-c8ddb7a245d1)

With this script you can know:
- Most written language.
- Number of files written with each language.
- Number of characters written in each language.
- Analysis filter between programming and markup languages.

It works by assuming the language of each file's content by it's file extension. However this repository it's open for any suggestions to improve accuracy. 

## Usage
```
main.py [-P -M] [your/proyect/location/.]
```

> [!WARNING]
> Note: the location must always end with ".".

If no location has been passed, the script will assume the location from which is running. (.)

Optional arguments:

`-P` lists files only written with programming languages (C/C++, Java, PHP, Python...)

`-M` lists files only written with markup languages (XML, CSS, HTML...)

## Recognized languages

| Language          | Type       |
|-------------------|------------|
| Assembly          | Programming|
| Batch             | Programming|
| C                 | Programming|
| C#                | Programming|
| C++               | Programming|
| CSS               | Markup     |
| HTML + CSS/JS/PHP | Markup     |
| Java              | Programming|
| JavaScript        | Programming|
| JSON              | Markup     |
| Kotlin            | Programming|
| Lua               | Programming|
| Perl              | Programming|
| PHP               | Programming|
| Python            | Programming|
| Ruby              | Programming|
| Rust              | Programming|
| Shell             | Programming|
| Squirrel          | Programming|
| XML               | Markup     |

## Requirements
- Tested in Python 3.13.0, but it should work in any Python 3.X version

## Contributing
Found a bug? Please [open an issue](https://github.com/Gathub22/code-analyzer/issues/new/choose) to review it inmmediately.

If you want to improve this code:
- You should fork the main branch and work on your changes there.
- Once you're done, create a PR. If it fixes a GitHub issue, link it.
- If it's approved your changes will be merged into the main branch.

If it's approved, your name, email address and merge commit link will be written into the CONTRIBUTORS file :)
