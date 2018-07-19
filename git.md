# 1.setup and config

* `git`
	* `-C <path>`:像在`<path>`目录下运行git,而不是当前目录.不是绝对路径，加上相对于`<path>`路径。下面等价的：

		```
		# 进入c目录（c有a.git目录和工作文件b），执行git status
		git --git-dir=a.git --work-tree=b -C c status
		
		#等价于
		git --git-dir=c/a.git --work-tree=c/b status
		```
	* `-c <name>=<value>`：给命令传递一个配置参数，覆盖配置文件。`git config`中的`<name>`
	* `--git-dir=<path>`:仓库的路径。也可以是环境变量`GIT_DIR`.
	* `--work-tree=<path>`:工作树的目录。也可以用`GIT_WORK_TREE`来设置。
	* `--bare`:将这个库视为bare库
* config
	* `--add`:不改变存在值，增加新行选项。
	* `--get`:获取值
	* `--global`:写到全局`~/.gitconfig`.读也是。
	* `--system`:写到`$(prefix)/etc/gitconfig`
	* `--local`:写到`.git/config`
* help
	* `-a`:所有的命令
	* `-g`:打印手册guides
	* `-i`:显示格式化手册信息
	* `-m`:以man形式显示信息
	* `-web`:web形式显示

# 2.getting and creating project

* `init`：创建新的仓库或已有的重新初始化。
	* `-q`:只打印error和warning信息
	* `--bare`:创建一个bare库
* `clone`:克隆一个新的目录，并创建在当前添加分支`git branch -r`.`git fetch`将会更新所有的远程分支。`git pull`将会远程master分支到当前的分支。默认配置在remote头`refs/remotes/origin`中添加`remote.origin.url`和`remote.origin.fetch`

	```
	[remote "origin"]
		fetch = +refs/heads/*:refs/remotes/origin/*
		url = git@172.16.8.220:aml_02.git
	```
	* `-l`:local从本地机器进行clone。略过正常的转换机制，通过HEAD副本和所有objects和refs目录。`.git/objects/`通过硬链接来尽可能减少空间。如果仓库具体路径如：`/path/to/repo`这个是默认，`--local`是一个空操作。如果仓库是一个URL，这个flag被忽略。当`/path/to/repo`提供，`--no-local`覆盖默认，而使用正常Git传输。
	* `--no-hardlinks`:强制避免对`.git/objects`的硬链接，用来备份。
	* `-s`shared:当本地克隆，不是用硬链接，自动建立`.git/objects/info/alternates`和源码来共享对象，结果的仓库没有任何自己的对象。**这是个危险操作**
	* `-q`:quiet进程不向标准错误进程报告。
	* `-v`:verbose不影响标准错误报告。
	* `-b`:bare制作一个bare仓库。
# 3.basic snapshotting

* `add`:
* `status`:
* `diff`:
* `commit`:
* `reset`:
* `rm`:
* `mv`:

# 4.braching and merging

* branch
* checkout
* merge
* mergetool
* log
* stash
* tag
* worktree

# 5.sharing and updating projects

* fetch
* pull
* push
* remote
* submodule

# 6.inspection and comparison

* show
* log
* diff
* shortlog
* describe

# 7.patching

* apply
* cherry-pick
* diff
* rebase
* revert

# 8.debugging

* bisect
* blame
* grep

