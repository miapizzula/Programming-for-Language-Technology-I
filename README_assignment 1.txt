
A) First you should make a function which you will call find_largest and which will accept a single mandatory argument, which:

If the argument is a list of numbers, then the function will return the largest number in the list
If the argument is a number, the function will simply return the number
If the argument is anything else, the function will return 0
For example, calling find_largest([2, 5, 32, 64, -2]) will return 64.

B) Next you need to make a function that you will call find_largest_from_the_two that will accept two lists of numbers as arguments and return the 
largest number from both lists. 
To implement the second function you must use the find_largest function that you implemented earlier. 
If one gives as one of the 2 arguments something other than a list of numbers, the same rules as described above should apply.

For example the call find_largest_from_the_two([2, -5, 32, 126], [0, -6, 122, 1000]) will return us 1000.

To simplify your code, assume that if the argument is a list, then the list will contain numbers, meaning you don't need to check the data type inside each list.



