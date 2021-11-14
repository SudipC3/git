# Access Github via SSH Server
You can easily access Github via ssh server.
<br>
You can link git and github through ssh server.
<br>
First you need to generate RSA Key Pair 
    
     ssh-keygen -t rsa -b 4096 -C "your-mail@example.com"
Then Start SSH on background

     $ eval "$(ssh-agent -s)"

Now add ssh with your Git 

     ssh-add ~/.ssh/id_rsa

 Copy your rsa.pub file ( path : ~/.ssh/ )

 Open your github page and go to "setting" and click 
 <br>
"SSH and GPG Keys" and paste your ssh public key.
Now you open git into terminal and paste following command

     ssh -T git@github.com

 if you done this process correctly then
 <br>
  
 output look like this  

    Enter passphrase for key '/root/.ssh/id_rsa': 
    Hi YourUserName! You've successfully authenticated, but GitHub does not provide shell access. 
 
