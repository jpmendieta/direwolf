# Class 3 Notes

* Pre-class notes
  * pull updates from DAT8 repo before class starts
`git pull origin master`
  * to commit updates:
    1. git add <filename>
    2. git status
    3. git commit -m “updating file”
    4. git push origin master

* Git & Github slides
  * gist.github.com
  * .gitignore
  * github.com/github/gitignore
  * To escape Vim— `:q!`
* hw2 review
  * the **c** option prints the word count in grep (so don’t have to pipe it to `wc`) 
`grep -ic ‘chicken burrito” chipotle.tsv`
  * grep returns lines, not words. the following does a word count of all the words in the lines returned: `grep -ir ‘dictionary’ . | wc -w`
  * better way is to get an approximate by counting the lines that came back from the grep that had the word dictionary `grep -ir ‘dictionary’ . |wc -l`
  * `grep -ir ‘dictionary’ . | tr ‘ ‘ ‘\n’ | grep -i ‘dictionary’`
  * `grep -ir ‘dictionary’ . | tr ‘ ‘ ‘\n’ | grep -i ‘dictionary’ | wc -l`
* Python exercise
  * create a dictionary from 2 arrays
    1. zip creates list of tuples
    2. dict converts the list into a dictionary
`dict(zip(airlines, incidents))`