# Reverse Words in a String

## 📘 Problem Summary

You are given a string `sentence` that may contain:

- Leading spaces  
- Trailing spaces  
- Multiple spaces between words  

Your task is to **reverse the order of the words** without changing the order of characters inside each word.

```
Note: A word is defined as a continuous sequence of non-space characters. Multiple words separated by single spaces form a valid English sentence. Therefore, ensure there is only a single space between any two words in the returned string, with no leading, trailing, or extra spaces.
```

### ✔ Requirements

- Words must appear in **reverse order**
- Characters **inside each word must stay the same**
- Output must contain **a single space** between each pair of words
- **No leading or trailing spaces**
- Input may contain any number of spaces anywhere
- A *word* is a continuous sequence of **non-space characters**

### ✔ Example  
Input:
```
"  hello   world  "
```

Output:
```
"world hello"
```

---

## 🧠 Constraints

- Sentence contains English letters, digits, and spaces  
- Sentence length is between **1 and 10⁴**
- There is at least **one word**

---

## 🚀 Solution Approach

This solution uses a classic **two‑pointer, in‑place string manipulation** technique.   The algorithm is optimal, clean, and does **not** rely on Python shortcuts like `split()`.

### The algorithm has 3 main steps:

---

### **1️⃣ Reverse the entire string**

Example:

```
"hello   world"
```

→ After full reverse:

```
"dlrow   olleh"
```

This puts the words in reverse order, but reverses each word as well.

---

### **2️⃣ Reverse each word individually**

We scan for word boundaries and reverse each word:

```
"dlrow   olleh"
 → reverse "dlrow" → "world"
 → reverse "olleh" → "hello"
```

Now we have:

```
"world   hello"
```

Words are correct, spacing is not.

---

### **3️⃣ Remove extra spaces**

Using two pointers:

- Copy non-space characters  
- Skip multiple spaces  
- Insert only **one space** when appropriate  
- Avoid leading/trailing spaces  

Result:

```
"world hello"
```

---

## ⏱ Complexity

| Step              | Time     | Space       |
| ----------------- | -------- | ----------- |
| Reverse full list | O(n)     | O(1)        |
| Reverse each word | O(n)     | O(1)        |
| Remove spaces     | O(n)     | O(n) output |
| **Total**         | **O(n)** | **O(n)**    |

This is optimal.

---

## 🧪 Example Test Cases

```
Input: "hello world"
Output: "world hello"

Input: "  hello world  "
Output: "world hello"

Input: "a good   example"
Output: "example good a"

Input: "the sky   is blue"
Output: "blue is sky the"

Input: "   hello    world    test   "
Output: "test world hello"
```

---

## ✅ Summary

This solution:

- Handles **all spacing edge cases**
- Uses **two‑pointer techniques**
- Reverses **in-place**
- Runs in **linear time**
- Produces **clean, correct output**  
