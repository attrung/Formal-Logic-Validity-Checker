# Formal Logic Validity Checker

<p><strong>This program was written as a work at my Minerva Schools at KGI, as the first optional challenge in my Formal Analyses class. </strong></p>

<p> The python file include functions that return a truth table and the validity of the argument. 

This code begin by allowing user to input information, including number of premises, number of atomic sentences,
 atomic sentences, the premises, and the conclusion. Certain requirements are need for the premises, such as there 
must be no space and use connectives as followed: ¬ (not), ^ (and), / (or), ? (imply), ? (if and only if), along with () (parenthesis).

*I used / instead of v for "or" because user might input "v" as an atomic sentence*

Then, the computer will iterate through 2^n situation, each with a different combination of truth values for the atomic sentences. 

For each iteration:

    The premises and conclusion is then processed through process_truth_value_premise(), which change the atomic sentences into 
    True and False values accordingly. 

    Next, they are passed through parenthesis(), which merges all the parts in the parenthesis into a list. Parts outside of 
    parenthesis remain the same. This is so that further running of the code will consider those in parenthesis first. 

    The code is then passed through truth_value(), where the truth value is determined through multiple steps.  They are 
    analyzed beginning with parenthesis, then negation, then and/or, then conditionals, and finally biconditionals.
    
    Finally, validity is determined basing on two criteria ("there exist a situation where all premises are true and the 
    conclusion is true" and "there is no situations where all the premises are true, but the conclusion is false").

Finally the code print "Valid" or "Invalid" basing on the criteria met.

It is suggested that the number of variables is kept as low as possible. If there are more than 12 symbols, the code takes some 
time to run. (since it is in the order of 2^n)

Below are some example test cases.

Example 1 (this deductive argument):

    Number of premises: 3
    Number of atomic sentences: 4
    Atomic sentence 1: a
    Atomic sentence 2: b
    Atomic sentence 3: c
    Atomic sentence 4: d

    Premise 1: ¬(a^b)?c
    Premise 2: a^b?d
    Premise 3: ¬d
    Conclusion: c
    
#### Answer: Valid

Example 2:

    Number of premises: 2
    Number of atomic sentences: 4
    Atomic sentence 1: x
    Atomic sentence 2: y
    Atomic sentence 3: z
    Atomic sentence 4: g
    Premise 1: ¬(x^(y/z))?g
    Premise 2: ¬x^(y/z)
    Conclusion: g
    
#### Answer: Valid
    
Example 3: (the reversed argument above)

    Number of premises: 3
    Number of atomic sentences: 4
    Atomic sentence 1: a
    Atomic sentence 2: b
    Atomic sentence 3: c
    Atomic sentence 4: d
    Premise 1: ¬(a^b)^¬d
    Premise 2: (a^b)^¬c
    Premise 3: c
    Conclusion: ¬d

#### Answer: Invalid </p>
