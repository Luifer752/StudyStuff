
b = '''сибас путин корова корова летала корова гелентваген 
или поедем корова корова летала и также летала гелентваген или нет'''

def numOfwords(string):
    let_dict = {}
    stop_words = ('нет', 'и', 'или', 'путин')
    inter_list = [i for i in string.split() if i not in stop_words]

    for i in inter_list:
        if i not in let_dict:
            let_dict[i] = + 1
        else:
           let_dict[i] = let_dict[i] + 1

    sorted_let_dict = dict(sorted(let_dict.items(), key=lambda x: x[1], reverse=True))
    return sorted_let_dict

print(numOfwords(b))