https://edabit.com/challenge/K9w9hEd9Pn7DtMzjs

# Return the Highest and Lowest Numbers

Create a function that accepts a string of space separated integers and returns the highest and lowest integers (as a string).

# Example

```
"1 2 3 4 5" ➞ "5 1"

"1 2 -3 4 5" ➞ "5 -3"

"1 9 3 4 -5" ➞ "9 -5"

"13" ➞ "13 13"
```

# Notes

* All integers are valid, no need to validate them.

* There will always be at least one integer in the input string.

* Output string must be two integers separated by a single space, and highest number is first.

# Tests

```
Test.assert_equals(high_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
Test.assert_equals(high_low("1 -1"), "1 -1")
Test.assert_equals(high_low("1 1"), "1 1")
Test.assert_equals(high_low("-1 -1"), "-1 -1")
Test.assert_equals(high_low("1 -1 0"), "1 -1")
Test.assert_equals(high_low("1 1 0"), "1 0")
Test.assert_equals(high_low("-1 -1 0"), "0 -1")
Test.assert_equals(high_low("42"), "42 42")
```
