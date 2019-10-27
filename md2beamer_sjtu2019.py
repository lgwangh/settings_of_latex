import re
from subprocess import check_output
find_md = re.compile(r'\S*\.md')

file = input('请输入要转换的文件名：(.md)\n')

if file == '':
    file = check_output('dir', shell=True).decode('gb18030')
    file = find_md.search(file).group()
    file = file[:-3]

print('开始转换', file+'.md', '\n')

res = check_output(r'copy "C:\Files\latex_template\bibtex\gbt7714-bibtex-style\gbt7714.sty"', shell=True).decode('gb18030')
res = check_output(r'copy "C:\Files\latex_template\bibtex\gbt7714-bibtex-style\gbt7714-plain.bst"', shell=True).decode('gb18030')
res = check_output(r'copy "C:\Files\latex_template\bibtex\gbt7714-bibtex-style\gbt7714-unsrt.bst"', shell=True).decode('gb18030')
res = check_output(r'copy "C:\Files\latex_template\beamer\beamerthemesjtu2019.sty"', shell=True).decode('gb18030')
res = check_output(r'copy "C:\Files\latex_template\beamer\abb"', shell=True).decode('gb18030')

command = 'pandoc --slide-level 2 -s --template="C:/Files/latex_template/for_pandoc/pandoc_md2sjtu2019.latex" -t beamer -o {0}.tex {0}.md'.format(file)
res = check_output(command, shell=True).decode('gb18030')

print(res)
if res == '':
    print('完成（*＾-＾*）')
else:
    print('额……\n')
    print(res)

input()