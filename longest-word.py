  GNU nano 5.9                    sublist-save.py                     Modified
"""
Longest Word
Have the function LongestWord(sen) take the sen parameter being passed and retu>
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
"""

def LongestWord(sen):
    liste = []
    for i in sen.split(" "):
        liste.append(i)
    a = max(liste)
    return a
    return sen
print(LongestWord(input()))
