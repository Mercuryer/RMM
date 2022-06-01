#逆向最大分词算法
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
    dic = ['北京','北京交通大学','位于','北京市','是','中华','中华人民','中华人民共和国','教育部','中华人民共和国教育部','直属','的','全国','重点','大学','全国重点大学','国家','双一流建设高校','211工程建设高校','先后','入选','985工程优势学科创新平台','高等学校创新能力提升计划','111计划','卓越工程师教育培养计划','高校','工程','建设','优势','学科','创新','平台','高等','学校','能力','提升','计划','卓越','工程师','教育','培养','创新能力','创新平台','优势学科']
    text = '北京交通大学位于北京市是中华人民共和国教育部直属的全国重点大学是国家双一流建设高校211工程建设高校先后入选985工程优势学科创新平台高等学校创新能力提升计划111计划卓越工程师教育培养计划'
    true_result = ['北京交通大学','位于','北京市','是','中华人民共和国教育部','直属','的','全国重点大学','国家','双一流建设高校','211工程建设高校','先后','入选','985工程优势学科创新平台','高等学校创新能力提升计划','111计划','卓越工程师教育培养计划']
    seg_result = backward_segment(text, dic)
    print('seg_result:',seg_result)

    true_len = len(true_result) #正确分词结果的个数
    seg_len = len(seg_result) #模型分词结果个数

    #计算召回率
    a=0
    for word in true_result:
        if word in seg_result:
            a+=1
    recall = a/true_len
    print('recall:',recall)

    #计算正确率
    b=0
    for word in seg_result:
        if word in true_result:
            b+=1
    precision = b/seg_len
    print('precision:',precision)

    #计算F值
    F = (recall+precision)/(2*recall*precision)
    print('F:',F)
