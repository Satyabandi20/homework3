# 📌 Intermediate Calculator - Homework3

This is an **Intermediate Calculator** that extends the basic functionality by implementing **Object-Oriented Programming (OOP)** principles.  
It introduces a **Calculation class** to encapsulate arithmetic operations and uses **static methods** in the `Calculator` class.

---

## 🚀 Features

✔️ Supports **Addition (+), Subtraction (-), Multiplication (×), and Division (÷)**  
✔️ Implements **Encapsulation** with a `Calculation` class  
✔️ Uses **Static Methods** in the `Calculator` class  
✔️ Handles **division by zero** with exception handling  
✔️ Fully **unit tested using pytest**  
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

### **`Calculator` Class**
- Uses **static methods** to perform operations.
- Calls the `Calculation` class to store and retrieve results.

---

## 🏁 Submission

🔗 **GitHub Repository:** [Satyabandi20/homework3](https://github.com/Satyabandi20/homework3)  

---

✔️ Ensure **all tests pass**  
✔️ Ensure **Pylint score is 7+/10**  
🚀 **Ready for submission!**

