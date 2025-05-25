import json

def save_tasks(tasks, filename='tasks.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Помилка збереження: {e}")

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Помилка завантаження: {e}")
        return []
