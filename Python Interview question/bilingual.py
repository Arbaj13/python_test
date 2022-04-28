def translate(b_dict,english_word_list):
    swedish_word_list=[]
    for i in english_word_list:
        swedish_word_list.append(b_dict[i])

    return swedish_word_list

b_dict={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}

english_word_list=["and","new"]

swedish_word_list=translate(b_dict,english_word_list)   

print("the list is ",swedish_word_list)
