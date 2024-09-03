import pyodbc
from flask import Flask, render_template, request, redirect, url_for, session

from GA_V1 import genetic_algorithm

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 需要设置一个密钥来处理会话

# 连接数据库
server = 'localhost'  # SQL Server 实例的地址，通常是 'localhost' 或 '127.0.0.1'
database = 'GA_V1'    # 您的数据库名称
username = 'root91'  # 替换为您的 SQL Server 用户名
password = '1234567890'  # 替换为您的 SQL Server 密码
driver = '{ODBC Driver 17 for SQL Server}'  # ODBC 驱动程序名称，可以根据安装的版本更改

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()


# 登录页面路由
@app.route("/", methods=["GET", "POST"])
def index():
    status = request.args.get('status')

    if request.method == "POST":
        # 管理员登录
        if 'adminUsername' in request.form and 'adminPassword' in request.form:
            admin_username = request.form.get("adminUsername")
            admin_password = request.form.get("adminPassword")

            cursor.execute("SELECT grade FROM Users WHERE Users.nickname = ?", (admin_username,))
            grade = cursor.fetchall()

            cursor.execute("SELECT psw FROM Users WHERE Users.nickname = ?", (admin_username,))
            correct_admin_password = cursor.fetchall()

            if len(grade) == 0 or grade[0][0] != 0: # 当不是管理员
                return redirect(url_for('index', status='admin_username_error'))
            elif len(correct_admin_password) == 0 or admin_password != correct_admin_password[0][0].strip(): # 当密码输入错误
                return redirect(url_for('index', status='admin_password_error'))
            else:
                # 管理员登录成功逻辑
                session['admin_logged_in'] = True
                session['adminname'] = admin_username
                session['adminpassword'] = admin_password
                return redirect(url_for('admin_dashboard'))
        # 普通用户登录
        elif 'username' in request.form and 'password' in request.form:  # 用户登录
            username = request.form.get("username")
            password = request.form.get("password")

            cursor.execute("SELECT NickName FROM Users WHERE Users.nickname = ?", (username,))
            NickName = cursor.fetchall()

            cursor.execute("SELECT TrueName FROM Users WHERE Users.nickname = ?", (username,))
            TrueName = cursor.fetchall()

            cursor.execute("SELECT psw FROM Users WHERE Users.nickname = ?", (username,))
            correct_password = cursor.fetchall()

            if len(NickName) == 0 or username != NickName[0][0].strip():
                return redirect(url_for('index', status='username_error'))
            elif len(correct_password) == 0 or password != correct_password[0][0].strip():
                return redirect(url_for('index', status='password_error'))
            else:
                session['logged_in'] = True
                session['username'] = username
                session['truename'] = TrueName[0][0].strip()
                session['password'] = password
                return redirect(url_for('user_dashboard', status='notshow_message'))

    return render_template('index.html', status=status)

# 注册页面路由
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        truename = request.form.get("truename")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if password != confirm_password:
            return redirect(url_for('register', status='error'))

        # 获取最后一个用户的 ID
        cursor.execute('SELECT ID FROM Users')
        lastId = cursor.fetchall()[-1][0]

        # 插入新的用户到数据库
        cursor.execute(
            "INSERT INTO Users (ID, NickName, TrueName, psw, grade) VALUES (?, ?, ?, ?, ?)",
            (str(int(lastId)+1), str(nickname), str(truename), str(password), 1)
        )
        # 提交事务以保存更改
        cursor.connection.commit()

        return redirect(url_for('index', status='register_success'))

    return render_template('register.html')


# 用户仪表盘页面路由
@app.route("/user_dashboard", methods=["GET", "POST"])
def user_dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('index'))  # 确保用户已登录

    if request.method == "POST":
        action = request.form.get("action")
        if action == "profile":
            # 处理个人中心逻辑
            return redirect(url_for('user_dashboard', status='show_message'))

        elif action == "view_tasks":
            # 处理展示调度结果逻辑
            # 参数设置
            rest_time = 10  # 机器维修时间
            max_work_time = 20  # 机器允许的单批次最大时间
            population_size = 30  # 搜索种群
            generations = 300  # 最大迭代次数

            tasks_name = session['tasks_name']
            tasks_time = session['tasks_time']
            wait_coefficients = session['wait_coefficients']

            optimal_batches, min_time, best_batch = genetic_algorithm(tasks_name, tasks_time, population_size,
                                                                      generations, wait_coefficients, max_work_time,
                                                                      rest_time)
            batch_str = ""
            for i, batch in enumerate(best_batch):
                batch_str += ("批次" + str(i + 1) + str(batch) + "\n")

            # return render_template('user_dashboard.html',status='show_results',task_result=task_result)

            return render_template('user_dashboard.html', status='show_results', optimal_batches=optimal_batches,
                                   min_time=min_time, batch_str=batch_str)

        elif action == "logout":
            session.pop('logged_in', None)
            session.pop('username', None)
            session.pop('truename', None)
            session.pop('password', None)
            return redirect(url_for('index'))

    return render_template('user_dashboard.html')


# 管理员仪表盘页面路由
@app.route("/admin_dashboard", methods=["GET", "POST"])
def admin_dashboard():
    if 'admin_logged_in' not in session:
        return redirect(url_for('index'))  # 确保管理员已登录
    task_result = None  # 默认值
    if request.method == "POST":
        action = request.form.get("action")
        
        if action == "profile":
            # 显示管理员信息
            return redirect(url_for('admin_dashboard', status='show_admin_message'))
        
        elif action == "add":
            # 处理添加调度任务逻辑
            tasks_name= request.form.get("String") # 捕获从管理员输入得到的调度序列
            tasks_time = request.form.get("Time") # 捕获从管理员输入得到的理想工作时长
            wait_coefficients = request.form.get("Deterioration") # 捕获从管理员输入得到的恶化率

            # 将调度序列转为列表
            tasks_name = tasks_name.split(",")
            tasks_time = list(map(int, tasks_time.split(",")))
            wait_coefficients = list(map(float, wait_coefficients.split(",")))

            session['tasks_name'] = tasks_name
            session['tasks_time'] = tasks_time
            session['wait_coefficients'] = wait_coefficients

            return redirect(url_for('admin_dashboard'))

        
        elif action == "delete":
            # 处理删除队列工作逻辑
            Delete_work_name = request.form.get("Delete_work") # 捕获从管理员输入得到的需删除工作
            Delete_task_name = "'" + Delete_work_name + "'"
            print(Delete_work_name)

            tasks_name = session['tasks_name']
            tasks_time = session['tasks_time']
            wait_coefficients = session['wait_coefficients']

            print((tasks_name))

            if Delete_work_name in tasks_name:
                # 获取 Delete_work_name 的索引位置
                index = tasks_name.index(Delete_work_name)

                # 从列表中移除 Delete_work_name
                tasks_name.pop(index)
                tasks_time.pop(index)
                wait_coefficients.pop(index)

                # 更新 session 中的 tasks_name
                session['tasks_name'] = tasks_name
                session['tasks_time'] = tasks_time
                session['wait_coefficients'] = wait_coefficients

                print(session['tasks_name'])


            return redirect(url_for('admin_dashboard'))
        
        elif action == "show":
            # 处理展示调度结果逻辑
            # 参数设置
            rest_time = 10  # 机器维修时间
            max_work_time = 20  # 机器允许的单批次最大时间
            population_size = 30  # 搜索种群
            generations = 300  # 最大迭代次数

            tasks_name = session['tasks_name']
            tasks_time = session['tasks_time']
            wait_coefficients = session['wait_coefficients']

            optimal_batches, min_time, best_batch = genetic_algorithm(tasks_name, tasks_time, population_size,
                                                                      generations, wait_coefficients, max_work_time,
                                                                      rest_time)
            batch_str = ""
            for i, batch in enumerate(best_batch):
                batch_str += ("批次" + str(i+1) + str(batch) + "\n")

            return render_template('admin_dashboard.html',status='show_results',optimal_batches=optimal_batches, min_time=min_time, batch_str=batch_str)
        
        # 其他逻辑
        elif action == "adminlogout":
            session.pop('admin_logged_in', None)
            session.pop('adminname', None)
            session.pop('truename', None)
            session.pop('adminpassword', None)
            return redirect(url_for('index'))

    return render_template('admin_dashboard.html',task_result=task_result)


if __name__ == '__main__':
    app.run(debug=True)