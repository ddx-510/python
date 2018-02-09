# count the times of letters
def find_num_uppercase(str):
    if len(str)==0:
        return 0
    if 65 <= ord(str[0]) <= 90:
        return find_num_uppercase(str[1:]) + 1
    else:
        return find_num_uppercase(str[1:])

# main
string = input("Enter a sentence: ")
print('number of uppercase: ',find_num_uppercase(string))
