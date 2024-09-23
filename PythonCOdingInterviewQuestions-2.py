# Python Coding Interview Questions - Hardier

# String segmentation
# You are provided with a large string and a list of the words.
# You have to find if the input string can be segmented into words using the dictionary or not.
list = ["data", "camp", "cam", "lack"]


def can_be_segmented(word, list):
    for i in range(1, len(word) + 1):
        firstWord = word[0:i]
        if firstWord in list:
            # If first word is found then we check second part
            second_half = word[i:]
            # check that second half has multiple words
            if (
                not second_half
                or second_half in list
                or can_be_segmented(second_half, list)
            ):
                return True
    return False


can_be_segmented("datacamp", list)
# True
can_be_segmented("camp", list)
# True
can_be_segmented("helloworld", list)
# False

# Remove duplicates from sorted array


def remove_duplicates(list):
    insertIndex = 1
    for i in range(len(list) - 1):
        if list[i] != list[i + 1]:
            list[insertIndex] = list[i + 1]
            insertIndex += 1
    return insertIndex


remove_duplicates([1, 2, 2, 3, 3, 4])
# 4

remove_duplicates([1, 1, 3, 4, 5, 6, 6])
# 5
