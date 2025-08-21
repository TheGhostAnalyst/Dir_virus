
# 🐍 Dir_virus - Simulated File Flooder

A Python script that simulates a basic "file virus" by generating hundreds or thousands of random `.txt` files. Great for learning Python file handling, automation, and practicing resource-aware scripting.

> ⚠️ **Disclaimer**  
> This is a harmless educational project. It does not contain real malware. Use responsibly in test environments.

---

## 📁 Features

- Creates a user-defined number of files.
- Each file has a random alphanumeric name.
- File content matches the file name (or can be modified).
- Written using Python's built-in `random`, `string`, and `os` modules.

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed  
- A terminal or shell environment  
- A test folder (highly recommended)

---

### 📦 Clone the Repository
```
git clone https://github.com/TheGhostAnalyst/Dir_virus.git
cd Dir_virus
````



### ▶️ Run the Script

```bash
python3 virus.py
```

Edit the script to set how many files you want:

```python
length = 12  # Length of each file name and content
long = 100   # Number of files to create
```

---

## 💻 Example Output

```bash
Simulated virus has been created as aB92kdLsQf7Z.txt
Simulated virus has been created as Jk02s9DhLqYx.txt
...
```

You’ll see these files appear in the same directory as the script.

---

## 🧠 Why This Project?

* Practicing file I/O in Python
* Learning about automation and loops
* Simulating high-load environments for testing
* Understanding system limitations when working with bulk file operations

---

## 🧼 Cleanup Tip

To delete the generated files (Linux/macOS):

```bash
rm *.txt
```

For Windows (PowerShell):

```powershell
Remove-Item *.txt
```

---

## 📌 Notes

* DO NOT run this in sensitive system directories.
* Avoid running with excessive file counts unless you're stress testing (and know what you're doing).
* Use a test folder or VM if going above 10,000 files.

---

## 🧠 Author

**The Ghost Analyst**

> *"Hack with purpose. Learn with fire. Stay unseen."*

GitHub: [@TheGhostAnalyst](https://github.com/TheGhostAnalyst)

---

## 🛡️ License

This project is licensed under the MIT License — see the `LICENSE` file for details.

