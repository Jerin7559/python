list1=[15,25,14,13,85,45,63]
list2=[78,41,22,132,12,65,78]
def common_value(x,y):
    common=0
    for value in x:
           if value in y:
                    common=1
    if(not common):
           return("the lists have no common elements")
    else:
            return("the lists have common elements")
def list_length(x,y):
    if(x.size_of()==y.size_of()):
             return("both list are of same length")
    else:
             return("both are different in length")
def list_sum(x,y):
    if(sum(x)==sum(y)):
                 return("both list sum to same value")
    else:
                 return("both list sum to different value")
          print(common_value(list1,list2))
          print(list_length(list1,list2))
          print(list_sum(list1,list2))