"""_summary_

[결과]
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

"""


for i in range(1,4):
    str=""
    for j in range(1,6):
        str+="{}\t" .format(j)
        if(j==3):
            break;
    print(str)
print("=============================")
    
    