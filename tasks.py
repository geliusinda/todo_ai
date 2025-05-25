# Prompt: # Function to add a task with optional priority
def add_task(tasks, title, priority=2):
    """
    Додає нове завдання до списку.

    :param tasks: список існуючих завдань
    :param title: назва нового завдання
    :param priority: числовий пріоритет (1-3)
    """
    task = {"title": title, "completed": False, "priority": priority}
    tasks.append(task)
    print("✅ Завдання додано успішно.")

# Prompt: # Function to remove task by index with validation
def remove_task(tasks, index):
    """
    Видаляє завдання за індексом.

    :param tasks: список завдань
    :param index: індекс завдання для видалення
    """
    if 0 <= index < len(tasks):
        task = tasks.pop(index)
        print(f"🗑️ Завдання '{task['title']}' видалено.")
    else:
        print("❌ Невірний індекс.")

# Prompt: # Function to mark task as completed
def mark_completed(tasks, index):
    """
    Позначає завдання як виконане.

    :param tasks: список завдань
    :param index: індекс завдання для оновлення
    """
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("☑️ Завдання позначено як виконане.")
    else:
        print("❌ Невірний індекс.")

# Prompt: # Function to display all tasks with header and formatting
def list_tasks(tasks, header=None):
    """
    Виводить список завдань з опціональним заголовком.

    :param tasks: список завдань
    :param header: заголовок перед виводом
    """
    if header:
        print(header)
    if not tasks:
        print("📭 Список порожній.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['title']} [{status}] Пріоритет: {task['priority']}")

# Prompt: # Filter tasks by completed or active and display them
def filter_tasks(tasks, status):
    """
    Фільтрує завдання за статусом: виконані або активні.

    :param tasks: список усіх завдань
    :param status: 'completed' або 'active'
    """
    if status == "completed":
        filtered = [t for t in tasks if t["completed"]]
    elif status == "active":
        filtered = [t for t in tasks if not t["completed"]]
    else:
        print("❌ Невірний статус.")
        return
    list_tasks(filtered)
