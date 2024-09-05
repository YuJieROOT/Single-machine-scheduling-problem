[toc]

# Flask开发Web应用

## 项目主结构
```python
/project				# 项目的名称
│
├── /data               # 存放数据库初始化文件
│
├── /static             # 静态文件夹，存放 CSS、JavaScript、图片等文件
│   ├── /css            # 存放样式表文件
│   ├── /js             # 存放 JavaScript 文件
│   ├── /images         # 存放图片文件
│   └── /fonts          # 存放字体文件
│
├── /templates          # 存放 HTML 文件
│   ├── index.html              # 首页登录页面
│   ├── register.html           # 注册页面
│   ├── user_dashboard.html     # 用户主页
│   └── admin_dashboard.html    # 管理员主页
│
└── app.py              # Flask 应用的主文件

```

### templates文件夹
- 存放 HTML 文件。`Flask` 使用 `Jinja2` 模板引擎，允许在 HTML 文件中嵌入 Python 代码。当你在视图函数中调用 `render_template` 方法时，`Flask` 会自动从 `templates` 文件夹中查找相应的 HTML 文件，并渲染出最终的网页。

### static文件夹
- 存放静态文件，如 CSS、JavaScript、图片、字体等。这些文件不需要经过服务器端处理，可以直接被浏览器加载。Flask 会自动从 static 文件夹中提供这些文件。

## 数据库配置细节
- 使用 `pyodbc` 连接 `SQL server` 数据库

### 数据库配置
```python
server = 'localhost'  # SQL Server 实例的地址，通常是 'localhost' 或 '127.0.0.1'
database = 'GA_V1'    # 您的数据库名称
username = 'root91'  # 替换为您的 SQL Server 用户名
password = '123456789'  # 替换为您的 SQL Server 密码
driver = '{ODBC Driver 17 for SQL Server}'  # ODBC 驱动程序名称，可以根据安装的版本更改
```
- 在 `SQL server` 中需要创建用户名为 `root91`，密码为`123456789`的用户，提供`SQL server`登录方式，并赋予`root91`用户操作权限，服务器名称为`localhost`提供本地连接，请注意ODBC驱动程序名称需和安装的版本相同。  
- 注意在SQL server 配置管理器中SQL server网络配置->“MSSQLSERVER的协议”中启用TCP/IP协议。  
- SQL server下载地址：https://www.microsoft.com/en-us/sql-server/sql-server-downloads  
- SSMS下载地址：https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16  

### 建库
```sql
USE [master]
GO
CREATE DATABASE [GA_V1]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'GA_V1', FILENAME = N'D:\MSSQL\MSSQL16.MSSQLSERVER\MSSQL\DATA\GA_V1.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'GA_V1_log', FILENAME = N'D:\MSSQL\MSSQL16.MSSQLSERVER\MSSQL\DATA\GA_V1_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
-- 设置数据库兼容级别
ALTER DATABASE [GA_V1] SET COMPATIBILITY_LEVEL = 160
GO
```
- 注意 `FILENAME = N'D:\MSSQL\MSSQL16.MSSQLSERVER\MSSQL\DATA\GA_V1.mdf` 中 `GA_V1` 为需要连接的数据库名，也需注意绝对路径的地址，不然连接失败。

## html模板网站 
https://sc.chinaz.com/tag_moban/html.html

