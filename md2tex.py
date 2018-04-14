import re
from subprocess import check_output
find_md = re.compile(r'\S*\.md')

file = input('请输入要转换的文件名：(.md)\n')

if file == '':
    file = str(check_output('dir', shell=True))
    file = find_md.search(file).group()
    file = file[:-3]

print('开始转换', file+'.md', '\n')

command = 'pandoc -s --template="F:/latex模板/for_pandoc/mytemp.latex" -o {0}.tex {0}.md'.format(
    file)
res = str(check_output(command, shell=True))

print(res)
if res == "b''":
    print('完成（*＾-＾*）')
else:
    print('额……\n')
    print(res)
