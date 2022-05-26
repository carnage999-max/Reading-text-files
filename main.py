# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        text = f.read()
    return text


def count_words(text):
    # [assignment] Add your code here
    word_count = dict()
    words = text.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

 
text = read_file_content("story.txt")       
#filename = "story.txt"    
print(count_words(text))