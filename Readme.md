# 📌 Advanced Calculator - Homework3

This is an **Advanced Calculator** that extends the Intermediate Calculator by adding **calculation history management**.  
It follows **Object-Oriented Programming (OOP)** principles and **SOLID design**, ensuring modular and maintainable code.

---

## 🚀 Features

✔️ Supports **Addition (+), Subtraction (-), Multiplication (×), and Division (÷)**  
✔️ Implements **Encapsulation** with a `Calculation` class  
✔️ Uses **Static Methods** in the `Calculator` class  
✔️ Uses **Class Methods** in the `Calculations` class for history management  
✔️ Handles **division by zero** with exception handling  
✔️ Fully **unit tested using pytest** (100% test coverage)  
✔️ **Pylint compliant** (Expected score: **7+/10**)  
✔️ **Modular Code** following **SOLID & DRY principles**  

---

## ⚙️ Installation & Usage

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/Satyabandi20/homework3.git
cd homework3
```

### **2️⃣ Create and Activate a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```
---

## 🛠️ Running Tests

### **Run Pytest**

```bash
pytest --cov=calculator tests/
```

✔️ **Expected Output:**  
```
TOTAL                           78      0   100%
========================== All tests passed ==========================
```

### **Run Pylint for Code Quality Check**

```bash
pylint calculator/
```

✔️ **Expected Pylint Score:** **7+/10**  

---

## 📜 Code Explanation

### **`Calculation` Class**
- Encapsulates a **single arithmetic operation**.
- Stores **two operands**, the **operation**, and the **result**.

### **`Calculations` Class**
- Uses **class methods** to **store and retrieve past calculations**.
- Implements **methods for retrieving history, clearing history, and getting the latest calculation**.

### **`Calculator` Class**
- Uses **static methods** to perform operations.
- Calls the `Calculations` class to store and retrieve past results.

### **`operations.py`**
- Defines **basic arithmetic functions** (`add`, `subtract`, `multiply`, `divide`).

---

## 🏁 Submission

🔗 **GitHub Repository:** [Satyabandi20/homework3](https://github.com/Satyabandi20/homework3)  

---

✔️ Ensure **all tests pass**  
✔️ Ensure **100% test coverage**  
✔️ Ensure **Pylint score is 7+/10**  
🚀 **Ready for submission!**

