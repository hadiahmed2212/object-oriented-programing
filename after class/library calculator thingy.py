books = ["the explorer", "picture books", "kensukes kingdom", "running wild", "dog man"]
copy_counts = [9, 6, 0, 1, 3]

library = {book: count for book, count in zip(books, copy_counts)}
print("Library Stock:", library)
available_books = [book for book in books if library[book] > 0]
print("Available books", available_books)

csn_bk = input("book u want?")

if csn_bk not in library or library[csn_bk] == 0:
    print(csn_bk, "NOT AVAIL...")
    exit()

late_fees = [3, 5, 4, 1, 9]
extra_fee = int(input("extra library fee: "))


updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
print("Updated Late Fees:", updated_fees)

book_index = books.index(csn_bk)
csn_fee = updated_fees[book_index]
print("Late fee for", csn_bk, "after update:", csn_fee)

library[csn_bk] = library[csn_bk] - 1
print(csn_bk, "book borrowed sucsessfully!", library[csn_bk])