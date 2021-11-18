# Starting With Git
Your first project with Git
<pre>
Here We use Linux Zsh shell, Don't worry you can 
use any shell availabel with your system. You Can also use Github CLI,
Github Desktop, Powershell etc.
</pre>
More info see [Git Installation](install.md)
### Make A Git Repo


           git init 

<pre>

linux@linux~# mkdir github-explore

linux@linux~# cd github-explore

linux@linux~# git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /home/kylin/Github/github-explore/.git/

linux@linux~# ls -a

.  ..  .git


</pre>
 here .git dir contains all information that is necessary for your project
in version control and all information about commits, remote server, etc.


### The Project
Your original project, Let I have a project, which I made and all dir and 
files of this project is

<pre>

linux@linux~# ls
__plug__.py  rdms.vim  README.md  vim.txt

</pre>
> The Commite : In Git, a commite is a snapshot of your repo at specific
point of time.
<br>
<br>
> The Staging Area: Staging area is " files that are going to be a part of the next commite"
### Project Status
How to know which files are into staging area and my project status ?

     
 
           git status


<pre>

linux@linux~# git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        __plug__.py
        rdms.vim
        vim.txt

nothing added to commit but untracked files present (use "git add" to track)


</pre>
you can see no file tracked by Git or no file in staging area.
If I want to put 'README.md' file into staging area, I use *git add <filename>*



          git add README.md


<pre>
linux@linux~# git add README.md

linux@linux~# git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        __plug__.py
        rdms.vim
        vim.txt

</pre>
now you can 'README.md' is tracked.

### Save Changes and Commit
To make a commit use *git commit -m "your message"*



            git commit -m "add README.md"

<pre>
linux@linux~# git commite -m "add README.md"
[master (root-commit) d6f334a] add README.md
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
</pre>

### Check Commit Log
To see chenges log use *git log*



          git log



<pre>
linux@linux~# git log
commit d6f334a2639ba971267546428d8eccf681da8541 (HEAD -> master)
Author: SadhukhanR <r*****************@gmail.com>
Date:   Tue Nov 16 23:50:43 2021 +0000

    add README.md
</pre>
### Adding Remote Repo
First you need to make a remote repository in Github
[How Can I Make A Github Repo](Github/make_github_repo.md)
Adding git remote
#### Over SSH

          git remote add origin git@github.com:SudipC3/github-explore 

#### Over Https


          git remote add origin https://github.com/SudipC3/github-explore



### Push Project To Remote Repo
To push main branch on Github use *git push -u origin main*


             git push -u origin main

