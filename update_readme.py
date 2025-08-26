import os
import re

# Root README file
README_FILE = "README.md"

# Problem directories live inside topic folders
TOPICS = ["arrays", "linked_list", "dp", "graphs", "trees", "backtracking", "heap", "binary_search", "sliding_window"]

def extract_problem_info(path, folder_name):
    """
    Extracts problem number and title from folder name like '001-two-sum'
    Returns (#, title, topic, relative_link)
    """
    match = re.match(r"(\d+)-(.+)", folder_name)
    if not match:
        return None
    
    number = int(match.group(1))
    title = match.group(2).replace("-", " ").title()
    topic = os.path.basename(path)
    relative_link = f"{path}/{folder_name}"
    return (number, title, topic, relative_link)


def gather_problems():
    problems = []
    for topic in TOPICS:
        if not os.path.exists(topic):
            continue
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

    # Replace Problem Index section
    new_content = re.sub(
        r"(## 📑 Problem Index\n\n)([\s\S]*?)(\n---)",
        f"\\1{table}\\3",
        content,
    )

    # Write back
    with open(README_FILE, "w") as f:
        f.write(new_content)
    print("✅ README updated!")


if __name__ == "__main__":
    problems = gather_problems()
    update_readme(problems)