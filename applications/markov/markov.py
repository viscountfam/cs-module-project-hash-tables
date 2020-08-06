import random

#run, right, fast

#UPER

## Understand

## 1. Read the file 'input.txt and split it into words
    #### already read in 
    ### split into words
# 2. Analyze the text, building up the dataset of words
    ### Which words can follow a word? any word that actually does follow the word
    ### these words will be any word at index + 1
    ### How to build dataset?
    
    ### Use a hashtable
    ### good way to relate one piece of data like a word with the w2ords that can be linked to it
    ### way to relate one piece of info, with other info. relational
    #### Frequent lookups kept at O(1)
    ### Key: word, value: list of all the words that can follow this word

# 3. Choose a random "start word" to begin.
    ## What is a start word
        ### words that start with a capital letter or a quotation mark followed by a capital letter should be start words
    ## Make a list of start words

# 4. Loop through, choose a random following word
    # if it's a stop word end the loop
        ## A stop word is a word that ends with a period, exclamation point, question mark or elipsis or has a second to last charactere which is one of these

# Read in all the words in one go
with open("applications\markov\input.txt") as f:
    words = f.read()
def markov(s):
    #split into words
    split_words = s.split()
# TODO: analyze which words can follow other words
    dataset = {}
    # loop to collect all the words in the dictionary
    for i in range(len(split_words) - 1):
        word = split_words[i]
        next_word = split_words[i + 1]

        if word not in dataset:
            dataset[word] = [next_word]
        
        else:
            dataset[word].append(next_word)


    # Make a list of start words
    start_words = [key for key in dataset.keys() if key[0].isupper() or len(key) > 1 and key[1].isupper() ]
    # end_words = [key for key in dataset.key() if key[-1]]
# TODO: construct 5 random sentences
    stop_signs = "?.!"
    for i in range(5):
        stopped = False
        word = random.choice(start_words)
        while not stopped:
            print(word, end=" ")
            if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
                stopped = True
            
            following_word = dataset[word]

            word = random.choice(following_word)

print(markov(words))
