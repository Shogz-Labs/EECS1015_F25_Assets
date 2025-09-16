---
layout: page
title: Labs (FAQ)
description: Commonly asked questions + Hints about the lab
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
<hr>