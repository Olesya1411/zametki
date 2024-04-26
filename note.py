import json
import datetime
import os

NOTES_FILE = 'notes.json'

def create_note():
    try:
        note_id = input("Ввод ID: ")
        title = input("Название: ")
        body = input("Содержание: ")
        created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note = {
            "id": note_id,
            "title": title,
            "body": body,
            "created_date": created_date
        }
        return note
    except Exception as e:
        print("Ошибка во время создания заметки:", e)
        return None

def save_notes(notes):
    try:
        with open(NOTES_FILE, 'w') as file:
            json.dump(notes, file, indent=4)
    except Exception as e:
        print("Ошибка во время создания заметки:", e)

def read_notes():
    try:
        if not os.path.exists(NOTES_FILE):
            print("Не найдено.")
            return

        with open(NOTES_FILE) as file:
            notes = json.load(file)
            for note in notes:
                print("ID: ", note["id"])
                print("Title: ", note["title"])
                print("Body: ", note["body"])
                print("Created on: ", note["created_date"])
                print()
    except Exception as e:
        print("Ошибка во вреям чтения:", e)


def filter_notes_by_date(date):
    try:
        if not os.path.exists(NOTES_FILE):
            print("Не найдено.")
            return []

        with open(NOTES_FILE) as file:
            notes = json.load(file)
            filtered_notes = [note for note in notes if note["created_date"].split()[0] == date]
            if not filtered_notes:
                print("Не найдено заметок по дате.")
                return []

            print("Заметки по дате:")
            for i, note in enumerate(filtered_notes):
                print(f"{i+1}. ID: {note['id']}, Title: {note['title']}")
            return filtered_notes
    except Exception as e:
        print("Ошибка:", e)
        return []


def print_selected_note(filtered_notes):
    try:
        if not filtered_notes:
            return

        choice = int(input("Введите количесвто заметок для просмотра: "))
        selected_note = filtered_notes[choice - 1]
        print("Selected note:")
        print("ID: ", selected_note["id"])
        print("Title: ", selected_note["title"])
        print("Body: ", selected_note["body"])
        print("Created on: ", selected_note["created_date"])
    except (IndexError, ValueError):
        print("Неверное количество. Введите другое значение.")

def edit_note(note_id):
    try:
        if not os.path.exists(NOTES_FILE):
            print("Не найдено.")
            return

        with open(NOTES_FILE, 'r') as file:
            notes = json.load(file)

        for note in notes:
            if note["id"] == note_id:
                title = input("Новый заголовок: ")
                body = input("Новое содержание: ")
                note["title"] = title
                note["body"] = body
                note["created_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break

        save_notes(notes)
    except Exception as e:
        print("Ошибка при редактировании:", e)

def delete_note(note_id):
    try:
        if not os.path.exists(NOTES_FILE):
            print("Не найдено")
            return

        with open(NOTES_FILE, 'r') as file:
            notes = json.load(file)

        notes = [note for note in notes if note["id"] != note_id]
        save_notes(notes)
    except Exception as e:
        print("ошибка при удалении:", e)

def main():
    while True:
        print("1. Создать заметку")
        print("2. Читать заметку")
        print("3. Читать по дате")
        print("4. Вывод выбранной заметки")
        print("5. Редактировать")
        print("6. Удалить")
        print("7. Искать по дате")
        print("8. Выход")

        choice = input("Введите ваше значение: ")

        try:
            if choice == "1":
                note = create_note()
                if note:
                    if not os.path.exists(NOTES_FILE):
                        save_notes([note])
                    else:
                        with open(NOTES_FILE, 'r') as file:
                            notes = json.load(file)
                            notes.append(note)
                        save_notes(notes)
            elif choice == "2":
                read_notes()
            elif choice == "3":
                start_date = input("Введите дату начала (YYYY-MM-DD): ")
                end_date = input("Введите дату конца (YYYY-MM-DD): ")
                filtered_notes = filter_notes_by_date(start_date, end_date)
            elif choice == "4":
                if filtered_notes:
                    print_selected_note(filtered_notes)
                else:
                    print("Заметки по фильтру не доступны.")
            elif choice == "5":
                note_id = input("Введите ID для редактирования: ")
                edit_note(note_id)
            elif choice == "6":
                note_id = input("Введите ID для удаления: ")
                delete_note(note_id)
            elif choice == "7":
                search_date = input("Искать по дате (YYYY-MM-DD): ")
                filtered_notes = filter_notes_by_date(search_date)
            elif choice == "8":
                break
            else:
                print("Неправильный ввод. Попробуйте еще.")
        except Exception as e:
            print("Ошибка:", e)

if __name__ == "__main__":
    main()