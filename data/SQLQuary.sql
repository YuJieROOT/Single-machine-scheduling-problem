
--------------------------创建数据库--------------------------------
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

----------------------前后分开执行，不然会报错-----------------------

-----------------------------创建表----------------------------------


USE GA_V1;  -- 切换到 GA_V1 数据库
CREATE TABLE Users (
    ID NCHAR(10) NOT NULL PRIMARY KEY,  -- 假设 ID 是 10 个字符长的固定长度字符串，并作为主键
    Nickname NCHAR(50) NOT NULL,        -- Nickname 字段，假设长度为 50
    Truename NCHAR(50) NOT NULL,        -- Truename 字段，假设长度为 50
    psw NCHAR(50) NOT NULL,             -- psw 字段，假设长度为 50
    grade INT NOT NULL                  -- grade 字段，类型为整数
);


-----------------------------添加数据-------------------------------------
USE GA_V1;  -- 切换到 GA_V1 数据库

INSERT INTO Users (ID, Nickname, Truename, psw, grade)
VALUES 
    (N'1', N'root', N'sam', N'123', 0), 
    (N'2', N'john', N'john', N'456', 1);
