### :point_right:myblog

使用pre-commit钩子，只适用于个人博客[朱晓伟的博客](hanamichi.wiki)，实际执行的脚本在**my_srcipt**文件夹中，放在博客仓库的根目录。

该钩子的作用是在提交时触发更新博客仓库的readme文件，在comit时加入参数`--no-verify`禁用该钩子。