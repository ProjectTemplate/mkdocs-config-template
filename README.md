时间：2020/7/1 9:55:22  

参考：

1. [mkdocs](https://www.mkdocs.org/)  
2. [主题](https://jamstackthemes.dev/ssg/mkdocs/)
3. [Typora](https://www.typora.io/)

# 项目
## 项目简介
mkdocs 模板项目，使用 `mkdocs new` 初始化项目之后对修改了一些配置信息，方便配置使用

mkdocs 安装和插件安装可参考 `Mkdocs` 章节内容。

模板效果可参考:  [蓝田的笔记](http://note.sunfeilong.com/)

配置修改的点：

* 主题：使用 `material` 主题。

* 文件构建日期。（基于 git 提交记录，因此要求 `docs` 目录里面的内容是一个 `git项目` ）。

* 代码高亮、代码行数，高亮语法如下,：

    ```go
    func hello(){
        fmt.Println("Hello MkDocs")
    }
    ```
    
* 搜索。

* 目录显示内容精确控制。

## 怎么使用

修改 [build.sh](./build.sh) 脚本中的 `git_repository` 变量内容，然后执行 `build.sh` 脚本,脚本执行结束之后会在当前目录生成 `site` 文件夹，里面是构建好的静态网站,把该目录发布到服务器(nginx,tomcat等)即可访问。
