#Define a function to count the frequency of words in a given list of words. 


def count_word_frequency(words):
    seen = []
    output = {}
    for i in range(len(words)):
        if words[i] not in seen:
            seen.append(words[i])
            count = 0
            for j in range(i,len(words)):
                if words[j] == words[i]:
                    count += 1
            output[words[i]] = count    
    return output
    
    
def count_word_frequency_Better(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count