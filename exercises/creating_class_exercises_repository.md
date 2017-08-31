## Accessing class exercises and storing your work

Use the following instructions to set up your repository for your individual exercises. This will be the place you work on your class exercises:

You will make your own student remote repository. You should have write access to your student repisitory, but it will be only readable by you, Niall Keleher, and Eve Mwangi. When you complete your exercises, you will use a push command to upload your work to this repository.

## Initial Setup

There are several ways that you can set up your local repository.  We recommend the following procedure.

First, create an empty repository in Github for your exercises, you can do this through the github user interface. 

## Create a new repository 

* this is done through the add menu on the upper right of your Github page.

--

* Put your repository in the INFO206_Fall2017 organization

Name the repository "info206_exercises_[Lastname]". Where [Lastname] is a placeholder for your surname. e.g. info206_exercises_Keleher

--
* Make the repository **private** with the radio button.
 
# Important: Do not add a readme file you need an empty repository

# Give the read access to Niall (NKeleher) and Eve ()

* In your new **private** repository, go to the settings tab, on the right and then select collaborators and teams on the left

* Give (only) Niall and Eve read access only (no need for write priviledges):

## Clone the assignments directory on your local machine

You need to tell git that you will be pulling content (exercises) onto your machine from course_materials and pushing modified content (completed exercises) to info206_exercises_[Lastname] on Github.

Open a command prompt and use it to navigate to your desktop or course working directory.  Then execute the following commands:

*Note: lines preceeded by "#" are comments to explain each step and should not be executed.* 

``` sh
# clone the assignment repository onto your computer

git clone https://github.com/INFO206_Fall2017/course_exercises.git

cd assignment-upstream-fall-2016

git remote add upstream https://github.com/INFO206_Fall2017/course_exercises.git
```

You can find the URL for YourNameREPO by navigating to the appropriate repository in your web browser, then clicking on the "Clone or download" button in the upper right corner.

``` sh
# set the origin to your personal repository

git remote remove origin
git remote add origin <ENTER YOUR REPOSITORY HTTPS URL HERE>

# i.e. git remote add origin https://github.com/MIDS-INFO-W18/info206_exercises_Keleher.git

```

To check if you did everything right, execute the following command:

``` sh
git remote -v
```

* The output should show "fetch" and "pull" for two remotes, one named origin and one named upstream.  

* You should also use the **ls** command to confirm that the course exercise files have been copied to your machine.

## Workflow

For each exercise, you will begin by navigating to your local version of **course_exercises**, and downloading the latest changes from the remote **course_exercises** repository. 

You do this with a git pull:

``` sh
git pull upstream master
```

Next, you complete all the exercises on your local machine and commit your changes to git. Finally, you will push your changes up to your personal student repository on Github.  You can do this with the following command:

```sh
git push origin master
```
