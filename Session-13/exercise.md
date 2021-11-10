# No. 1
Create a new dictionary called ```prices```

Put these key and values in your ```prices``` dictionary:
- "Banana": 4
- "Apple": 2
- "Orange": 1.5
- "Pear": 3

Create a new dictionary called ```stocks```

Put these key and values in your ```stocks``` dictionary:
- "Banana": 6
- "Apple": 0
- "Orange": 32
- "Pear": 15

Loop through each key in ```prices```. For each key, print out the key along with its price and stock information. Print the answer in the following format:
```zsh
Apple
Price: 2
Stock: 0
```

Let's determine how much money you would make if you sold all of your food

- Create a variable called "total" and set it to zero
- Loop through the ```prices``` dictionary. For each key in ```prices```, multiply the number in ```prices``` by the number in ```stocks```. Print that value into the terminal and then add it to total
- Finally, outside your loop, print total

```zsh
Banana: 24
Apple: 0

Total: 24
```

# No. 2
Use the same two dictionaries you defined in No. 1

Create a list called ```groceries``` with the values "Banana", "Pear", and "Orange"

- Define a function ```compute_bill``` that takes one argument ```food``` as a parameter. In the function, create a variable total with an initial value of zero. For each item in the food list, add the price of that item to total. Finally, return the total. Ignore whether the item you're billing for is in stock. Note that your function should work for any food list.

- Make the following changes to your ```compute_bill``` function (overwrite the function after it's defined):
  - While you loop through each food item, only add the price of the item to total if the item's stock count is greater than zero.
  - If the item is in stock, after you add the price to the total, subtract one from the item's stock count
