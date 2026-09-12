*This activity has been created as part ofthe 42 curriculum by eabushak*

# get_next_line

<p align="center">
  <img src="https://img.shields.io/badge/42-School-blue" />
  <img src="https://img.shields.io/badge/Language-C-green" />
</p>

---

## 📌 Description

**get_next_line** is a function that reads from a file descriptor and returns **one line per call**.

- Reads data using a fixed `BUFFER_SIZE`
- Returns a line ending with `\n` if present
- Returns `NULL` when there is nothing left to read
- Handles files, standard input, and EOF correctly

---

## 🧠 How it works

<details>
<summary>Click to expand explanation</summary>

- The function reads `BUFFER_SIZE` bytes at a time using `read()`
- Data is stored in a **static stash** to keep leftover content
- When a newline `\n` is found:
  - The line is extracted and returned
  - The remaining content is saved for the next call
- When EOF is reached:
  - Remaining content is returned if it exists
  - Otherwise, `NULL` is returned

</details>

---




## Resources
GNL pdf file

AI for understanding

some websites like geeksforgeeks

## ⚙️ Compilation & Usage

Compile with a custom buffer size:

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 *.c


