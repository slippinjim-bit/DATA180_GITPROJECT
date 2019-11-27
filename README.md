# DATA 180 GitHub Project
## This is a sample project and Markdown file

## This project is a sample of additional code written for SFU MACM 101.

### Table of Contents
| File          | Description   |
| ------------- |:-------------:|
| README.md|This markdown file  |
| factorial.py    | .py file containing code for 9 combinatoric problems |
| a4p1b.py    | .py file containing code to estimate the completixty of various functions with various input size n    |
| IMG_1242.JPG| A picture of my dog Rudy|

Running these python files simply requires exectution from the terminal or use of the excellent <https://repl.it/>

---

### Sample Code

This problem asked for the ammount of time for a hacker to try all possible password combinations

```python
#hacker with no information
pwt1 = 62**6 + 62**7 + 62**8        #number of passwords hacker must try
secs1 = pwt1/float(pwps)                   #number of seconds to try all passwords
print("number of seconds to try all 6/7/8 digit passwords: " + str(secs1))
sec2 = pwchar/float(pwps)
print("number of seconds to try all passwords if the information about passwords is knows:" + str(sec2))
```


### My Dog Rudy
![alt text](https://github.com/slippinjim-bit/DATA180_GITPROJECT/blob/master/IMG_1242.JPG)
