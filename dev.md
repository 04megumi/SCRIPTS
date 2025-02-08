# 开发文档



## GITHUB_TOKEN

由于github官方限制，21年后远程开发登陆时需要的pw变成了token，而token又十分难

记，所以我把他配置到了环境变量中(SeraphimWei's Linux bash)。如果使用其他设备也

可以参考这个配置



### 打开配置文件(以bash为例)

```bash
vim ~/.bashrc
```



### 在末尾加入以下配置

token不方便展示，可以自己申请或者找我要

```bash
# GitHub Token for Dev
export GITHUB_USERNAME="04megumi"
export GITHUB_TOKEN="your_personal_access_token"
export GIT_PUSH_COMMAND="git push https://$GITHUB_USERNAME:$GITHUB_TOKEN@github.com/04megumi/SCRIPTS.git"
```



### 使配置生效

```bash
source ~/.bashrc
```



### 使用方式

直接在终端使用即可

```bash
$GIT_PUSH_COMMAND
```


