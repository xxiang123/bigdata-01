internet=open('Internet.html','a+')
internet.writelines('<!DOCTYPE html>'+'\n'+'<html lang="en">'+'\n'+'<head>'+'\n'+'<meta charset="UTF-8">'+'\n'+'<title>movie score</title>'+'\n')
internet.writelines('<style type="text/css">'+'\n')
internet.writelines('div{background-image:url(./img/background.jpg); background-size:100% 100%; background-repeat:no-repeat;}'+'\n')
internet.writelines('a:link{color:#00f;text-decoration:none}'+'\n')
internet.writelines('a:visited{color:#999;}'+'\n')
internet.writelines('a:hover{color:#fff;font-size:30px;}'+'\n')
internet.writelines('a:active{color:#F00;}'+'\n')
internet.writelines('</style>'+'\n')
internet.writelines('</head>'+'\n')
internet.writelines('<body>'+'\n'+'<h1>MOVIE SCORE</h1>'+'\n')
internet.writelines('<div>'+'\n'+'<ul>'+'\n')
with open('text.txt','r',encoding='utf-8') as fp:
    while True:
        s=fp.readline()
        if s=='':
            break
        s=s.replace('\n','')
        list=s.split()
        string='<li>'+'<a href='+list[3]+'>'+list[0]+' '+'Grade:'+list[1]+' '+'Type:'+list[2]+'</a>'+'</li>'
        internet.writelines(string+'\n')
        print(string)
internet.writelines('</ul>'+'\n'+'</div>'+'\n'+'</body>'+'\n'+'</html>')
internet.flush()

internet.close()
fp.close()