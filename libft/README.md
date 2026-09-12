*This activity has been created as part of the 42 curriculum by eabushak.*

-------------------------------------------------------------------------------
Description
-------------------------------------------------------------------------------

This project is a programming activity developed as part of the 42 curriculum.
Its objective is to strengthen fundamental skills in C programming through the
creation of a reusable library while respecting strict coding rules and best
practices.

The project focuses on:
- Clean and readable code
- Proper memory management
- Modular design
- Full compliance with the 42 Norm

The resulting library is intended to be reused in future 42 projects.

-------------------------------------------------------------------------------
Instructions
-------------------------------------------------------------------------------

Compilation:

This project is written in C.

To compile the project:
    make

To remove object files:
    make clean

To remove all compiled files, including the library:
    make fclean

To recompile everything from scratch:
    make re

-------------------------------------------------------------------------------
Usage
-------------------------------------------------------------------------------

Once compiled, the generated library can be linked to other C projects using the
compiler flags defined in the Makefile.

Example:
    gcc main.c -L. -lft

-------------------------------------------------------------------------------
Library Description
-------------------------------------------------------------------------------

This project includes a custom C library composed of reusable utility functions.

The library provides:
- String manipulation functions
- Memory allocation and handling utilities
- Character and number processing functions

All functions are written in accordance with the 42 Norm, ensuring:
- Safe memory usage
- Clear structure
- Consistent naming conventions

This library is designed to be reused in future 42 projects.

-------------------------------------------------------------------------------
Resources
-------------------------------------------------------------------------------

The following resources were used during the development of this project:
- 42 intra documentation
- Linux manual pages (man gcc, man malloc, man free)
- https://en.cppreference.com
- https://man7.org/linux/man-pages/

-------------------------------------------------------------------------------
AI Usage
-------------------------------------------------------------------------------

AI was used as a support tool to clarify C programming concepts, improve
documentation quality, and assist in structuring this README file.

All implementation logic and final code decisions were made by the student.

-------------------------------------------------------------------------------
Author
-------------------------------------------------------------------------------

eabushak

-------------------------------------------------------------------------------

All functions are written in accordance with the 42 Norm, ensuring safe memory usage, clear structure, and consistent naming conventions. This library is designed to be reused in future 42 projects.
Author
eabushak
