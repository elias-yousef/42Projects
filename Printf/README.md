*This activity has been created as part of the 42 curriculum by eabushak.*

# ft_printf

## Description

The **ft_printf** project is a reimplementation of the standard C `printf` function.  
The goal of this project is to understand variadic functions, formatted output, low-level I/O using `write`, and number representation in both decimal and hexadecimal.

This implementation supports a subset of the original `printf` format specifiers while respecting the 42 Norm.

Supported conversions:
- `%c` character
- `%s` string
- `%d` / `%i` signed decimal integer
- `%u` unsigned decimal integer
- `%x` lowercase hexadecimal
- `%X` uppercase hexadecimal
- `%p` pointer address
- `%%` percent sign

---

## Instructions

### Compilation

To compile the project, run:

```bash
make
```

This will generate the static library:

```text
libftprintf.a
```

### Usage

Include the header file in your project:

```c
#include "ft_printf.h"
```

Compile your program with:

```bash
cc main.c libftprintf.a
```

Example:

```c
ft_printf("Hello %s, number = %d\n", "world", 42);
```

---

## Algorithm and Technical Choices

- Variadic arguments are handled using `va_list`, `va_start`, `va_arg`, and `va_end`.
- The format string is parsed character by character.
- Each conversion specifier is handled by a dedicated function for clarity and Norm compliance.
- Numbers are printed using recursion to ensure correct digit order.
- Hexadecimal values are produced using base-16 conversion.
- Pointer addresses are printed with the `0x` prefix, and `(nil)` is printed when the pointer is `NULL`.
- All output is written using the `write` system call.

---

## Resources

- The C Programming Language – Kernighan & Ritchie
- `man printf`
- `man stdarg`
- GNU C Library documentation
- 42 Network documentation

### Use of AI

AI tools were used strictly as a learning aid to:
- understand variadic functions and recursion
- clarify pointer handling and edge cases
- review logic during development

All code was written, tested, and understood by **eabushak**.

---

## Author

**eabushak**  
42 Network
