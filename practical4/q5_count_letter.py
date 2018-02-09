# count the times of letters
def count_letter(str, ch):
    if len(str)==0:
        return 0
    if str[0]==ch:
        return count_letter(str[1:],ch) + 1
    else:
        return count_letter(str[1:],ch)

# main
string = input("Enter a string: ")
letter = input("Enter a letter: ")
print(count_letter(string,letter))

