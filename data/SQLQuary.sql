
--------------------------�������ݿ�--------------------------------
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
-- �������ݿ���ݼ���
ALTER DATABASE [GA_V1] SET COMPATIBILITY_LEVEL = 160
GO

----------------------ǰ��ֿ�ִ�У���Ȼ�ᱨ��-----------------------

-----------------------------������----------------------------------


USE GA_V1;  -- �л��� GA_V1 ���ݿ�
CREATE TABLE Users (
    ID NCHAR(10) NOT NULL PRIMARY KEY,  -- ���� ID �� 10 ���ַ����Ĺ̶������ַ���������Ϊ����
    Nickname NCHAR(50) NOT NULL,        -- Nickname �ֶΣ����賤��Ϊ 50
    Truename NCHAR(50) NOT NULL,        -- Truename �ֶΣ����賤��Ϊ 50
    psw NCHAR(50) NOT NULL,             -- psw �ֶΣ����賤��Ϊ 50
    grade INT NOT NULL                  -- grade �ֶΣ�����Ϊ����
);


-----------------------------�������-------------------------------------
USE GA_V1;  -- �л��� GA_V1 ���ݿ�

INSERT INTO Users (ID, Nickname, Truename, psw, grade)
VALUES 
    (N'1', N'root', N'sam', N'123', 0), 
    (N'2', N'john', N'john', N'456', 1);
