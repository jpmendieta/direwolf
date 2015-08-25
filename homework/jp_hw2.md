# Homework 2

## Command Line Chipotle

* Each column is defined by the **header field names** (order_id, quantity, item_name, choice_description, item_price). 
`head chipotle.tsv`
* Each row is an an item that was ordered by a hungry chipotle customer.
* There appear to be 1834 orders.
`tail chipotle.tsv` 
* There are 4623 lines in the file.
`wc chipotle.tsv`
* The chicken burrito is more popular.
`grep -i 'Steak Burrito' chipotle.tsv | wc -l`
**368**
`grep -i 'Chicken Burrito' chipotle.tsv | wc -l`
**553**
* Hmm, not sure how to find whether black beans or pinto beans are more popular in chicken burritos.
* **./data/chipotle.tsv** and  **./data/sms.tsv**
`find . -name *.tsv`
* 10 counts of the word dictionary in DAT8
`grep -ri 'dictionary' *.* | wc -w`