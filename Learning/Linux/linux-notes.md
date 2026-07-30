# Linux Notes and Questions

## What is Linux?

Linux is an **operating system kernel**, not an entire operating system by itself. A kernel is the core software that sits between applications and the computer's hardware. It manages things like the CPU, memory, storage devices, networking, and hardware drivers.

A Linux "operating system" (called a **distribution**, or *distro*) combines the Linux kernel with additional software such as command-line tools, desktop environments, libraries, and package managers.

Examples of Linux distributions include:

- Ubuntu
- Debian
- Fedora
- Arch Linux
- Linux Mint

### Analogy

Think of the kernel as the **engine of a car**.

The operating system is the **entire car** built around that engine.

Applications communicate with the kernel, and the kernel communicates with the hardware.

---

## Why do servers use Linux?

Linux is extremely popular for servers because it is:

- Free and open source
- Stable and reliable
- Highly customizable
- Secure
- Efficient with system resources
- Excellent for automation and scripting
- Supported by a massive developer community

Unlike Windows, Linux can run with only the software that is actually needed, making it ideal for cloud servers and backend infrastructure.

Today, the majority of web servers, cloud servers, supercomputers, and embedded systems run Linux.

---

## Kernel vs Operating System

One thing I misunderstood at first was the difference between a kernel and an operating system.

The **kernel** manages hardware resources.

The **operating system** is everything the user interacts with, including:

- Terminal
- File system
- Desktop environment
- Applications
- Package manager
- System utilities

The operating system relies on the kernel to communicate with the computer's hardware.

---

## GUI vs Terminal

A graphical user interface (GUI) is simply another program running on top of Linux.

Examples include:

- GNOME
- KDE Plasma
- XFCE

The GUI is **not** Linux itself.

Linux works perfectly without a GUI, which is one reason servers usually don't have one installed.

---

## Absolute vs Relative Paths

### Absolute Path

An absolute path always starts from the root directory and points to the full location of a file.

Examples:

```text
/home/brennon/Documents/notes.txt
```

or on Windows:

```text
C:\Users\Brennon\Documents\notes.txt
```

Absolute paths always point to the same location regardless of where you currently are.

---

### Relative Path

A relative path starts from your current working directory.

Examples:

```text
notes/day2.txt
```

```text
../Projects
```

Relative paths depend entirely on where you currently are.

---

## Important Commands Learned

```bash
pwd        # Print Working Directory
ls         # List directory contents
cd         # Change directory
cd ..      # Move up one directory
mkdir      # Make directory
touch      # Create empty file (Linux)
cp         # Copy files/directories
mv         # Move or rename files
rm         # Remove files
cat        # Display file contents
whoami     # Show current user
which      # Locate where a command is installed
sudo       # Run a command as an administrator
```

Git Bash on Windows doesn't include every Linux utility by default (for example, `touch` may or may not be available depending on the environment), but you'll use these constantly once we move to WSL.

---

## Linux File System

Unlike Windows, Linux does not organize storage using drive letters like C: or D:.

Instead, everything begins from one root directory:

```text
/
```

Everything—including hard drives, USB drives, and files—is attached somewhere underneath this root.

This is one of Linux's biggest conceptual differences from Windows.

---

## Things That Surprised Me

- The Linux terminal isn't nearly as intimidating as I expected.
- Git Bash feels very similar to Linux because it provides a Bash shell with many Unix-style commands.
- The command line is much faster than clicking through folders once I know the commands.
- I now understand that VS Code, Git Bash, and File Explorer are simply different ways of interacting with the same files on my computer.

---

## Questions I Still Have

- How exactly do applications communicate with the kernel?
- What happens inside the kernel when I type a command like `ls`?
- How does Linux know which hardware driver to use?
- Why are Linux file permissions structured the way they are?
- What exactly are `/bin`, `/sbin`, `/usr`, and `/etc`, and what purpose does each serve?
- Why do some user accounts have access to `sudo` while others do not?
- What are environment variables, and how do they affect command execution?