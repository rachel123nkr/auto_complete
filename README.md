# project with google - 
Program that enable completion of sentences from articles, documentation and information files on various technological issues.

The program ran in two stages:
First stage (offline)- The system reads the text files from a pre-determined place and prepares them for the service stage (serving)

Second stage (online) - The system waits for user's input.
The user types characters and presses Enter. The system displays the five best completions. To finish typing the sentence, press #

Quick start
-----------
a. First put all the files you want to run on them in Aechive directory

b. Run the offline stage
 ```
python build_tree.py
 ```
c. Run the online stage
```
python main.py
 ```

Example
-----------
![Farmers Market Finder Demo](https://user-images.githubusercontent.com/44622520/105209858-fb825280-5b52-11eb-9b94-bd2cd247f387.gif)
