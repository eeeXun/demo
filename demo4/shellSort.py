def shellsort(EBITDA_csv):
    size_csv=len(EBITDA_csv)
    gap=1
    while gap<size_csv:
        gap=gap*3+1
    while gap>1:
        gap//=3
        key=int
        key_list=[]
        j=int
        for i in range(gap,size_csv):
            key=EBITDA_csv[i][0]
            key_list=EBITDA_csv[i]
            j=i-gap
            while j>=0 and key<EBITDA_csv[j][0]:
                EBITDA_csv[j+gap]=EBITDA_csv[j]
                j-=gap
            EBITDA_csv[j+gap]=key_list

def readfile(EBITDA_csv):
    with open('/home/xun/Downloads/500_constituents_financial.csv','r') as f:
        first_row=True
        for row in f:
            if first_row:
                first_row=False
                continue
            else:
                tmp=row.split(',')
                if '"' in row:
                    EBITDA=tmp[10]
                else:
                    EBITDA=tmp[9]
                if 'E' in EBITDA:
                    EBITDA_csv.append([int(eval(EBITDA)),row])
                else:
                    EBITDA_csv.append([int(EBITDA),row])

def writefile(EBITDA_csv):
    with open('new.csv','w') as f:
        for i in EBITDA_csv:
            f.write(str(i[0])+'|'+i[1])

def main():
    EBITDA_csv=[]
    readfile(EBITDA_csv)
    shellsort(EBITDA_csv)
    writefile(EBITDA_csv)

if __name__=='__main__':
    main()
