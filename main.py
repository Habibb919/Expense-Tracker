import json
import os

FILE_NAME = "expenses.json"
expenses = []


def load_data():
    global expenses
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            expenses = json.load(f)
        print("Məlumatlar yükləndi.")
    except json.JSONDecodeError:
        print("Fayl oxunmadı (JSON səhvi var), boş siyahı ilə davam edirik.")
        expenses = []


def save_data():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(expenses, f, indent=4, ensure_ascii=False)
        print("Yadda saxlanıldı.")
    except Exception as err:
        print("Yadda saxlamaq olmadı:", err)


def add_expense():
    print("\n--- Yeni xərc ---")
    date = input("Tarix (məs: 2026-11-21): ").strip()
    category = input("Kateqoriya (məs: food, transport): ").strip()
    description = input("Qeyd / təsvir: ").strip()

    try:
        amount = float(input("Məbləğ: "))
    except ValueError:
        print("Məbləği düzgün yaz, rəqəm olmalıdır.")
        return

    expenses.append({
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    })
    print("Əlavə olundu.")


def print_table(items):
    print(f"{'Tarix':<12} | {'Kateqoriya':<14} | {'Təsvir':<18} | {'Məbləğ':>10}")
    print("-" * 62)
    for item in items:
        desc = item["description"][:18]
        print(f"{item['date']:<12} | {item['category']:<14} | {desc:<18} | {item['amount']:>9.2f}$")


def view_expenses():
    print("\n--- Bütün xərclər ---")
    if not expenses:
        print("Hələ heç bir xərc yoxdur.")
        return
    print_table(expenses)


def calculate_total():
    total = sum(item["amount"] for item in expenses)
    print(f"\nÜmumi xərc: {total:.2f}$")


def category_filter():
    if not expenses:
        print("\nSiyahı boşdur.")
        return

    cat = input("\nHansı kateqoriya? ").strip().lower()
    matches = [item for item in expenses if item["category"].lower() == cat]

    if not matches:
        print(f"'{cat}' üzrə heç nə tapılmadı.")
        return

    print(f"\n--- '{cat}' xərcləri ---")
    print_table(matches)


def delete_expense():
    if not expenses:
        print("\nSilməyə xərc yoxdur.")
        return

    print("\n--- Xərc silinməsi ---")
    for i, item in enumerate(expenses, start=1):
        print(f"{i}. {item['date']} | {item['category']} | {item['description']} | {item['amount']:.2f}$")

    try:
        num = int(input("Silmək istədiyin nömrə: "))
    except ValueError:
        print("Nömrə rəqəm olmalıdır.")
        return

    if num < 1 or num > len(expenses):
        print("Belə nömrə yoxdur.")
        return

    removed = expenses.pop(num - 1)
    print(f"Silindi: {removed['description']} ({removed['amount']:.2f}$)")


def main():
    load_data()

    while True:
        print("\n=== XƏRCLƏR ===")
        print("1. Xərc əlavə et")
        print("2. Xərclərə bax")
        print("3. Cəmi hesabla")
        print("4. Kateqoriyaya görə filter")
        print("5. Xərc sil")
        print("6. Yadda saxla")
        print("7. Fayldan yenidən oxu")
        print("8. Çıxış")

        secim = input("Seçim (1-8): ").strip()

        if secim == "1":
            add_expense()
        elif secim == "2":
            view_expenses()
        elif secim == "3":
            calculate_total()
        elif secim == "4":
            category_filter()
        elif secim == "5":
            delete_expense()
        elif secim == "6":
            save_data()
        elif secim == "7":
            load_data()
        elif secim == "8":
            save_data()
            print("Sağ ol.")
            break
        else:
            print("1-dən 8-ə qədər rəqəm seç.")


if __name__ == "__main__":
    main()