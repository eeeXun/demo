def readfile():
    d1=''
    d2=''
    d3=''
    d4=''
    with open('new.csv','r') as f:
        for row in f:
            EBITDA,csv=int(row.split('|')[0]),row.split('|')[1]
            if EBITDA<0:
                d1+='<tr><td>{}</td></tr>'.format(csv)
            elif EBITDA==0:
                d2+='<tr><td>{}</td></tr>'.format(csv)
            elif EBITDA>0 and EBITDA<10000000000:
                d3+='<tr><td>{}</td></tr>'.format(csv)
            else:
                d4+='<tr><td>{}</td></tr>'.format(csv)
    tohtml(d1,d2,d3,d4)

def tohtml(d1,d2,d3,d4):
    html='''
<table border="1">
    <tr><td>EBITDA</td><td>CSV</td></tr>
    <tr style="color:#d9534f">
        <td>EBITDA less than 0</td>
        <td>
            <table border="1" style="color:#d9534f">{}</table>
        </td>
    </tr>
    <tr style="color:#f0ad4e">
        <td>EBITDA equal to 0</td>
        <td>
            <table border="1" style="color:#f0ad4e">{}</table>
        </td>
    </tr>
    <tr style="color:#5cb85c">
        <td>EBITDA between 0 and 10billion</td>
        <td>
            <table border="1" style="color:#5cb85c">{}</table>
        </td>
    </tr>
    <tr style="color:#0275d8">
        <td>EBITDA not less than 10billion</td>
        <td>
            <table border="1" style="color:#0275d8">{}</table>
        </td>
    </tr>
</table>'''.format(d1,d2,d3,d4)
    with open('index.html','w') as f:
        f.write(html)

if __name__=='__main__':
    readfile()
