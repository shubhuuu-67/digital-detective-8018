# Mission 4 - How programs run

## 1. Task / objective
Create and run a basic Python script from Terminal and compare how compilers and interpreters translate and run source code.

## 2. Work completed

**Task 4.1 - Create and run a Python program**
Created `hello.py` inside `mission-04-programs` containing `print("Hello from Python")` and executed it in Terminal with `python3`. The output `Hello from Python` appeared cleanly in the terminal.

**Task 4.2 - Compare compiler and interpreter**

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| When translation / execution happens | Translates the entire source code into machine code before the program starts running. | Reads and executes the source code line by line while the program is running. |
| Typical output | Creates a separate standalone executable file that the computer can run directly. | Does not produce a separate executable file; runs the script directly and shows the output. |
| One example | C or C++ (using GCC or Clang). | Python (using `python3`). |
| One advantage | Runs very fast once compiled because the machine code is already prepared for the processor. | Makes testing and fixing mistakes quicker since changes run immediately without a separate build step. |

As shown in the comparison table above, the main difference between a compiler and an interpreter is when translation happens. A compiler converts the entire program into a separate executable file ahead of time, which allows languages like C++ to run fast once built. An interpreter like Python reads and carries out instructions one line at a time at runtime without creating a standalone binary, making it quick to test small scripts like `hello.py`.

## 3. Commands / tools used
- `echo` and `cat` to create `hello.py` with the print statement and verify its contents.
- `python3 mission-04-programs/hello.py` to execute the Python script from Terminal.
- `code mission-04-programs/README.md` to open and edit the documentation in VS Code.
- `git add`, `git commit`, and `git push` to save and upload Mission 4 to GitHub.

## 4. My understanding
Computers only understand low-level machine instructions, so human-readable code has to be translated before the CPU can act on it. Compilers and interpreters handle that translation differently, with compilers building an executable file first and interpreters running code step by step on the fly. Knowing this makes it clear why Python scripts can be run immediately from Terminal with `python3`.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-04-programs/hello.py` (one-line Python script printing `"Hello from Python"`)
- `mission-04-programs/README.md` (program execution notes and compiler vs. interpreter comparison)

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Status: Committed and pushed to the `main` branch on GitHub.