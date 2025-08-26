import os

def create_problem(topic, number, name):
    # Normalize folder name: 3-digit padded number
    folder_name = f"{int(number):03d}-{name.lower().replace(' ', '-')}"
    path = os.path.join(topic, folder_name)

    if os.path.exists(path):
        print(f"⚠️ Problem already exists: {path}")
        return

    os.makedirs(path)
    print(f"📂 Created folder: {path}")

    # README.md template
    readme_content = f"""# {int(number):03d}. {name.title()}

**Link**: [LeetCode - {name.title()}](https://leetcode.com/problems/{name.lower().replace(' ', '-')}/)

---

## Problem
description

---

## Example
### Normal
- Input: 
- Output: 

### Edge
- Input: 
- Output: 

### Invalid
- Input: 
- Output: 

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - 

---

## Complexity
- **Time**: O(?)
- **Space**: O(?)

---

## Pitfalls
- 

---
"""

    with open(os.path.join(path, "README.md"), "w") as f:
        f.write(readme_content)
    print("📝 Created README.md")

    # solution.py boilerplate
    solution_content = """
def TODO(self):
    pass
"""
    with open(os.path.join(path, "solution.py"), "w") as f:
        f.write(solution_content)
    print("🐍 Created solution.py")


if __name__ == "__main__":
    # Ask user for inputs interactively
    topic = input("Enter topic/folder name (e.g., arrays, linked_list): ").strip()
    number = input("Enter problem number (e.g., 20): ").strip()
    name = input("Enter problem name (e.g., Valid Parentheses): ").strip()

    # Create topic folder if it doesn't exist
    if not os.path.exists(topic):
        os.makedirs(topic)
        print(f"📂 Created topic folder: {topic}")

    create_problem(topic, number, name)