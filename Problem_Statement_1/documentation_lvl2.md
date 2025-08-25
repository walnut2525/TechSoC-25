# My Experience
This assignment forced me to learn a lot of things and made me think about cryptography in a new way. I had to think creatively to come up with a method to solve the cipher
# Method
I rewrote the code from the first bit to allow it to shift anywhere. I created a list of each shifted word. Now the problem was to compare frequency of each shifted word. By looking up online i was able to find 
the letter frequencies for each letter. I added up the letter frequencies for each letter in the shifted word, and i had a new list which showed the number corresponding to the sum
of each frequency of each letter in it. Using max function I am able to the most frequent word. This word doesnt necessarily need to be in the english language, so I
imported a library which contains all english words. I compared the word from the list and the library, if it didnt match it will move on to the second most frequent word and so on
thus the final result is a decoded word which is from the english dictionary.
