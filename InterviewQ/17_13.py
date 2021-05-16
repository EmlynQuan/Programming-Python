
!!!!
def respace(dictionary, sentence):
    length = len(sentence)
    i = 0
    ret = []
    while i < length:
        j = i
        while j < length:
            print sentence[i:j + 1]
            if sentence[i:j+1] in dictionary:
                ret.append(sentence[i:j+1])
                i = j
                break
            j += 1
        i += 1

    counter = 0
    for i in range(len(ret)):
        counter += len(ret[i])

    return length - counter


if __name__ == "__main__":
    dictionary = ["vprkj","sqvuzjz","ptkrqrkussszzprkqrjrtzzvrkrrrskkrrursqdqpp","spqzqtrqs","rkktkruzsjkrzqq","rk","k","zkvdzqrzpkrukdqrqjzkrqrzzkkrr","pzpstvqzrzprqkkkd","jvutvjtktqvvdkzujkq","r","pspkr","tdkkktdsrkzpzpuzvszzzzdjj","zk","pqkjkzpvdpktzskdkvzjkkj","sr","zqjkzksvkvvrsjrjkkjkztrpuzrqrqvvpkutqkrrqpzu"]
    sentence = "rkktkruzsjkrzqqzkvdzqrzpkrukdqrqjzkrqrzzkkrr"

    print respace(dictionary, sentence)