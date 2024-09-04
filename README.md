# Flask开发Web应用
## 项目主结构
- **/project**: 项目根目录。
  - **/static**: 静态文件夹，存放CSS、JavaScript、图片等文件。
    - **/css**: 存放样式表文件。
    - **/js**: 存放JavaScript文件。
    - **/images**: 存放图片文件。
    - **/fonts**: 存放字体文件
  - **/templates**: 存放HTML文件。
    - **index.html**: 首页登录页面。
    - **register.html**: 注册页面。
    - **user_dashboard.html**: 用户主页
    - **admin_dashboard.html**: 管理员主页
  - **app.py**: Flask应用的主文件。
  
### templates文件夹
存放HTML文件。Flask使用Jinja2模板引擎，允许在HTML文件中嵌入Python代码。当你在视图函数中调用render_template方法时，Flask会自动从templates文件夹中查找相应的HTML文件，并渲染出最终的网页。

### static文件夹
存放静态文件，如CSS、JavaScript、图片、字体等。这些文件不需要经过服务器端处理，可以直接被浏览器加载。Flask会自动从static文件夹中提供这些文件。



