def backward_segment(text, dic):
    """
    :param text:待分词的文本
    :param dic:词典
    :return:元素为分词结果的list列表
    """
    word_list = []
    # 扫描位置作为终点
    i = len(text) - 1
    while i >= 0:
        longest_word = text[i]                      
        for j in range(0, i):                       
            word = text[j: i + 1]                   
            if word in dic:
                # 越长优先级越高
                if len(word) > len(longest_word):   
                    longest_word = word
                    break
        # 逆向扫描，所以越先查出的单词在位置上越靠后
        word_list.insert(0, longest_word)           
        i -= len(longest_word)
    return word_list

if __name__ == '__main__':
    # 加载词典
    dic = ['研究','研究生','生命','起源','命']
    text = '研究生命起源'
    print(backward_segment(text, dic))
