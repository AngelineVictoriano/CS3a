# /*****************************************************/
# /* CS03A - Summer 2026
# /* Assignment 1 - Question 3
# /* Student Name: Angeline Victoriano
# /* SID: 20528831
## /***************************************************/

def run():
    def sentence_capitalizer(phrase):

        new_sentence = phrase.title()
        return new_sentence

    phrase = input("Enter sentence/s: ")
    print(phrase)
    print(sentence_capitalizer(phrase))
if __name__ == "__main__":
    # This allows students to run this specific file
    # individually for testing (e.g., `python q1.py`)
    run()