server = 'localhost'  # SQL Server 实例的地址，通常是 'localhost' 或 '127.0.0.1'
database = 'GA_V1'    # 您的数据库名称
username = 'root91'  # 替换为您的 SQL Server 用户名
password = '1234567890'  # 替换为您的 SQL Server 密码
driver = '{ODBC Driver 17 for SQL Server}'  # ODBC 驱动程序名称，可以根据安装的版本更改

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()