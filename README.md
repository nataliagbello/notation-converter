# notation-converter

This project was developed as part of the Algorithms and Data Structures course at Universidade Federal do Rio de Janeiro (UFRJ). The goal was to implement an algorithm to transform Infix mathematical expressions into Postfix and Prefix notations. By using a Stack data structure, the system acesses its LIFO (Last In, First Out) property, which is ideal to manage operator precedence and parentheses handling.

### Conversion Logic
* **Infix to Postfix:** * Uses a **dictionary of weights** to define operator precedence.
    * Implementation uses two stacks: `op_stack` (for operators) and `output_stack` (for the final expression).
    * Handles left-associative operators (+, -, *, /) and includes a specific exception rule for **exponentiation ($)**, which is right-associative.
* **Infix to Prefix:** * Involves **expression reversal** (including parentheses flip).
    * Applies a modified postfix logic where tie-breaking rules for operator weights are inverted.
    * The final result is reversed again to achieve the correct prefix notation.

### Numerical Evaluation
The calculation is performed on the **Postfix expression**. The algorithm iterates through the list, pushing operands to a stack and popping them when an operator is encountered to perform the math, until only the final result remains.

###  Complexity Analysis
The nature of this problem is defined as $\Omega(n)$, as every element of the input must be processed at least once. Since the proposed algorithm achieves a time complexity of $O(n)$ by handling the expression in a single pass with efficient stack operations, $\Omega(n) = O(n)$, the implementation is considered optimal.

### Testing the algorithm
To test the converter, simply run the script. A default test expression is provided at the bottom of the file.

  

 
