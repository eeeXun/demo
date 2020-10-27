import os
def main():
    status={}
    sorted_count={}
    log=[]
    sorted_log=[]

    with open('/home/xun/Downloads/access_test.log','r') as f:
        for i in f:
            tmp=i.split(' ')
            log.append([])
            if tmp[8]=='"-"':
                log[len(log)-1].append(tmp[6])
                print('yes',tmp[6])
            else:
                log[len(log)-1].append(tmp[8])
            log[len(log)-1].append(i.replace('\n',''))
            if tmp[8] in status:
                status[tmp[8]]+=1
            else:
                status[tmp[8]]=1

    def bub_status(tmp):
        for i in range(len(tmp)-1,-1,-1):
            for j in range(i):
                if tmp[j]>tmp[j+1]:
                    tmp[j],tmp[j+1]=tmp[j+1],tmp[j]

    def sortingStatus():
        tmp=[]
        sorted_status=[]
        sorted_status_count=[]
        for i in status:
            tmp.append(i)
        bub_status(tmp)
        for i in tmp:
            sorted_status.append(i)
            sorted_status_count.append(status[i])
        for i in range(1,len(sorted_status_count)):
            sorted_status_count[i]+=sorted_status_count[i-1]
        for i in range(len(sorted_status)):
            sorted_count[sorted_status[i]]=sorted_status_count[i]

    def counting_sort():
        for i in range(len(log)):
            sorted_log.append([])
        for i in range(len(log)-1,-1,-1):
            tmp_status=log[i][0]
            tmp_log=log[i][1]
            sorted_log[sorted_count[tmp_status]-1].append(tmp_status)
            sorted_log[sorted_count[tmp_status]-1].append(tmp_log)
            sorted_count[tmp_status]-=1


    def writeLog():
        if os.path.exists('status.log'):
            os.remove('status.log')
        with open('status.log','w') as f:
            first_time=True
            for i in sorted_log:
                if first_time:
                    f.write('{},{}'.format(i[0],i[1]))
                    first_time=False
                else:
                    f.write('\n{},{}'.format(i[0],i[1]))

    sortingStatus()
    counting_sort()
    writeLog()
    return sorted_count

if __name__=='__main__':
    main()
