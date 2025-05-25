from tasks import add_task, remove_task, list_tasks, mark_completed, filter_tasks
from storage import save_tasks, load_tasks

# Prompt: # Function to show main CLI menu
def show_menu():
    """
    Виводить головне меню для користувача з усіма опціями.
    """
    print("\nОберіть опцію:")
    print("1. Додати завдання")
    print("2. Видалити завдання")
    print("3. Позначити як виконане")
    print("4. Показати всі завдання")
    print("5. Показати лише виконані / активні")
    print("6. Вийти")

# Prompt: # Function to choose task priority with input validation
def get_priority():
    """
    Отримує від користувача числовий пріоритет завдання.

    :return: ціле число (1-3), що відповідає рівню пріоритету
    """
    print("Оберіть пріоритет:")
    print("1 — Високий 🔥")
    print("2 — Середній ⏳")
    print("3 — Низький 💤")
    p = input("Введіть 1, 2 або 3: ")
    if p not in ('1', '2', '3'):
        print("Невірне значення пріоритету. Встановлено за замовчуванням: 2.")
        return 2
    return int(p)

# Prompt: # Main program loop with task manager functionality
def main():
    """
    Основна функція застосунку. Обробляє взаємодію з користувачем:
    додавання, видалення, оновлення, перегляд та фільтрацію завдань.
    """
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Введіть номер опції: ")

        if choice == '1':
            title = input("Введіть назву завдання: ")
            priority = get_priority()
            add_task(tasks, title, priority)
            save_tasks(tasks)

        elif choice == '2':
            list_tasks(tasks, header="🗑️ Виберіть завдання для видалення:")
            try:
                idx = int(input("Введіть номер завдання для видалення: ")) - 1
                remove_task(tasks, idx)
                save_tasks(tasks)
            except ValueError:
                print("❌ Введіть числовий індекс.")

        elif choice == '3':
            list_tasks(tasks, header="☑️ Виберіть завдання для позначення як виконаного:")
            try:
                idx = int(input("Введіть номер завдання, яке виконано: ")) - 1
                mark_completed(tasks, idx)
                save_tasks(tasks)
            except ValueError:
                print("❌ Введіть числовий індекс.")

        elif choice == '4':
            list_tasks(tasks, header="📋 Всі завдання:")

        elif choice == '5':
            print("Оберіть статус для фільтрації:")
            print("виконані — лише завершені")
            print("активні — ті, що ще не виконано")
            status_input = input("Введіть статус (виконані / активні): ").lower()

            # Prompt: # Convert Ukrainian input into task status keywords
            if status_input == "виконані":
                status = "completed"
                print("✅ Виконані завдання:")
            elif status_input == "активні":
                status = "active"
                print("🟢 Активні завдання:")
            else:
                print("❌ Невірний статус.")
                continue

            filter_tasks(tasks, status)

        elif choice == '6':
            save_tasks(tasks)
            print("Завдання збережено. До побачення!")
            break
        else:
            print("Невірна опція. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
