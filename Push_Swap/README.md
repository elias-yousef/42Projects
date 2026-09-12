*This activity has been created as part of the 42 curriculum by eabushak, mkhashan.*

# Push_swap: Adaptive Sorting

## Description
This project is an advanced variation of the classic 42 Push_swap activity. Instead of relying on a single sorting algorithm, our program implements an *Adaptive Strategy*. It analyzes the "disorder" of the input stack (a metric between 0.0 and 1.0) and dynamically selects the most efficient algorithm to sort the integers using the lowest possible number of operations, and you can choose between 4 methods (simple, medium, complex, adaptive).

The goal is to sort data on a stack, with a limited set of instructions, using the lowest possible number of actions.

## Instructions

### Compilation
To compile the push_swap binary, simply run:

```make```

Execution

Run the program with a list of integers as arguments:

```./push_swap 4 67 3 87 23```

You can also force specific strategies or enable benchmark mode using flags:

```--simple: Force O(n²) algorithm.```

```--medium: Force O(n√n) algorithm.```

```--complex: Force O(n log n) algorithm.```

```--adaptive: Default behavior (selects based on disorder).```

```--bench```: Displays detailed statistics (disorder %, operation counts) to stderr.

# Algorithm Justification

**```--simple```**

The alogrithm used:
Selection Sort: A straightforward O(n2) algorithm that iteratively scans the stack for the minimum element, rotates it to the top, and pushes it to a temporary stack. This process is repeated until the main stack is empty, ensuring the elements are sorted when pushed back.
How it works:
Imagine holding a hand of cards. You look through them to find the smallest one, pull it out, and place it face-up on the table. You keep doing this until your hand is empty. Finally, you pick up the pile from the table, and your hand is now perfectly sorted.

**```--medium```**

Here we implement a bucket sort algorethim using two stacks with limited operations so at first we index the numbers so each node has it's index value then insert the node in specific range into stack b and chagne the rang untill stack a become empty then tack back all node to stack a from smallest one to the biggest.

**```complex```**

The alogrithm used:
radix Sort (Bitwise LSD): A non-comparative algorithm that processes numbers by their binary representation. It sorts integers by distributing them into two stacks based on the value (0 or 1) of each bit, starting from the least significant bit, guaranteeing a stable sort in O(n⋅logn) time.
How it works:
Instead of comparing numbers to each other, we look at them in binary (base 2). We sort them bit-by-bit. First, we sort them based on the last bit, then the second-to-last, and so on. By using Stack B as a temporary bucket for the "0s" and Stack A for the "1s", the list naturally becomes sorted after checking all bits.
Our adaptive engine selects one of three algorithms based on the calculated disorder d:

**```adaptive```**

1. Low Disorder (d < 0.2)

    Selected Algorithm: Simple Sort (Optimized Bubble Pass)

    Complexity: O(n) target

    Rationale: When the stack is nearly sorted (low disorder), complex setup costs (like bucket allocation) are wasteful. A simple pass that swaps adjacent inverted elements fixes local errors instantly with minimal overhead.

2. Medium Disorder (0.2 <= d < 0.5)

    Selected Algorithm: Chunk Sort (Butterfly Algorithm)

    Complexity: O(n√n)

    Rationale: We divide the stack into √n chunks based on value ranges. By pushing chunks to Stack B, we create a roughly sorted "hourglass" shape. This allows us to push elements back to Stack A efficiently. It balances the cost of pushing vs. rotating, which is optimal for medium-randomness datasets.

3. High Disorder (d >= 0.5)

    Selected Algorithm: Radix Sort (Bitwise LSD)

    Complexity: O(n log n)

    Rationale: When data is highly random, comparison-based sorts struggle. Radix Sort processes numbers bit-by-bit (base 2). This guarantees a stable runtime proportional to the number of bits (log n), making it the most reliable choice for highly disordered large stacks (e.g., 500 random numbers).

# Resources

## Documentation:

Introduction to Algorithms (CLRS) - For understanding Big-O complexity.

GeeksforGeeks - For Radix Sort implementation details.

## AI Usage:

AI tools were used to help debug specific segmentation faults in the linked list implementation.

AI assistance was used to generate test cases for the benchmark parser and to format this documentation.