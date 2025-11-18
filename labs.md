---
layout: page
title: Labs (FAQ)
description: Commonly asked questions + Hints about the lab
math: katex
---

# Labs (FAQ)

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## General

1. Is attendance mandatory for lab sessions?

    **TA Response:** No, however, it is generally recommended to go if you have time. You can get support for your questions in real-time and also network with classmates. If you want to work on the lab computers from home, once you create an EECS account, you can use <a href = "https://remotelab.eecs.yorku.ca/#/">EECS Remote Lab</a>. Please consult the <a href = "https://wiki.eecs.yorku.ca/dept/tdb/login:remotelabs-tips:start">RemoteLab Wiki</a> if you require additional assistance.

2. When do TA Office Hours start? 

    **TA Response:** We will begin offering TA office hours starting from the week of <b><i>September 15</i></b>. Additionally, we will offer support during reading week.

3. I missed a lab! What should I do?

    **TA Response:** We will only consider the best 8/10 labs so there should be no major issues. If you have missed more than two labs, please fill out the Accommodation Request Form. 

4. Which IDE should I use for this course?

    **TA Response:** Wing Personal is your best bet as a novice programmer. PyCharm is also fairly standard if you have programming experience. The teaching team recommends these two IDEs as they are supported on the lab machines. You can use any IDE (e.g., Visual Studio Code) to complete the labs.

5. Should I be using Interactive Mode or Script Mode to complete the labs?

    **TA Response:** Interactive code is convenient for testing small snippets of code. As you can imagine, it is not very good for large-scale programs; statements are not saved. Script mode is better for completing the labs as it is easier to change the code and better supports iterative development and debugging practices.

6. Do you have any advice for a 1st Year student? How can I succeed in this course (and more generally, University)?

    **TA Response:** To succeed in any course, the key is to practice everyday until you can explain the concepts seamlessly. There are many resources to practice programming such as <a href = "https://codingbat.com/python">CodingBat</a> or <a href = "https://leetcode.com/">LeetCode</a>.

    You should also keep up with course readings. A website that I found useful is <a href = "https://openstax.org/">OpenStax</a> which provides open-source textbooks to students. Some of the textbooks also have live coding environments for interactive learning.

    If you are looking for advice on how to study, I recommend checking out <a href = "https://ocul-yor.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma991036592774005164&context=L&vid=01OCUL_YOR:YOR_DEFAULT&lang=en&search_scope=OCULDiscoveryNetwork&adaptor=Local%20Search%20Engine&tab=OCULDiscoveryNetwork&query=any,contains,Letters%20to%20a%20new%20student&offset=0">Letters to a New Student: Tips to Study Smarter from a Psychologist</a>. You need to work very hard, but you also need to be efficient with your time.

    In terms of succeeding in University, my biggest advice is to get involved in activities and network with your colleagues. <a href = "https://yorku.campuslabs.ca/engage/organization/cshub">CSHub</a> is a great student club to join and learn from senior students who can offer you advice and mentorship. You can also look into becoming a Student Ambassador or Peer Helper.   

    If you are interested in research, I recommend looking into <a href = "https://studyoptions.students.yorku.ca/opportunities-beyond-the-classroom/research-at-york-ray">Research at York (RAY)</a> or <a href = "https://lassonde.yorku.ca/research/undergraduate-research-at-lassonde">Lassonde Undergraduate Research at York (LURA)</a>. In some cases, reaching out to faculty members and offering to volunteer in their lab can be effective as well. 

    As an upper year student, you can also look into taking a project or capstone course such as <a href = "https://wiki.eecs.yorku.ca/dept/project-courses/">LE/EECS 4080</a> to build interesting projects and augment your resume.

    You can increase your chances of getting a research assistant position by taking the time to read a faculty members recent work on <a href = "https://scholar.google.ca/">Google Scholar</a> and proposing a research proposal or contribution. 

7. I tried re-running my code in PrairieLearn but it won't let me. Help!

    **TA Response:** While you are able to resubmit your code as many times as you wish (up until the deadline), the teaching team has set a 5 minute cooldown for each attempt. If your code fails certain test cases, this timeout will help you spend time to debug rather than applying a brute-force approach.
<hr>

## Lab Questions & Hints

<hr>

### Lab 1 (Setup)

1. Just to clarify, what am I supposed to do/submit for the first lab?

    **TA Response:** Firstly, please navigate to: <b><i>Week 1: Introduction > Lab</i></b>. You will need to click each of the hyperlinks to complete the first two tasks; eClass automatically records your activity and gives you, "credit." Task 3 will require you to submit the relevant screenshot through eClass; you will get an e-mail confirming your submission.

2. I am using PyCharm but I cannot access interactive mode! Please help!

    **TA Response:** You should see a Python emblem near the bottom left corner of the IDE; clicking this will enable Interactive Mode. If you do not see the emblem, then please:
      - Click the, "☰" icon in the top left corner of your IDE.
      - Hover over, "View" and select Tool Windows > Python Console.

### Lab 2 (Building Blocks)

1. For Task 1, what do I submit? There were many code fragments that we were instructed to write.

    **TA Response:** Please only submit the last component (that is, from Q1.9) to PrairieLearn.

2. For Task 4, how do you get the highest score resulting from Lab 1 and Lab 2?.

    **TA Response:** The most direct way would be to use one of Python's built-in functions (Week 2 Slides, p. 140). You can also check out the documentation <a href = "https://docs.python.org/3/library/functions.html">here</a>. In future lectures, you will learn about control-flows which you can use to implement your own version of the solution.

3. I don't see any starter code for Task 5 and 6. Why is that?

    **TA Response:** You will be asked to write your own script from scratch. As such, it is important that you follow the requirements so that the autograder works properly. If you have any trouble, please feel free to drop by my office hour on Friday :)

4. How do I convert from one datatype to the other (e.g., String to Integer)?

    **TA Response:** You will need to cast the datatype using one of Python's built-in constructors (e.g., int(), float(), str(),  bool()).
    I recommend watching this <a href = "https://www.youtube.com/watch?v=Qtq83lAoogM">video</a> if you want a really strong explanation.

### Lab 3 (Building Blocks II)

1. I am having difficulty understanding Task 2. Can you give me some hints?

    **TA Response:** Understanding how to get the, "correct" answer depends on your understanding of boolean operators and <a href = "https://www.math.wichita.edu/discrete-book/section-logic-equivalences.html">logical equivalences.</a> I recommend that you watch this <a href = "https://www.youtube.com/watch?v=o4KLkur0oTE">video</a> for reference.  

2. For Task 3, I am having trouble understanding the question. Can you offer me some hints?

    **TA Response:** You are told that a child does not need to purchase a ticket if they are under the age of 6, however, having a height greater than 120 cm requires a ticket regardless of age. Try to think of the boolean conditions as, "directions." Try to make them operate in the same, "direction". You will also need to understand exactly how logical and/or work to debug the problem. 

    There is no one correct solution as boolean expressions can be written in many logically-equivalent ways.  

3. I am having trouble understanding how to validate a well-formed phone number. Can you offer me some advice?

    **TA Response:** Try to break the problem down into discrete pieces first; do not try to solve the problem in one-shot. For example, consider, "cleaning" the phone number first prior to checking that (1) it only consists of digits, and (2) has a length of 10.

    You will need to handle the potential inclusion of trailing spaces and the symbols: "-", "(", ")", " ". 

    **Hint:** A clean solution may use <a href = "https://docs.python.org/3/library/stdtypes.html#str.translate">str.translate</a> to help deal with the inclusion of non-digit characters at first!

4. Can I modify the print statements in some of the tasks?

    **TA Response:** Yes, but the modification must be very minimal. Remember that you are only supposed to print out the exact value that is being requested from the requirements. Do not make the string output fancy as the autograder will likely get very.... angry.... 

    If you experience significant issues, please come talk to me in the lab or visit office hours on Friday :)

### Lab 4 (Functions) 

1. I submitted Task 1 to PrairieLearn but the autograder gave me a mark of 0! Help!

    **TA Response:** Please check that you ``import doctest`` in your submission and run ``doctest.testmod()``. 
    
    Additionally, for your own benefit, I often recommend running ``doctest.testmod(verbose=True)`` as you can get more useful information to debug with.

2. My doctest is throwing errors when I expect an AssertionError to occur. Please help!

    **TA Response:** A limitation of doctest is that it compares the results with the expected value as a string. If your comparisons are not exactly the same (e.g., existence of whitespace), it will throw an error. Please ensure that you are writing concise doctest.

    Additionally, for AssertionError, ensure that your doctest answer follows the template:
    
    ```python
    import doctest

    def foo(name: str) -> str:
        """
        Checks the vibe of a given person.

        >>> foo('Hachi')
        'Hello Hachi, you are a cool person!'

        >>> foo(42)
        Traceback (most recent call last):
        ...
        AssertionError: invalid datatype of name
        """
        assert isinstance(name, str), 'invalid datatype of name'
        return f'Hello {name}, you are a cool person!'
    doctest.testmod(verbose=True)
    ```

3. We are asked to write at least 4 doctests per function. What is the best way to come up with test cases that are actually meaningful?

    **TA Response:** At a minimum, you should write doctests that cover each of the following equivalence classes:
    - **Happy:** A well-defined test case using known inputs that execute and produce the expected output. It does not guarantee handling of error conditions.
    - **Boundary:** Synonymous with, "edge" or, "corner" cases. They test the application under an extreme minimum or maximum argument value.
    - **Exceptional:** Used to test the application under contract-breaking (pre and post conditions!) violation(s). We want to test the robustness of the applications error handling.

4. I saw in the lab that you are using ``isinstance()`` to check the data type of your parameters. Why don't you just use ``type()``?

    **TA Response:** For the purposes of this course, we are using ``isinstance()`` because it can check whether a variable belongs to multiple data types (or subclasses). This makes the amount of code you have to write for future labs (and the lab tests) more minimal, clean, and concise.

    Once you take LE/EECS 2030, you will learn about the concept of inheritance. Another reason to use ``isinstance()`` is because it supports inheritance whereas ``type()`` does not. This will become much more important later on in your course work; don't worry about it too much for now :)

### Lab 5 (Functions II)

1. What specifically should I be submitting for Task 1 to PrairieLearn?

    **TA Response:** You need to submit the following **completed** functions with their corrected doctest. I have provided you with the skeleton code below.
    
    ```python
    import doctest

    def circle_area(radius: float) -> float:
        pass
    
    def circle_circumference(radius: float) -> float:
        pass

    doctest.testmod()
    ```

2. I have been stuck on Task 2 for a long time. Everything I try to do causes more errors. Help!

    **TA Response:** Use the debugger and step through the code line-by-line. Remember that ```x``` and ```y``` are global variables which means that they are shared across all of the functions and main method. 

    You should also consider the fact that function1 relies on **y** being instantiated to instantiate **x**.

3. I have corrected the bugs in Task 2, however, the autograder keeps giving me a final mark of 0! Help!

    **TA Response:** Please ensure that you are only submitting ```problematic_function``` to PrairieLearn.

4. For Task 4, it is recommended to decompose the functions into more modular components. Can you give me some direction?

    **TA Response:** You should modularize pieces of code that can be re-used between ```my_food_credit``` and ```opponent_food_credit```.
    
    For example, it makes sense to create methods that calculate (1) the raw credits for each participant based on their class, and (2) penalty scores based on the opponent.

    As the program becomes more sophisticated (e.g., more classes are added under consideration), it will become clear why modularizing the functions becomes useful (especially for Test-Driven Development purposes).

5.  I am completely overwhelmed by Task 5. Can you please offer me any sort of hints or tricks?

    **TA Response:** You have actually already solved a variant of this problem! The general approach to solving Task 5 is very similar to Lab 3 Task 4 (Phone Number).
    
    First, you need to validate the basic pre-conditions (e.g., data type of parameters). Following this, you slowly begin to pre-process the input and check the other pre-conditions starting from broad cases (e.g., placement of the bars) to specific ones. 

    I strongly encourage you to take a look at the test cases after you submit the preliminary code to PrairieLearn.

### Lab 6 (Control Flow)

1. What specifically should I be submitting for Task 1 to PrairieLearn?

    **TA Response:** You need to submit the following **completed** functions with their corrected doctest. I have provided you with the skeleton code below.
    
    ```python
    import doctest

    def is_prime(num: int) -> bool:
        """
        Your function description and tests go here
        """
        pass
    
    def count_primes(start: int, stop: int) -> int:
        """
        Your function description and tests go here
        """
        pass

    doctest.testmod(verbose = True)
    ```

2. I am trying to implement the Leibniz Formula for Task 3 but all of my values are slightly off. Why is this happening?

    **TA Response:** Recall that the formula is: $$\large \pi \approx 4 \times \sum\limits_{n=0}^m{\frac{(-1)^n}{2n + 1}}$$.
    
    
    You should be paying close attention to how the numerator is calculated due to order of operations:

    | Precedence Level | Operators |
    |:-------------|:--------------------------------------------------------|
    | 1            | Brackets                                                | 
    | 2            | Exponents                                               | 
    | 3            | Sign (+, -)                                             | 
    | 4            | Multiplication, Division, Modulo, At                    | 
    | 5            | Addition, Subtraction                                   |
    | 6            | Less Than, LEQ, Greater Than, GEQ, Equals, Not Equal To |
    | 7            | Logical Negation $$(\neg)$$                             |
    | 8            | Logical And $$(\wedge)$$                                |
    | 9            | Logical Or $$(\vee)$$                                   |

    Also, do note the following equivalences between for loops and mathematical notation. $$\large \sum\limits_{i=0}^{10}{i}$$ is equivalent to the following Python loop:
    
    ```python
    sum = 0
    for i in range(0, 11, 1):
        sum += i
    print(sum)
    ```

3. I am having trouble with the Caesar Cipher shifting (Task 4). I don't understand how to support the wrap-around.

    **TA Response:** Remember that in ASCII, A-Z is represented as 65-90. The wrap-around can be implemented by making smart use of the modulo (%) operator and accounting for the numerical shifts to keep values between 65 and 90. 

    Additionally, you could use a String alphabet to simplify the solution so that you don't need to account for the offset, however, there is a small memory overhead.

4. To solve Task 5, is it necessary to use a for loop?

    Not necessarily; the same outcome can be achieved by using string slicing!

### Lab 7 (Collections I)

1. How can we check whether the numbers (after splitting) do not contain illegal characters (such as alphabetical characters)? Moreover, how can we ensure that the method accepts an arbitrary number of ints or floats? 

    **TA Response:** Think back to Lab 5, Task 5 (```absolute_value(str)```); Once you get the list of numbers after splitting by, "\|", you need to pre-process each number and check that it is well-formed.

    You can validate if the number is initially well-formed by replacing legal (non-digit characters) with the empty string and then using str.isdigit() in an assertion.

    You should still check that the following properties are met prior to casting the string into an int / float:

    - Whitespaces are removed (replaced/stripped).
    - If there is a positive sign ('+') in the string, that it is in the correct (legal) position. 
    - If there is a negative sign ('-') in the string, that it is in the correct (legal) position.
    - If there is a decimal sign ('.') in the string, that it is in the correct (legal) position.
    - If there is an, 'e' operator in the string, that it is in the correct (legal) position.
    - That the counts of operators makes sense. 
    
    
2. For Task 2, is there a more optimal way to check whether all of the items in ```input_list``` are non-negative integers? 

    **TA Response:** Yes; you will learn about it next week. The more efficient way to write the code would be to leverage <a href = "https://www.w3schools.com/python/python_lists_comprehension.asp">list comprehension</a> with the built-in <a href = "https://www.w3schools.com/python/ref_func_all.asp">all(iterable, /)</a> function.

3. I am having a lot of difficulty with Task 4. Can you please give me some hints? Do I need to write my own sorting function?

    **TA Response:** You should check out the documentation <a href = "https://docs.python.org/3/howto/sorting.html">here</a> for more help. You do not need to write your own sorting algorithm for this problem. 

4. For Tasks 6/7, I am having a great deal of difficulty with determining when to throw an AssertionError. Can you provide me with some ideas?

    **TA Response:** Think broadly; try writing a boolean condition that uses the length of the collection as an upper bound against the index. You also need to consider boundary cases where you try to remove any index from an empty collection.

    It may help you to consider how ```bool()``` works by providing collections of different sizes to the constructor. Try running the following lines in the interactive shell:
    ```python
    # Empty List
    bool([])
    # Empty Tuple
    bool(())
    # Empty Set 
    bool(set())
    # Empty Dict 
    bool({})

    # Non-Empty List
    bool([1])
    # Non-Empty Tuple
    bool((1000,)) 
    # Non-Empty Set 
    bool({1, 2, 3, 4})
    # Non-Empty Dictionary
    bool({'hello': 'world'})
    ```

### Lab 8 (Collections II)
1. I am unsure of what's happening with Task 1! I submit the code to PrairieLearn but the autograder says that my signature annotation is wrong. What should I do!? AHHHHH!!!!

    **TA Response:** The autograder will not accept signature annotations that use imports from the typing module. Use the built-in annotations
    that do not require an import.

2. I am really lost with Task 2. The code that they gave us is giving me a headache! Can you offer some advice?

    **TA Response:** The first step should be to fix syntax errors (e.g., missing indentation, imports, etc.,) After this has been done, I recommend:

    - Ensuring the consistency of expected data types.
    - Validating the boolean conditions for your branches.
    
    It is also very important that you understand the difference between **continue** and **break**.
    I suggest that you refer <a href = "https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements">here</a> for additional clarification. 

3. For Task 3, how do I keep track of the most frequent numbers?

    **TA Response:** Solving this question relies on your mastery of the dict() data structure. Consider the following before you begin implementing:

    - For each number, you need to record how many times it appears in the list. (What do you think the key-value pairs should represent?)
    - Afterwards, you need to determine the maximum value for the number of appearances.
    - You can iterate through the key-value pairs of the dictionary to identify the numbers which should appear in the final solution.

    I strongly recommend that you take a read through **help(dict)** in the interactive shell.
    Please speak with me in the lab or during office hours for additional assistance.

### Lab 9 (Collections III)

1. What specifically should I be submitting for Task 1 to PrairieLearn?

    **TA Response:** You need to submit the following **completed** functions with their corrected doctest. I have provided you with the skeleton code below.
    
    ```python
    import doctest

    def is_odd(num: int) -> bool:
        """
        Your function description and tests go here
        """
        pass
    
    def separate_numbers(nested_list: list[list[int]]) -> dict[str, dict[str, list[int]]]:
        """
        Your function description and tests go here
        """
        pass
    doctest.testmod(verbose = True)
    ```

    **Do note use the type annotations from typing or the Autograder will not work properly!**

2. I am having a lot of difficulties with Task 2. I feel like I have fixed most of the issues but my doctest is still failing! Can you offer me some advice or hints?

    **TA Response:** I highly suggest that you implement and test each module in isolation. 
    
    Once you are sure that each of the components works correctly, you can rebuild the program and submit the final code.

3. For Task 2, my IDE is showing a Lint Error in the signature annotation's return type. Why is this?

    **TA Response:** You need to explicitly define the Tuple annotation. You can fix it by replacing ```(List[int], float)``` with ```Tuple[List[int], float]```.
    
    Please remember that you will also need to add the following import statement: ```from typing import List, Tuple```.

4. I've been stuck on Task 3 for hours! I don't know what methods I am allowed to touch/modify.

    **TA Response:** I recommend approaching the problem in the following way:
    - Review the game logic found in ```play_tic_tac_toe()```. You will need to understand this to start working backwards and implementing the helper functions properly.
    - Implement and evaluate ```initialize_board()```. 
    - Implement and evaluate ```drop_piece()```.
    - For ```is_winner()```, implement each of the win-condition checkers as a separate helper method:

    ```
        (i) Check for horizontal win-con
        (ii) Check for vertical win-con
        (iii) Check for diagonal win-con type 1 (Top-Left to Bottom-Right)
        (iv) Check for diagonal win-con type 2 (Top-Right to Bottom Left)
    ```
    **Note:** You should not modify the provided code ```print_board()```, ```play_tic_tac_toe()``` in any capacity.

    Some other tips that may help:
    - Checking for a vertical/horizontal win-condition will require a nested for-loop. 
    - If you transpose the board (hint: <a href = "https://docs.python.org/3/library/functions.html#zip">zip()</a>), you can re-use your horizontal win-condition checker for the vertical check. Do note that this approach will require you to understand tuple unpacking as well.
    - Checking for a diagonal win-condition will only require 1 for-loop.
    - You can use the <a href = "https://docs.python.org/3/library/functions.html#all">all()</a> function in tandem with for-loops and/or list comprehension to succinctly check for a win-condition.
    - **The biggest conundrum comes from understanding how to properly index the board.** I recommend drawing out a board with each cell containing the numerical indexes to discover the underlying pattern(s) required to check for win-conditions with nested for-loops. This should make things substantially more clear :)

    If you still require additional help, please speak to me in the lab or during office hours! 
    
    This lab is a bit trickier than the past ones so don't feel bad if it takes you more time to pass all of the test-cases on PL :) 

### Lab 10 (Classes & Objects)

1. TBD

    **TA Response:** TBD