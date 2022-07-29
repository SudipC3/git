# git
+ ## 1. add git to a project
``` 
git init
```
+ ## 2. add usermane and email to git
```
git config --global user.name "your_user_name"
```
```
git config --global user.name "SudipC3"
```
```
git config --global user.email "your_mail"
```
```
git config --global user.email "s********@pm.me"
```
+ ## 3. clone a repo
```
git clone repo_url
```
```
git clone https://github.com/sadhukhanr/papae
```
# project
+ ## 4. create branch
```
git checkout -b branch_name
```
```
git checkout -b dev2
```
+ ## 5. check branch
```
git branch -a
```
+ ## 6. delete a remote branch
```
git push origin --delete remote_branch_name
```
```
git push origin --delete dev2
```
+ ## 7. check git tracks
```
git status
```
+ ## 8. add all files on git track
```
git add .
```
+ ## 9. make a commit
```
git commit -m "your message"
```
```
git commit -m "rsadhukhan: update"
```
+ ## 10. push git remote repo
```
git push
```
+ ## 11. update remote repo to local
```
git pull
```
+ ## 12. ckeck git log
```
git log origin/branch_name
```
```
git log origin/master
```

---------------------------------------------------------
# git: Advanced
> ## 1. add a ssh-key
>> ### generate RSA key pair
```
ssh-keygen -t rsa -b 4096 -C "your-mail@example.com"
```
>> ### start ssh on background
```sh
$ eval "$(ssh-agent -s)"
```
>> ### add ssh to git
```sh
ssh-add ~/.ssh/id_rsa
```
>> ### add public key to github
```
Copy your rsa.pub file ( path : ~/.ssh/ )
```
```
goto -> github profile > settings > SSH and GPG Keys ~ [paste public key]
```
>> ### test ssh
```
ssh -T git@github.com
```
```
Enter passphrase for key '/root/.ssh/id_rsa': 
Hi YourUserName! You've successfully authenticated, but GitHub does not provide shell access. 
```




