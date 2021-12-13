# **Exercise 1:**

You are given words. Some words may repeat. For each word, output its
number of occurrences. The output order should correspond with the input
order of appearance of the word. See the sample input/output for
clarification.

**Note:** Each input line ends with a **"\\n"** character.

**Constraints:**

1 ≤ n ≤ 10<sup>5</sup>

The sum of the lengths of all the words do not exceed 10<sup>6</sup> All
the words are composed of lowercase English letters only.

## **Input Format**

The first line contains the integer, **n**.

The next **n** lines each contain a word.

## **Output Format**

Output 2 lines.

On the first line, output the number of distinct words from the input.

On the second line, output the number of occurrences for each distinct
word according to their appearance in the input.

**Sample Input:**  

```
4  
bcdef  
abcdefg  
bcde  
bcdef 
```
**Sample Output:**  

```
3  
2 1 1  
```
## **Explanation**

There are 3 distinct words. Here, **"bcdef"** appears twice in the input
at the first and last positions. The other words appear once each. The
order of the first appearances are **"bcdef"**, **"abcdefg"** and
**"bcde"** which corresponds to the output.

# **Exercise 2:**

**Lexicographical order** is often known as alphabetical order when
dealing with strings. A string is greater than another string if it
comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its
characters. This new word must meet two criteria:

> ● It must be greater than the original word  
> 
> ● It must be the smallest word that meets the first condition  

## **Example**
```
w = abcd
```

The next largest word is **abdc**.

Create the function bigger_Is_greater and return the new string meeting
the criteria. If it is not possible, return **no answer**.

## **Function Description**

Function has the following parameter(s):

● string w: a word

**Returns**

\- string: the smallest lexicographically higher string possible or **no
answer**

## **Input Format**

The first line of input contains **T**, the number of test cases. Each
of the next **T** lines contains **w**.

**Constraints**

> ● 1 ≤ **T** ≤ 10<sup>5</sup>  
> 
> ● 1 ≤ length of **w** ≤ 100  
> 
> ● **w** will contain only letters in the range ascii\[a...z\]  

**Sample Input:**
```
5  
ab  
bb  
hefg  
dhck  
dkhc  
```

**Sample Output:**  
```
ba  
no answer  
hegf  
dhkc  
hcdk
```

**Explanation**  
● Test case 1:  
  `ba` is the only string which can be made by rearranging `ab`. It is greater.  

● Test case 2:  
  It is not possible to rearrange `bb` and get a greater string.  

● Test case 3:  
  `hegf` is the next string greater than `hefg`.

● Test case 4: 
  `dhkc` is the next string greater than `dhck`.  
  
● Test case 5:  
  `hcdk` is the next string greater than `dkhc`.

**Sample Input:**  
```
6  
lmno  
dcba  
dcbb  
abdc  
abcd  
fedcbabcd  
```

**Sample Output:**  
```
lmon  
no answer  
no answer  
acbd  
abdc  
fedcbabdc  
```

# **Exercise 3:**

Bomberman lives in a rectangular grid. Each cell in the grid either
contains a bomb or nothing at all.

Each bomb can be planted in any cell of the grid but once planted, it
will detonate after exactly 3 seconds. Once a bomb detonates, it's
destroyed — along with anything in its four neighboring cells. This
means that if a bomb detonates in cell *i, j*, any valid cells ( i ± 1,
j ) and ( i, j ± 1 ) are cleared. If there is a bomb in a neighboring
cell, the neighboring bomb is destroyed without detonating, so there's
no chain reaction.

Bomberman is immune to bombs, so he can move freely throughout the grid.
Here's what he does:

> 1\. Initially, Bomberman arbitrarily plants bombs in some of the
> cells, the initial state.
>
> 2\. After one second, Bomberman does nothing.
>
> 3\. After one more second, Bomberman plants bombs in all cells without
> bombs, thus filling the whole grid with bombs. No bombs detonate at
> this point.
>
> 4\. After one more second, any bombs planted exactly three seconds ago
> will detonate.
>
> Here, Bomberman stands back and observes.
>
> 5\. Bomberman then repeats steps 3 and 4 indefinitely.

Note that during every second Bomberman plants bombs, the bombs are
planted simultaneously (i.e., at the exact same moment), and any bombs
planted at the same time will detonate at the same time.

Given the initial configuration of the grid with the locations of
Bomberman's first batch of planted bombs, determine the state of the
grid after **N** seconds.

For example, if the initial grid looks like:
```
...
.O.
...
```
It looks the same after the first second. After the second second,
Bomberman has placed all his charges:
```
OOO
OOO
OOO
```
At the third second, the bomb in the middle blows up, emptying all
surrounding cells:
```
O.O
...
O.O
```
## **Function Description**

Create the bomber_man function with following parameter(s):

> ● int n: the number of seconds to simulate
>
> ● string grid\[r\]: an array of string that represents the grid

## **Returns**

● string\[r\]: n array of string that represent the grid in its final
state

**Sample Input:**
```
3
.......
...O...
....O..
.......
OO.....
OO.....
```
**Sample Output:**  
```
OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO
```  

# **Project**:

## **REST URL Shortener API**

URL shortening is a technique on the World Wide Web in which a Uniform
Resource Locator (URL) may be made substantially shorter and still
direct to the required page. This is achieved by using a redirect which
links to the web page that has a long URL. For example, the URL
"https://example.com/assets/category_B/subcategory_C/Foo/" can be
shortened to

"https://example.com/Foo", and the URL
"https://en.wikipedia.org/wiki/URL_shortening" can be shortened to
"https://w.wiki/U". Often the redirect domain name is shorter than the
original one. A friendly URL may be desired for messaging technologies
that limit the number of characters in a message (for example SMS), for
reducing the amount of typing required if the reader is copying a URL
from a print source, for making it easier for a person to remember, or
for the intention of a permalink. In November 2009, the shortened links
of the URL shortening service Bitly were accessed 2.1 billion times.

Other uses of URL shortening are to "beautify" a link, track clicks, or
disguise the underlying address. Although disguising of the underlying
address may be desired for legitimate business or personal reasons, it
is open to abuse.\[2\] Some URL shortening service providers have found
themselves on spam blocklists, because of the use of their redirect
services by sites trying to bypass those very same blocklists. Some
websites prevent short, redirected URLs from being posted.

Required features:

> \- API to create URL with random short name (something like this
> url/78sda8s6d), url random name should be fixed size string and unique
> per url
>
> \- API for premium clients to create URL with custom name
> (url/\<custom>)
>
> \- Input url validation, that it is a correct url and size must be
> below 250 characterAu
>
> \- Counters - how many times the url was accessed (optional
> requirement)
>
> \- Automatic deletion of urls older than 30 days (optional
> requirement)
