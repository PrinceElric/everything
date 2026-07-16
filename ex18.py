import re


def is_valid_variable(variable_name):
    regex = r"\d"
    carac = re.findall(f" |{regex}|-", variable_name)
    if not carac:
        return True
    else:
        return False


print(is_valid_variable("first_name"))  # True
print(is_valid_variable("first-name"))  # False
print(is_valid_variable("1first_name"))  # False
print(is_valid_variable("firstname"))  # True

sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%\o@wering peo@ple. ;I found tea@ching m%\o@re interesting tha@n any other %jo@bs. %Do@es thi%\s mo@tivate yo@u to be a tea@cher!?"""


def clean_text(txt):
    # Escape \$ and add \\ to remove backslash
    txt = re.sub(r"%|@|#|&|!|;|\$|\\", "", txt)
    return txt


def most_frequent_words(texte):
    # Split text into words list
    words = texte.split()
    relevé = {}

    for i in words:
        if i not in relevé:
            relevé[i] = 1
        else:
            relevé[i] += 1

    # Sort by count big to small, take top 3
    sorted_words = sorted(relevé.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:3]


cleaned = clean_text(sentence)
print(cleaned)
print(most_frequent_words(cleaned))
# Output: [('I', 3), ('teacher', 2), ('and', 2)]
