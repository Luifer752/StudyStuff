a = 'коко'
b = 'сибас корова летала'
c = 'парпапапа'
def numOfletters(*words):
    vowels = ['а','я','у','ю','о','е','ё','э','и','ы']
    let_dict = {}
    for i in words:
        for letter in i:
            if letter not in let_dict:
                let_dict[letter] = + 1
            else:
                let_dict[letter] = let_dict[letter] + 1

    return let_dict

print(numOfletters(a, b, c))