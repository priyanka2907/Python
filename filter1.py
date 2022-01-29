def Filter1(fun_name,list1):
    newdata=[]
    for i in range(len(list1)):
        if(fun_name(list1[i]) == True):
            newdata.append(list1[i]);
    return newdata;