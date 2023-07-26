import csv
import os
from mybookreview import app


def main():
    f = open("books.csv")
    reader = csv.reader(f)
    header = next(reader)

    print("Running script ... ")
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books(isbn, title, author, year) VALUES(:i, :t, :a, :y)", {"i": isbn, "t": title, "a": author, "y": year})

    db.commit()
    
    print("Completed ... ")


if __name__ == "__main__":

    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )