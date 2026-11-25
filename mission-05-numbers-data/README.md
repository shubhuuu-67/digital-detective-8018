# Mission 5 - Numbers and data

## 1. Task / objective
Practice converting numbers between decimal, binary, and hexadecimal by hand, verify the results using Python, build a Python number converter script, and explain how computers store text using character encoding.

## 2. Work completed

**Task 5.1 - Convert numbers by hand**

| Question | Your working and answer |
| :--- | :--- |
| Convert decimal 13 to binary. | Divide 13 by 2 repeatedly and record remainders: 13 / 2 = 6 (R 1), 6 / 2 = 3 (R 0), 3 / 2 = 1 (R 1), 1 / 2 = 0 (R 1). Reading remainders from bottom to top gives **1101**. |
| Convert decimal 25 to binary. | Divide 25 by 2 repeatedly: 25 / 2 = 12 (R 1), 12 / 2 = 6 (R 0), 6 / 2 = 3 (R 0), 3 / 2 = 1 (R 1), 1 / 2 = 0 (R 1). Reading remainders from bottom to top gives **11001**. |
| Convert binary 1010 to decimal. | Multiply each bit by its power of 2: (1 x 8) + (0 x 4) + (1 x 2) + (0 x 1) = 8 + 0 + 2 + 0 = **10**. |
| Convert binary 1101 to decimal. | Multiply each bit by its power of 2: (1 x 8) + (1 x 4) + (0 x 2) + (1 x 1) = 8 + 4 + 0 + 1 = **13**. |
| Convert hexadecimal A to decimal. | In base 16, the letter A stands for 10, so A in decimal is **10**. |
| Convert hexadecimal 1F to decimal. | Multiply each digit by its power of 16 (where F = 15): (1 x 16) + (15 x 1) = 16 + 15 = **31**. |
| Convert binary 1111 to hexadecimal. | First convert 1111 to decimal: 8 + 4 + 2 + 1 = 15. In hexadecimal, 15 is represented as **F**. |

**Task 5.2 - Verify using Python**

| Expression tested | Python result | Matches manual calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes (`1101` with Python's `0b` binary prefix) |
| `bin(25)` | `'0b11001'` | Yes (`11001` with Python's `0b` binary prefix) |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `int("A", 16)` | `10` | Yes |
| `int("1F", 16)` | `31` | Yes |
| `hex(0b1111)` | `'0xf'` | Yes (`f` with Python's `0x` hexadecimal prefix) |

**Task 5.3 - Build a small number converter**

Created `number_converter.py` in this folder and tested it with three positive numbers from Terminal:

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| 10 | `0b1010` | `0xa` |
| 25 | `0b11001` | `0x19` |
| 42 | `0b101010` | `0x2a` |

**How the conversion functions work:** Python's `int()` turns the text typed by the user into a whole integer. Then `bin()` takes that integer and returns its base-2 binary string starting with `0b`, while `hex()` returns its base-16 hexadecimal string starting with `0x`.

**Task 5.4 - How is text stored?**

- **ASCII decimal codes:** Uppercase `A` is **65** and lowercase `a` is **97**.
- **Why computers need an encoding standard:** Computers can only store and process binary numbers (0s and 1s), so an encoding standard is needed to give every letter, digit, and symbol a consistent numeric code that all devices can read properly.
- **Character not in basic ASCII:** The Indian Rupee symbol (`₹`) or emojis like `😊` are not part of basic 7-bit ASCII and require UTF-8 encoding.

## 3. Commands / tools used
- `python3` to open the Python interactive shell and run `number_converter.py`.
- `input()`, `int()`, `bin()`, and `hex()` inside Python to read user input and convert integers into binary and hexadecimal strings.
- `code` to open and edit `number_converter.py` and `README.md` in VS Code.
- `git add`, `git commit`, and `git push` to save and upload Mission 5 to GitHub.

## 4. My understanding
Everything inside a computer eventually comes down to binary digits (bits), while hexadecimal gives programmers a shorter way to read groups of four bits at a time. Writing `number_converter.py` showed how Python handles base conversions directly with built-in functions, and learning ASCII and UTF-8 made it clear how numbers map back to readable text on screen.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py` (working decimal-to-binary and hexadecimal converter)
- `mission-05-numbers-data/README.md` (manual conversion steps, Python checks, test results, and text encoding answers)

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Status: Committed and pushed to the `main` branch on GitHub.