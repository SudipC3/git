# Working With Branch
Now we want make a new Branch
## Make A Branch
To make a branch use (*git branch branchname*)



            git branch dev

## Changing Branch
Let move on *dev* Branch (*git checkout branchname*)

            git checkout dev

<pre>
linux@linux~# git checkout dev
Switched to branch 'dev'
</pre>

## Make Changes
Now it is on dev branch , make changes which you want for example I change __plug__.py file

<pre>
linux@linux~# git status
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   __plug__.py

no changes added to commit (use "git add" and/or "git commit -a")
</pre>
Now I try to add some file
<pre>
linux@linux~# touch vnc.py

linux@linux~# git status
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   __plug__.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        vnc.py

no changes added to commit (use "git add" and/or "git commit -a")

</pre>
## Save Changes
Now save it
<pre>
linux@linux~# git add .

linux@linux~# git status
On branch dev
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   __plug__.py
        new file:   vnc.py


linux@linux~# git commit -m "first commit on dev"
[dev 563e2a6] first commit on dev
 2 files changed, 13 insertions(+)
 create mode 100644 vnc.py

linux@linux~# git log
commit 563e2a6aa7282c3094f89b40dad8ad0bd1a96da1 (HEAD -> dev)
Author: SadhukhanR <r************@**.com>
Date:   Fri Nov 19 12:42:27 2021 +0000

    first commit on dev

commit d257af468e308c6954527cd11cfd78e153520b8b (master)
Author: SadhukhanR <r***************@**.com>
Date:   Fri Nov 19 12:30:46 2021 +0000

    jgj

commit d6f334a2639ba971267546428d8eccf681da8541 (dev2)
Author: SadhukhanR <r***************@**.com>
Date:   Tue Nov 16 23:50:43 2021 +0000

    add README.md

</pre>
now save it on remote server or Github (*git push -u origin branchname*)


            git push -u origin dev


