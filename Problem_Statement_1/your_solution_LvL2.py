import enchant
code = input("Input the word you want to decode: ")
letters = list(code)
length = len(code) - 1
i = 0
value = [ord(char) for char in letters]
shift = 0
words=[]
shift=0
while shift<= 25:
    while i <= length:
        if 0 <= value[i] < 65 or 91 <= value[i] <= 96 or 123 <= value[i] <= 127:
            value[i] = value[i]
        elif 65 <= value[i] <= 90:  
            value[i] = (value[i] - 65 - shift) % 26 + 65
        elif 97 <= value[i] <= 122:  
            value[i] = (value[i] - 97 - shift) % 26 + 97
        i = i + 1
        new_letter=[chr(num) for num in value]
        new_word=''.join(new_letter)
    words.append(new_word)
    shift=shift+1
    i=0
    value = [ord(char) for char in letters]
letter_weights = {
    "E": 12.49,
    "T": 9.28,
    "A": 8.04,
    "O": 7.64,
    "I": 7.57,
    "N": 7.23,
    "S": 6.51,
    "R": 6.28,
    "H": 5.05,
    "L": 4.07,
    "D": 3.82,
    "C": 3.34,
    "U": 2.73,
    "M": 2.51,
    "F": 2.40,
    "P": 2.14,
    "G": 1.87,
    "W": 1.68,
    "Y": 1.66,
    "B": 1.48,
    "V": 1.05,
    "K": 0.54,
    "X": 0.23,
    "J": 0.16,
    "Q": 0.12,
    "Z": 0.09
}
weighted_list=[]
for new_words2 in words:
    letters2= list(new_words2)
    j=0
    length= len(new_words2)-1
    word_weight=0
    while j<= length:
        word_weight=word_weight + letter_weights[letters2[j].upper()]
        j=j+1
    weighted_list.append(word_weight)
ordered_list=weighted_list[:]
ordered_list.sort(reverse=True)
d = enchant.Dict("en_GB")
k = 0
while k < len(words) and not d.check(words[weighted_list.index(ordered_list[k])]):
    k= k+1
print("Likely decoded word:", words[weighted_list.index(ordered_list[k])])
