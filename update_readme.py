import os
import re

# Root README file
README_FILE = "README.md"

def extract_problem_info(topic, folder_name):
    """
    Extracts problem number and title from folder name like '001-two-sum'
    Returns (#, title, topic, relative_link)
    """
    match = re.match(r"(\d{3})-(.+)", folder_name)  # 3-digit padded number
    if not match:
        return None
    
    number = int(match.group(1))
    title = match.group(2).replace("-", " ").title()
    relative_link = f"{topic}/{folder_name}"
    return (number, title, topic, relative_link)


def gather_problems():
    problems = []
    for topic in os.listdir("."):
        if not os.path.isdir(topic) or topic.startswith(".") or topic == "__pycache__":
            continue
        # Scan topic folders
        for folder in os.listdir(topic):
            folder_path = os.path.join(topic, folder)
            if os.path.isdir(folder_path):
                info = extract_problem_info(topic, folder)
                if info:
                    problems.append(info)
    return sorted(problems, key=lambda x: x[0])


def update_readme(problems):
    # Read existing README
    with open(README_FILE, "r") as f:
        content = f.read()
    
    # Build new table
    header = "| #   | Title | Topic | Solution |\n|-----|-------|-------|----------|\n"
    rows = []
    for num, title, topic, link in problems:
        rows.append(f"| {num} | {title} | {topic.capitalize()} | [Link]({link}) |")
    table = header + "\n".join(rows)

    # Count total problems
    total_count = len(problems)

    if re.search(r"(### ✅ Problems Solved: )(\*{0,3}\d+\*{0,3})", content):
        new_content = re.sub(
            r"(### ✅ Problems Solved: )(\*{0,3}\d+\*{0,3})",
            f"\\1***{total_count}***",
            content,
        )
    else:
        # If not present, insert it above the problem index section
        new_content = re.sub(
            r"(## 📑 Problem Index)",
            f"### ✅ Problems Solved: ***{total_count}***\n\n\\1",
            content,
        )

    # Replace Problem Index section
    new_content = re.sub(
        r"(## 📑 Problem Index\n\n)([\s\S]*?)(\n---)",
        f"\\1{table}\\3",
        new_content,
    )

    # Write back
    with open(README_FILE, "w") as f:
        f.write(new_content)
    print(f"✅ README updated! ({total_count} problems solved)")


if __name__ == "__main__":
    problems = gather_problems()
    update_readme(problems)