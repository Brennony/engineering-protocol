# Git Notes

## Why Git Exists
Git exists because developers need a simple and effect way to collaborate with eachother on complex systems over different interfaces in a way that allows for easy transfer and access to code and information. It also helps devs manage the history and snapshots of a project. Basically, it's like a community-office google drive.
##### Examples:
- Multiple developers working on a game engine can each update different parts without overwriting each other.
- A team building a website can track every change made to HTML, CSS, and JavaScript files.
- Students collaborating on a class project can share code without emailing files back and forth.

## Repository
Reposistory's are basically just huge file and code databases that house the information that people create and versions of those files. It's like a file explorer that keeps records of all the changes you make and allows you to go back to different snapshots of the folders. 
##### Examples:
- A repo for a mobile app containing folders for UI, backend, assets, and documentation.
- A repo for a robotics project storing Arduino code, CAD files, and wiring diagrams.
- A repo for class assignments where each homework is a folder with its own commit history.

## Commits
Commits snapshots and versions of code at specific times and points. They are basically like photos of a room that you are decorating, allowing you to see all the parts and places where you made additions and changed things up. 
##### Examples:
- “Added login page UI”
- “Fixed bug where robot arm wouldn’t stop rotating”
- “Refactored physics engine for better performance”
- “Updated README with installation instructions”

## Branches
Branches are very simple in the way they function. They allow for you to use the code you already have, but being able to add to it and put things into the code without affecting the main database or original code. It helps for bug fixes and feature making, like sketching on an already made model in 
SolidWorks.
##### Examples:
- feature/payment-system — adding a new payment feature without touching main.
- bugfix/camera-freeze — fixing a camera glitch in a game.
- experiment/new-ai-model — trying a new machine learning model without breaking the working version.

## Merge
And if Branches are like sketches on a 3D model in SolidWorks, then merging is like finally adding those sketches to the 3D model through extruding or other features. Aptly named, merging is just taking the branches and putting them in the main repository.
##### Examples:
- Merging a finished login system into main.
- Merging a bugfix branch that solves a crash issue.
- Merging documentation updates from a teammate.

## GitHub
GitHub is the cloud backup site basically, where people can share and edit files online or even code directly on the site. It allows for people to share ideas, upload snapshots and versions on the web, and many more feature. The best way I've seen it used so far is in CS50 where they use GitHub for student file uploads.
##### Examples:
- Hosting open-source projects like Linux, React, or Blender.
- Collaborating on homework with classmates.
- Using GitHub Actions to automatically test code when someone pushes changes.
- Storing your portfolio projects publicly for employers to see.

## Diagram of Git Process
┌──────────────────────────────┐
│        Remote Repo            │
│          (GitHub)             │
└──────────────────────────────┘
              ▲
              │ git pull
              │ (fetch + merge)
              │
┌──────────────────────────────┐
│     Local Repository          │
│ (Full history stored locally) │
└──────────────────────────────┘
              ▲
              │ git commit
              │
┌──────────────────────────────┐
│      Staging Area             │
│ (Files ready to be committed) │
└──────────────────────────────┘
              ▲
              │ git add
              │
┌──────────────────────────────┐
│   Working Directory           │
│ (Your actual project files)   │
└──────────────────────────────┘
              ▲
              │ You edit files
              │
┌──────────────────────────────┐
│        Local Machine          │
│ (Your laptop / VS Code area)  │
└──────────────────────────────┘
              │
              │ git push
              ▼
┌──────────────────────────────┐
│        Remote Repo            │
│          (GitHub)             │
└──────────────────────────────┘


## Common Commands
I learned about main basic commands: 
1. Git Init which initializes the system, makes repos, or parts of the system
2. Git Status which shows files and their statuses
3. Git Log which shows the commits that have happened
4. Git Remote which Pushes
5. Git Fetch which gets latest changes without merging
6. Git Checkout which can be used to check branches
There's more than this but this is what I can recall and have written down, theses are also not counting cd, mkdir, and rm commands since those are common terminal commands.

## Things That Surprised Me
My biggest surprise was really just how easy it is to branch off into features and merge code together in the local, since I thoughht it would be a much bigger hassle (I guess that's what the point of branching is). Another thing that surprised me is how much is actually put into uploading changes to the remote database, since even uploading and changing something as simple as a file name took a lot of time and research to figure out. 

## Questions I Still Have
I have a lot, mainly on what commands do what. Can I merge conflicting code, and what would take priority if done so? What do professionals put into commits to make them meaninful? How does a software engineer use GitHub in their daily life to create and build systems when they can do it from something like VS code by itself?