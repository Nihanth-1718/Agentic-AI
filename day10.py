students = {
    "ids": [23, 21, 45, 52],
    "names": ["Praneeth", "Abhiram", "Vasanthi", "Akshitha"],
    "places": ("Hyd", "Vijayawada"),
    "gender": {"Male", "Female"}
}

print(students)
print(len(students))
print(students.keys())
print(students.values())
print(students.items())
print(students["names"])
print(students.get("branch"))
print(students.get("branch", "CSE"))

students["course"] = ["PFS", "JFS", "AAA", "DA"]
students["ids"].extend([56, 67, 87])
students["names"].insert(1, "Ashok")

students["places"] = list(students["places"])
students["places"].append("Vizag")

students["names"].sort()

print(students["course"][1::2])      # ['JFS', 'DA']
print(students["ids"][::3])          # [23, 52, 87]
print(students["names"])

students.setdefault("branch", ["CSE", "CSD", "ECE", "IT"])

students.update({"fees": [456, 234], "marks": [45, 78, 85]})
print(students)

print(students.pop("marks"))
print(students.popitem())

d = dict.fromkeys([23, 45, 67], None)
d[23] = "Random"
print(d)
print(23 in d)

college = {
    "Student1": {
        "id": 23,
        "name": "Ram",
        "place": "Hyd"
    },
    "Student2": {
        "id": 25,
        "name": "Sony",
        "place": "Bengaluru"
    }
}

print(college)
print(college.keys())
print(college["Student1"]["name"])
