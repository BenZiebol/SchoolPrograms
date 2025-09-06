#Ben Ziebol

def qtoz(str_list):
    new_list=[]
    for i in str_list:
        word=i
        new_word=''
        for j in i:
            
            if j=='q':
                new_word+='z'
            elif j=='Q':
                new_word+='Z'
            else:
                new_word+=j
        new_list.append(new_word)

    return new_list

def sum_lists(nested_list):
    new_list=[]
    for i in nested_list:
        #goes over the list 2 in list 1
        new_list.append(sum(i))
    return new_list
            
def secret_message(sentence):
    sentence=sentence.split()
    new_sentence=''
    for i in sentence:
        new_sentence+=i[0]
    return new_sentence

def get_rows_cols(fname):
    rows=0
    columns=0
    try:
        file_name=open(fname)
    except FileNotFoundError:
        return [0,0]
    for i in file_name:
        rows+=1
        if i.count(',')>columns:
            columns=i.count(',')
    file_name.close
    return [rows,columns]

def repeat(fname):
    file_name=open(fname)
    file_write=open('repeat_'+fname,'w')
    for i in file_name:
        for j in i:
            if j.isalpha():
                file_write.write(j+j)
            else:
                file_write.write(j)
