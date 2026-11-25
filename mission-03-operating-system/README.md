# Mission 3 - Understand the operating system

## 1. Task / objective
Check my operating system details, active account, free storage, and running processes in Terminal. Practice using absolute and relative paths, check file permissions, and explain the core responsibilities of an operating system.

## 2. Work completed

**Task 3.1 - Explore your operating system**

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| Operating system / system details (`sw_vers` and `uname -m`) | Shows the OS name, version number, build version, and chip architecture. | macOS 27.2.1 (Build 26B131) running on Apple Silicon (`arm64`). |
| Current account identity (`whoami`) | Shows the username of the account currently logged in and running commands. | `[redacted]` |
| Available and used storage (`df -h /`) | Shows the main drive's total size, used space, and available free space. | Main drive (`/`) is 460Gi total with 13Gi used and 333Gi available (4% capacity used). |
| System activity snapshot (`ps -eo pid,comm \| head -n 12`) | Lists active background and user processes along with their process IDs. | Showed core macOS system services running in the background, starting with `/sbin/launchd` at PID 1. |

**Task 3.2 - Understand processes**

- **What is a process?** A process is a program that is currently loaded in memory and actively running on the computer.
- **What does the PID column represent?** PID stands for Process Identifier. It is a unique number assigned by the operating system to every running process so the OS can track and manage it individually.
- **Two examples of processes running on my computer:** `/sbin/launchd` (PID 1, the main macOS service manager) and `/usr/libexec/logd` (PID 533, the system logging daemon).

**Task 3.3 - Understand paths and permissions**

When I checked `pwd` inside `terminal-practice`, the path showed the full nested location inside `mission-02-terminal`. Running `cd ../..` moved two levels up and brought me back to the main `digital-detective-8018` folder.

- **Difference between an absolute path and a relative path:** An absolute path starts all the way from the root folder (`/`) and gives the complete address of a file or folder from anywhere on the system. A relative path describes where something is starting from the folder you are currently inside.
- **Absolute path example:** `/Users/[redacted]/Desktop/digital-detective-8018/mission-02-terminal/terminal-practice/log.txt`
- **Relative path example:** `mission-02-terminal/terminal-practice/log.txt` (when starting from `digital-detective-8018`)

Running `ls -l log.txt` showed `-rw-r--r--` at the start of the line. The first `-` means it is a regular file, and the next three characters `rw-` show the owner's permissions. This means the owner can **read** and **write** (edit) the file, but cannot **execute** it as a program (`-` instead of `x`).

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| r - Read | Allows reading a file's contents or viewing the files inside a folder. | Reading `log.txt` with `cat` or opening it in VS Code. |
| w - Write | Allows editing, saving changes to, or deleting a file. | Appending a new line of text to `log.txt`. |
| x - Execute | Allows running a file as a program or script, or entering a folder. | Running a script in Terminal or moving into a folder with `cd`. |

**Task 3.4 - Explain operating-system responsibilities**

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| Process management | Starts, schedules, and stops running programs so multiple apps can share the CPU smoothly. | Running VS Code, Terminal, and Chrome at the same time. |
| Memory management | Gives active programs space in RAM and frees that memory when apps close. | Allocating RAM for open browser tabs and releasing it when they close. |
| Device management | Connects software to physical hardware and accessories through drivers. | Taking typing input from the keyboard and sending display output to the screen. |
| File management | Organizes data into files and folders on the drive and tracks where they are stored. | Saving `README.md` inside the `mission-03-operating-system` folder. |
| User interface / shell | Provides a way for users to control the computer visually or through text commands. | Navigating folders in Finder or running commands in `zsh`. |
| Security and permissions | Controls which accounts and apps can read, change, or run specific files. | Protecting system files so regular user accounts cannot accidentally alter them. |

## 3. Commands / tools used
- `sw_vers` and `uname -m` to check the macOS version, build, and processor architecture.
- `whoami` to check the logged-in account name (redacted in notes).
- `df -h /` to check total, used, and available disk space.
- `ps -eo pid,comm | head -n 12` to inspect active processes and their PIDs.
- `pwd`, `cd`, and `ls -l` to check folder paths and file permissions.
- `git add`, `git commit`, and `git push` to save and upload Mission 3 to GitHub.

## 4. My understanding
The operating system manages all hardware and software activity behind the scenes. It assigns every active program a unique PID, keeps track of RAM and SSD storage, and enforces read, write, and execute permissions so files stay protected. Knowing how absolute and relative paths work also makes moving around in Terminal much easier.

## 5. Difficulties faced
When I ran `cd mission-02-terminal/terminal-practice`, Terminal showed `cd: no such file or directory` because I was already inside the `terminal-practice` folder from the previous mission.

## 6. How I resolved them
I checked `pwd` to confirm my current location, inspected `log.txt` directly, and used `cd ../..` to return to the root `digital-detective-8018` folder.

## 7. Evidence / files
- `mission-03-operating-system/README.md` containing the system observations, process answers, path and permission notes, and OS responsibilities table.

## 8. Commit details
- Commit message: `Document operating system and file management`
- Status: Committed and pushed to the `main` branch on GitHub.