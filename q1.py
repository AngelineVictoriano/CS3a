#/*****************************************************/
#/* CS03A - Summer 2026
#/* Assignment 2 - Question 1
#/* Student Name: Angeline Victoriano
#/* SID: 20528831
## /***************************************************/

def run():

    def falling_distance(falling_time):
        d = 0.5*9.8*falling_time**2
        return d

    for i in range(1,11):
        print(f"distance the object has fallen in {i} seconds: {falling_distance(i):.2f} meters")



if __name__ == "__main__":
    # This allows students to run this specific file
    # individually for testing (e.g., `python q1.py`)
    run()