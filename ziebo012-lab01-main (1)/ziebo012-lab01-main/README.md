# 3081 Lab 1: Git
_(Due: Thursday, September 12, 2024 @ 11:59pm)_

## General Information

Welcome to CSCI 3081W Lab. Here you will get practice to familiarize and become proficient with skills and concepts learned in this course. The first 3 weeks of labs will go over some basic, yet very important skills that will be utilized daily throughout the course. Take your time to read and learn what is being covered in these labs rather than just copying and pasting commands as you see them. This will save you a lot of unnecessary backtracking in the future.

In this lab, you will become familiar with some of Git's standard and advanced features. You will simulate a collaborative development environment where you and a teammate will be setting up a repository, and your first step is adding your names to a name file. It is recommended that you have basic knowledge of how to use the command line in Linux. The rest of this document is divided into two parts *General Information*, and *Lab Instructions*. The *General Information* section provides instructions on the background required for this lab and how to access a lab machine to complete the assignment. (If you would like to use your own machine to complete the lab, that is ok but we may not be able to provide troubleshooting help for errors that might be machine-related. If needed, you can find how to install Git on your machine at this [link](https://git-scm.com/downloads).) The section *Lab Instructions* details the instructions for this lab.

Finally, we suggest reading this file on the github webpage for better presentation.


### Background

If you are not familiar with using the command line, you can find a tutorial [here](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview). (For this tutorial, you can use a lab machine; see details in the next paragraph.) In this course, we are going to use the command line extensively and we suggest you feel comfortable using it. 

## Lab Instructions

In the following sections, we use the term "REPO" to indicate the GitHub repository that we have created for you. This repo is located at https://github.umn.edu/umn-csci-3081w-f24-sec010/x500-lab01 where x500 is your x500 ID. **Make sure that this is not a repository you created on your own.** Please let your Grad TA know if you do not have this repo created for you.

Please also make sure to read the whole assignment before getting started and to follow the instructions we provide to the letter (e.g., use the exact commit messages and capitalizations provided in the assignment, rather than variations of them). If you don’t know how to accomplish a task, either consult Git's help by running `git --help <command>` in a terminal, or leverage online resources (there are plenty, such as this [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)). If you receive an error while executing a Git command, make sure to read the error message, as Git often suggests exactly the right thing to do.

This lab is meant for beginners to become familiar with Git and GitHub. If you feel like you are completely lost, ask your classmates, TAs, and instructors for help. You can also look at our class lecture on "Git and Version Control". In addition, you can check the tutorials at [link1](http://try.github.io/levels/1/challenges/1) and [link2](https://learngitbranching.js.org), which should further get you familiar with Git’s basic concepts. There are also plenty of helpful YouTube tutorials and articles online as well.

### Part 0 (GitHub SSH Keys)
GitHub requires users to authenticate every time they want to upload code to any repository, or download code from a private repository. You can type in your username/password every single time, but instead you will setup SSH keys to automatically authenticate your computer with GitHub's servers.

You will need to do these steps for every different machine that you work on the code from. Personal laptop, home desktop, school machines, etc. For school machines, since your home directory `~/` is "synched across machines", if your ssh keys are saved in `~/.ssh/` you will not need to do this every week you switch between lab machines.

1. Generate an SSH key and add it to the SSH agent. [Follow the instructions here.](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) You will need to open a terminal on your computer to run the commands in the guide. Stop after you've added your SSH key to the ssh-agent. Step 3 of Adding your SSH key to the ssh-agent is what we'll be doing next.
2. Add your key to the github.umn.edu server. [Follow the instructions here.](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) Make sure you are adding your key to github.umn.edu, NOT github.com.


### Part 1 (Cloning)
In this section, you will learn how to clone an existing repository in GitHub onto your machine, make a file, then upload it to GitHub.
1. Open a terminal window
2. Make a new folder for this class
    ```bash
    $ mkdir csci-3081w-f24
    ```
3. Go into this new folder (`cd csci-3081w-f24`)
    ```bash
    $ cd csci-3081w-f24
    ```
4. Next you're going to configure Git with your name and school email address. Run the following commands, replacing "your name" and "x500@umn.edu" with the appropriate values: <br>
    ```bash
    $ git config --global user.name "your name"
    $ git config --global user.email "x500@umn.edu"
    ```

    (**Optional**: You can also set your default editor if you would like. For example, to set vim as the default editor, use `git config --global core.editor <editor>` where \<editor\> could be `nano`, `vim`, or `code` for vscode)

5. Now you're going to clone your REPO with the following the command.
***Note: replace x500 with your actual x500***
    ```bash
    $ git clone git@github.umn.edu:umn-csci-3081w-f24-sec010/x500-lab01.git
    ```
    If this command fails, you haven't setup your SSH keys correctly. Review Part 0 to make sure you completed all the steps.

6. Now you should have a directory called `x500-lab01` (e.g., `gango010-lab01`)


### Part 2 (Branching)
1. Make sure you are in your repository directory (`x500-lab01`)
2. From here, when you make changes to your repository, you should not be making changes directly to your `main` branch. So what we want to do is make a new branch from our main branch. To do this, make sure that you are on the main branch by using the `git branch` command.
    ```bash
    $ git branch
      * main
    ```
    Here we can see we are on the main branch because of the "*" star next to main.
3. Next, create a branch with a meaningful name. Typically, the branch name should be something corresponding to the feature that you're implementing, whether that be the ticket name or ID, or the feature itself. For example, use `battery-dev` if we are talking about the drone simulation system and you're implementing a battery.
    ```bash
    $ git checkout -b <x500>-dev
    ```
    In this command, we are creating a branch with the `-b` flag and checking it out immediately after. 

4. Now, you should be on the newly created branch. You can verify this with `git branch`
    ```bash
    $ git branch
    * gango010-dev
      main
    ```
    We can now see that you're on a different branch, `gango010-dev` in my case. **You should have a different branch name corresponding to your x500.**
5. From here, modify the file `name.md` using your favorite editor and add your first and last name to the file.
6.  Now, upload your changes to the `name.md` file to GitHub. To do so, first ***Add*** the changes, then ***commit*** it to your local repo with comment "Added name initials" and finally ***push*** it to your github server.<br>
    
    This command will add the `name.md` file to the commit. Alternatively, you can use `-A` flag to add all the modified files inside the directory.
    ```bash
    $ git add name.md
    ```

    This will commit your added files to the commit stage with the description of what you provide after the tag `-m`.
    ```bash
    $ git commit -m "Added name to name.md"
    ```

    This will finally push your committed files onto the GitHub server.
    ```bash
    $ git push
    ```
    _Note: If the push command fails and you see a message saying "The current branch has no upstream branch", set the upstream branch with..._
    ```bash
    $ git push --set-upstream origin <branch-name>
    ```

### Part 2 (Merging and Merge Conflicts)
**Scenario**: Your teammate Ash has also modified the `name.md` file with his name on another branch named `teammate-dev`.

**Your Task**: **Merge** in yours and your teammate's changes into the `main` branch without overwriting or deleting yours or your teammate's changes.


1. Change back to the main branch. You are likely still on your development branch. Use `git branch` to see what branch you're currently on. To change back to the `main` branch, use the `git checkout <branch-name>` command
    ```bash
    $ git checkout main
    ```
    You can verify that you've switched back to main by using the branch command again.

2. From here, its time to [merge](https://git-scm.com/docs/git-merge) in your changes from your development branch into the branch you're currently in. **It's very important for the rest of the lab that you are in the main branch.**
    ```bash
    $ git merge <branch>
    Fast-forward
    name.md | 1 +
    1 file changed, 1 insertion(+)
    ```
    You should see a message like shown above that the branch was fast-forwarded with 1 change in the file name.md.
3. Now it's time to combine your changes. Merge in your teammate's changes using the `merge` command again. _Don't worry, this command should fail!_
    ```bash
    $ git merge origin/teammate-dev
    ```
    But why did we have "origin/" in front of the branch name this time? This is because that branch has not been pulled locally, yet rather is on the github server through the "origin" alias. We didn't need this because our development branch is local on our machine. We can also work around this by pulling the `teammate-dev` branch locally by doing `git checkout teammate-dev` and this will pull the branch locally. _Again, you do not need to do this if you've run the command above._

4. Are you still calm? Good. What happened here is that both of these changes stemmed from the same [commit id](https://stackoverflow.com/questions/29106996/what-is-a-git-commit-id) thus causing a conflict.
![](pics/lab1_mergeconflict.png)
1. The changes from the branch you tried to merge in (in this case, `teammate-dev`) should now be present in your branch along with your changes, and some added characters that tells you where the merge conflict is. Using an editor, open up the conflicting file and look for a region that looks something like this.
    ```
    >>>>> HEAD
    YourFirstName YourLastName
    =====
    TeammateFirstName TeammateLastName
    <<<<< teammate-dev
    ```
2. To resolve this issue, we want to keep both of the changes, so we can delete the added characters `>>>>>`, `<<<<<`, `=====` and the name of the branches such as "HEAD" and "teammate-dev". Though for future reference, say you just wanted to keep your changes and ignore your teammate's incoming changes, you can delete the symbols as well as your teammate's incoming changes.

    Make sure that only names are left in the files. If you delete the merge symbols noted above, be sure to delete the names of the branches as well. A file called `name.md` should ideally only have names in it.

3. Add, commit and push your changes now that the merge conflict is resolved.
    ```bash
        $ git add name.md
        $ git commit -m "Merged in teammate-dev"
        $ git push
    ```
    You do not need to include `-m "message"` when commiting your changes and just use `git commit`. This will use your selected text editor set up in Part 1 Step 4 where you can edit a file to more easily edit your commit message where you can use up to 500 characters as opposed to `-m` where you're limited to 50 characters.

#### Commit Messages
Be sure to be accurate and descriptive with your git commit messages. Commit messages are very important as they help developers go back and see where bugs and features may have been implemented as well as helping with other processes such as code reviews, composing release notes, and rollbacks. 

> At my last job as a firmware engineer, we had very strict rules on our commit messages. We had a strict template that we needed to follow that involved linking the Jira ticket or Github issue associated with it. Our commits also had to have a detailed writeup of the change that were made.
> These were very helpful when selecting what branches would be merged into the release branch based off their ticket/feature IDs as well as pulling from the commits for generating our release notes and documentation.

### Final Submission

To submit your assignment, post on the Gradescope assignment "Lab 1: Git" your x500 and the commit ID of your latest commit to the main branch. Click [here](https://github.umn.edu/umn-csci-3081-s24/FAQ/blob/main/Commit%20ID/README.md) to see how to get commit id.

### Bonus Comic
[XKCD comic 1597](https://xkcd.com/1597/)

![](pics/git.png)
