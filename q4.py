#/*****************************************************/
#/* CS03A - Summer 2026
#/* Assignment 1 - Question 4
#/* Student Name: Angeline Victoriano
#/* SID: 20528831
## /***************************************************/

def run():

    fname = input("Enter your name: ")
    description = input("Describe yourself: ")

    with open("myself.html", "w") as file:
        file.write(f"""<html>
<head>
</head>
<body>
      <center>
            <h1>{fname}</h1>
      </center>
      <hr />
      {description}
</body>
</html>""")

if __name__ == "__main__":
    # This allows students to run this specific file
    # individually for testing (e.g., `python q1.py`)
    run()