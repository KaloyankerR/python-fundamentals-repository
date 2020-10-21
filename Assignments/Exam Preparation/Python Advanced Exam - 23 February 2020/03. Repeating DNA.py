def get_repeating_DNA(DNA):
    repeated_DNAs = []
    for letter in range(len(DNA)):

        current_DNA = DNA[letter:letter + 10]
        if len(current_DNA) == 10:
            if (DNA.count(current_DNA) >= 2 and current_DNA not in repeated_DNAs) or current_DNA == DNA[
                                                                                                    letter + 1:letter + 11]:
                repeated_DNAs.append(current_DNA)
        else:
            return repeated_DNAs


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)
print()
test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)
print()
test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
