# -描述
可以根据web of science中下载的savedrecs.ciw文件（注意不要修改名字）或者知网下载的.txt文件（这个名称无所谓，自己选文件）自动生成一个论文笔记tex模板，一切都从0开始，我会在自己看论文记笔记的过程中逐渐为它添加功能

# -使用方法
1.将format.py,format_CNKI.py,n.template.tex,readarticle.cls文件放在同一目录。

2.从web of science或者知网导出自己想要生成笔记的savedrecs.ciw文件或*.txt文件到该工作目录。

3.双击运行format.py文件，输入阅读编号，比如第一篇文献就输入1.

4.当前目录下会自动新建名为 "编号.论文名称"的目录
该目录结构为：
编号.论文名称
|--images(文件夹)

|--编号.tex

|--readarticle.cls

5.双击打开tex文件就可以开始边看论文边记笔记了
进去之后可以把一些信息先填上，比如论文译名，期刊分区，审稿周期等。
