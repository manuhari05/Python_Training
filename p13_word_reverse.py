class Word:
    def __init__(self, word):
        # Initialize the class with a word
        self.word = word

    def reverse(self):
        # Split the word into a list of words
        word = self.word
        # Split the string into words
        l = word.split()  
         # Reverse the order of the words
        l.reverse()  

        # Join the reversed list back into a string
        return ' '.join(l)  

# Create an instance of the Word class with the string 'hello world'
word = Word('hello world')
# Call the reverse method to reverse the order of words
reversed_word = word.reverse()
# Print the reversed word string
print(reversed_word)
            