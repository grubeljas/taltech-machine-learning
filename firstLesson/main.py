"""Set exercises."""


def create_set_from_numbers(a: int, b: int, c: int) -> set:
    """
    Create set from three integers.

    create_set_from_numbers(1, 2, 3) => {1, 2, 3}
    create_set_from_numbers(1, 2, 1) => {1, 2}
    create_set_from_numbers(1, 1, 1) => {1}
    """
    s = set()
    s.add(a)
    s.add(b)
    s.add(c)
    return s


def add_one(set_a: set) -> set:
    """
    Take a set of integers and increment each integer by one, return new set.

    add_one({1, 2, 3}) => {2, 3, 4}
    add_one({-10, 0, 10}) => {-9, 1, 11}

    :param set_a: given set
    :return: new set where all elements have been incremented by one.
    """
    s = set()
    for i in set_a:
        s.add(i + 1)
    return s


def remove_six(set_a: set) -> set:
    """
    Take a set of digits and remove the number six from it if its there, return set.

    remove_six({1, 2, 3, 4, 5, 6, 7, 8, 9}) => {1, 2, 3, 4, 5, 7, 8, 9}
    remove_six({1, 5, 7}) => {1, 5, 7}

    :param set_a: given set
    :return: set without sixes.
    """
    set_a.discard(6)
    return set_a


def convert_to_set(list_a: list) -> set:
    """
    Take a list, convert it to a set and return it.

    convert_to_set([1, 2, 3, 1]) => {1, 2, 3}
    convert_to_set([1, 2, 3, 4]) => {1, 2, 3, 4}

    :param list_a: given list
    :return: set made from given list.
    """
    return set(list_a)


def count_unique_elements(input_list: list) -> int:
    """
    Count unique elements in the list.

    Hint: set only has unique elements.

    Hint: no loop required

    count_unique_elements([1, 2, 3]) => 3
    count_unique_elements([1, 1, 1]) => 1
    count_unique_elements([]) => 0
    """
    return len(set(input_list))


def common_characters_in_words(word1: str, word2: str) -> set:
    """
    Find common characters in two words.

    No loops required.

    common_characters_in_words("hello", "hi") => {"h"}
    common_characters_in_words("world", "low") => {"l", "o", "w"}
    """
    set1 = set(word1)
    set2 = set(word2)
    return set1.intersection(set2)


def exam_conditions_not_met(names1: list, names2: list) -> set:
    """
    Who has NOT met the conditions for the exam.

    To get to the exam, two tests have to be passed.
    There is one list with the names who passed the first test.
    And another list with the names who passed the second test.
    All the names are unique in this exercise.
    All the names are case-sensitive ("Kati" != "kati").

    So, the names who are in both lists, get to do the exam.
    This function has to return the names who DID NOT get to the exam.

    No loops required.

    exam_conditions_not_met(["Mati"], ["Mati", "Kati"]) => {"Kati"}
    exam_conditions_not_met(["Mati", "Kati"], ["Mati", "Kati"]) => {}
    exam_conditions_not_met(["Mati", "Kaja"], ["Mati", "Kati"]) => {"Kaja", "Kati"}
    """
    set1 = set(names1)
    set2 = set(names2)
    return set1.symmetric_difference(set2)


def uninvited_friends_count(friends: list, invited: list) -> int:
    """
    How many friends were not invited.

    There is a list of friends and a list of invited people.
    How many of the friends were not invited?

    No loops required.

    uninvited_friends_count(["mati", "kati"], []) => 2
    uninvited_friends_count(["mati", "kati"], ["kati"]) => 1
    uninvited_friends_count(["mati", "kati"], ["kati", "rein"]) => 1
    """
    set1 = set(friends)
    set2 = set(invited)
    return len(set1.difference(set2))


def contains_duplicates(input_list: list) -> bool:
    """
    Return whether the list contains duplicate elements.

    No loops required.

    contains_duplicates([1, 2, 3]) => False
    contains_duplicates([1, 2, 1]) => True
    contains_duplicates([1, 1]) => True
    contains_duplicates([1]) => False
    contains_duplicates([]) => False
    """
    return True if len(input_list) != len(set(input_list)) else False


def find_numbers_divisible_by_3(numbers: list) -> set:
    """
    Return a set of numbers from the input list which are divisible by 3.

    Numbers are between 0 and 1000 (inclusive).

    Hint: this function can be done without a loop.
    As we know the limit of numbers, we can create
    a set of all the numbers in the range which are
    divisible by 3.
    Hint: use range().

    find_numbers_divisible_by_3([1, 2, 3]) => {3}
    find_numbers_divisible_by_3([3, 2, 3, 12]) => {3, 12}
    """
    return set(range(0, 1000, 3)).intersection(numbers)
