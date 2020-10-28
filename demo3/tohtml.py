import counting
import os
def main():
    d1=''
    d2=''
    d3=''
    d4=''
    d5=''
    # log=counting.main()
    with open('status.log','r') as f:
        for i in f:
            status_log=i.split(',')
            status=int(status_log[0])
            log=status_log[1]
            if status>=100 and status<200:
                d1+='<tr><td>{}</td></tr>'.format(log)
            elif status>=200 and status<300:
                d2+='<tr><td>{}</td></tr>'.format(log)
            elif status>=300 and status<400:
                d3+='<tr><td>{}</td></tr>'.format(log)
            elif status>=400 and status<500:
                d4+='<tr><td>{}</td></tr>'.format(log)
            else:
                d5+='<tr><td>{}</td></tr>'.format(log)

    html='''
<table border="1">
    <tr><td>Status</td><td>Log File</td></tr>
    <tr style="color:#5bc0de">
        <td>
            Informational Responses
        </td>
        <td>
            <table border="1" style="color:#5bc0de">{}</table>
        </td>
    </tr>
    <tr style="color:#5cb85c">
        <td>
            Successful Responses
        </td>
        <td>
            <table border="1" style="color:#5cb85c">{}</table>
        </td>
    </tr>
    <tr style="color:#0275d8">
        <td>
            Redirects
        </td>
        <td>
            <table border="1" style="color:#0275d8">{}</table>
        </td>
    </tr>
    <tr style="color:#f0ad4e">
        <td>
            Client Errors
        </td>
        <td>
            <table border="1" style="color:#f0ad4e">{}</table>
        </td>
    </tr>
    <tr style="color:#d9534f">
        <td>
            Server Errors
        </td>
        <td>
            <table border="1" style="color:#d9534f">{}</table>
        </td>
    </tr>
</table>'''.format(d1,d2,d3,d4,d5)

    with open('index.html','w') as f:
        f.write(html)

if __name__=='__main__':
    main()
