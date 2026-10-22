1. 为什么要用git？
2. git安装及其初始化操作
3. 掌握git基本命令
4. 掌握git工作流一般步骤，并按照要求创建自己的学习仓库


相关指令：
git status  哪些改了、哪些已暂存、当前分支（全能大王）
git diff    还有什么改动没提交的
git log --oneline --graph --all  看每一次的提交，带分支图
git add .   暂存当前目录的全部改动
git commit -m "xxx"  提交一个名字是“xxx”的修改

git branch                  看本地分支
git switch -c feat/week1    新建并切过去
git switch main             切回主线
git merge feat/week1        把分支并进来
git branch -d feat/week1    合并后删掉

git remote add origin <url>     关联远程仓库，别名叫 origin
git push -u origin main         首次推送，-u 建立跟踪关系，之后就可以直接push了
git pull                        拉取并合并
git fetch                       只拉下来看看，不合并


写每日日志怎么做？
git status                                  检查一下
git diff                                    检查一下×2
git add notes/2026-10-21.md                 我说添加一下笔记
git commit -m "docs: 记录第一天的 Git 笔记"  我说提交一下笔记
git push                                    上传一下

如果说要在项目上完成自己的修改
git status
git switch -c feat/week1
进行一顿提交
git push -u origin feat/week1
git switch main
git pull
git branch -d feat/week1