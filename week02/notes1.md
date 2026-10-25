Answers:

1. It printed "/mnt/c/Users/Kaushal" 

2. 'ls -a' showed dots on the left most side, with one dot corresponding to line 1 and 2 dots corresponding to line 2. However plain 'ls' did not show any dots. The rest of the content was the same for the two.

3. "drwxrwxrwx 1 kaushal kaushal 4096 Aug 16 11:23  'brighu lake pdfs + photos' "
It shows the area where the file is stored, the path, the number of files with this name and the date it was last altered.

4. It is a relative path because it doesn't include the entire path. The path is relative to your current location.

5. The first mv moved the file we created 'README-backup.md' into week01, when it was originally in the top layer of coding cafe. The second mv renamed 'README-backup.md' to 'old-readme.md'.

6. 127!!

7. It lives in: /usr/bin/python3

8. They are not the same because the two of us have saved the file differently in our systems, according to our own convenience.

9. 
"Command 'pyton3' not found, did you mean:
  command 'python3' from deb python3 (3.14.3-0ubuntu2)
Try: sudo apt install <deb name>"
--> The system did not find the command because it doesn't exist, but then asked if we had meant to ask about a similarly spelled command, and it provided the PATH of that command for us to understand which exact file it was talking about.

10. .venv is a hidden file - it does not show up in the ls command. But in the ls -a command, hidden files are visible.

11. There is a (.venv) phrase at the beginning of my prompt. It shows that the virtual command of wsl has been activated in my terminal.

12. A different path is visible, namely: '/mnt/c/Users/Kaushal/coding-cafe/.venv/bin/python3'
--> 'activate' added the '.venv' to the PATH, meaning it made the PATH hidden.

13. The second list now includes the requests which weren't there in the first list.    

14. It points to: /usr/bin/python3 --> same as answer for Q7.

15. ls -h produces the output: 'week01'. It shows the file that is in coding-cafe. However it does not show the other file, week02. My guess is because this file is open in VS Code and is being edited currently so the terminal doesn't show it. 

16. Control+C interrupted the keyboard while Control+D brought me back to the user prompt. 