⚠️ This repository is not maintaining by us, check <https://github.com/cx0y/git>
# git
+ ## 1. add git to a project
``` 
git init
```
+ ## 2. add username and email
```
git config --global user.name <your_user_name>
```
```
git config --global user.name "SudipC3"
```
```
git config --global user.email <your_mail>
```
```
git config --global user.email "s********@pm.me"
```
+ ## 3. clone a remote repo
```
git clone <repo_url>
```
```
git clone https://github.com/cx0y/kex.git
```
>>> ### ssh
```
git clone git@github.com:cx0y/xlbr.git
```

+ ## 4 git remote
>> ### view origin
```
git remote -v
```
>> ### add origin
```
git remote add origin <url>
```
>> ### change origin
```
git remote set-url origin <url>
```

# projects
+ ## 5. create branch
```
git checkout -b <branch_name>
```
```
git checkout -b dev2
```
+ ## 6. check branch
```
git branch -a
```
+ ## 7. change branch
```
git checkout <branch_name>
```
```
git checkout dev2
```
+ ## 8. delete a remote branch
```
git push origin --delete <remote_branch_name>
```
```
git push origin --delete dev2
```
+ ## 9. check git tracks
```
git status
```
```
git diff
```
```
git diff --stat
```
+ ## 10. add all files
```
git add .
```
+ ## 11. make a commit
```
git commit -m <your message>
```
```
git commit -m "update"
```
+ ## 12. push commit
```
git push <remote> <branch>
```
```
git push origin main
```
>> ### force push
```
git push --force
```
```
git push -f <remote (origin)> <branch(master)>
```
```
git push origin <branch_name(master)> --force
```
```
git push --force-with-lease
```
+ ## 13. update local branch
```
git fetch <remotename>
```
```
git pull origin <my_default_branch_name>
```
+ ## 14. log
```
git log
```
```
git log origin/branch_name
```
```
git log origin/master
```
```
git log --oneline
```
>> ### checkout log
```
git checkout <hash_of_commit>
```
```
git checkout c3d88eaa1aa4e4d5f
```

+ ## 15. git commit message undo

```
git commit --amend -m <new_commit_message>
```
+ ## 16. reset commit

```
git reset <hash_of_commit>
```
```
git reset 9a9add8
```
+ ## 17. reaverting a commit and write as a new commit
```
git revert HEAD ~ x 
```
> x being a number. 1 going back one more
```
git revert HEAD ~ 1
```
+ ## 18. merge branch
```
git merge <marge_branch_name>
```
```
git merge dev2
```
+ ## 19. delete local branch
```
git branch -d <branch_name>
```
```
git branch -d dev2a
```
+ ## 20. rebase
```
git rebase -i HEAD~x
```
---------------------------------------------------------
# git ~ advanced
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


---------------------------------------------------------

```
MIT License

Copyright (c) 2021 Sudip Bakuli (SudipC3), wiz (cx0y), level up (levelupdefy)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

-------------------------------------------------------------------

| [RAW](https://raw.githubusercontent.com/levelupdefy/git/master/README.md) | [GITHUB](https://github.com/levelupdefy/git) | [WEB](https://levelupdefy.github.io/git/)|
