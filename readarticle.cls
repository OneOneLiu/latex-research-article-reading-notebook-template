% Author: Liu Daohui
% Homepage: none
% Email: 1183418633@qq.com
% Lastest Version: this version
\ProvidesClass{readarticle}
\NeedsTeXFormat{LaTeX2e}
\LoadClass[UTF8]{ctexart}

%一些要用的包，
\RequirePackage{hyperref}    %插入超链接
\RequirePackage{graphicx}    %插入图片
\RequirePackage{color}    %使用彩色字体
\RequirePackage{enumerate}%enu编号用的库
\RequirePackage{booktabs}%表格横线


\RequirePackage{tikz}    %自主绘制图形
\usetikzlibrary{shapes.geometric, arrows}
\tikzstyle{startstop} = [rectangle, rounded corners, minimum width=3cm, minimum height=1cm,text centered, draw=black, fill=red!30]%开始结尾框设置
\tikzstyle{io} = [trapezium, trapezium left angle=70, trapezium right angle=110, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=blue!30]%输入输出设置
\tikzstyle{process} = [rectangle, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=orange!30]%处理框设置
\tikzstyle{decision} = [diamond, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=green!30]%判断决定框设置
\tikzstyle{arrow} = [thick,->,>=stealth]%箭头框设置
\tikzstyle{line} = [draw, -latex']%直线设置
\tikzstyle{cloud} = [draw, ellipse,fill=red!20, node distance=3cm,minimum height=2em]%好像是椭圆


\RequirePackage{xcolor}      %插入自定义颜色
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\RequirePackage{listings}    %插入代码段
\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=4
}
\lstset{style=mystyle}

%一些重新定义的风格命令
\renewcommand{\thefootnote}{\textcolor{red}{[\arabic{footnote}]}}%这一句的作用就是把角标的数字从 1 --> [1]，加上对应的命令后也可以改颜色