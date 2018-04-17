本仓库存放个人常用的一些git hook

## :point_right:myblog

使用pre-commit钩子，只适用于个人博客[朱晓伟的博客](http://hanamichi.wiki)，实际执行的脚本在**my_srcipt**文件夹中，放在博客仓库的根目录。

该钩子的作用是在提交时触发更新博客仓库的readme文件，在comit时加入参数`--no-verify`禁用该钩子。

## :point_right:validateCommitMsg

当代码库每次提交的commit msg需要做验证时，可以使用update钩子，这是一个服务端钩子。

对commit msg的验证采用类似**angularjs**的提交规则

### 代码提交规范

#### *Git commit日志基本规范*

```bash
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

**格式要求**:

```bash
# head：50个字符以内，描述主要变更内容
#
# body：更详细的说明文本，建议72个字符以内。 需要描述的信息包括:
#
# * 为什么这个变更是必须的? 它可能是用来修复一个bug，增加一个feature，提升性能、可靠性、稳定性等等
# * 他如何解决这个问题? 具体描述解决问题的步骤
# * 是否存在副作用、风险? 
#
# footer：如果需要的化可以添加一个链接到issue地址或者其它文档，或者关闭某个issue。
```

commig msg包含3个部分：**head**，**body**，**footer**，其中body和footer不是必须。

**type类型**如下:

> type代表某次提交的类型，比如是修复一个bug还是增加一个新的feature。

- feat: 新增 feature
- fix: 修复 bug
- docs: 仅仅修改了文档，比如 README, CHANGELOG等等
- style: 仅仅修改了空格、格式缩进、逗号等等，不改变代码逻辑
- refactor: 代码重构，没有加新功能或者修复 bug
- perf: 优化相关，比如提升性能、体验
- test: 测试用例，包括单元测试、集成测试等
- chore: 改变构建流程、或者增加依赖库、工具等
- revert: 回滚到上一个版本

**scope类型**：

> 用来说明此次修改的影响范围 ，非必须

* all :表示影响面大 ，如修改了网络框架  会对整个程序产生影响 
* loation :表示影响小，某个小小的功能  
* module :表示会影响某个模块