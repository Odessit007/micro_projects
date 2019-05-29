# GPA calculator for Ukrainian diplomas

## Introduction

GPA (Grade Point Average) is a weighted average of diploma's marks.

The formula is simple: `(w[1] * m[1] + ... + w[n] * m[n]) / (w[1] + ... + w[n])` where
* each summand corresponds to one course taken
* `w[i]` is number of hours (or credits)\
    It's assumed that hours is some multiple of credits thus the result doesn't change.\
    For example 1 credit might correspond to 36 hours.
* `m[i]` is mark\
    It can be Ukrainian mark (between 0 and 100) or US mark (between 0 and 4).

## Usage

Add information about your courses in file `data.csv` with the following format:

```
hours,marks,exam
360,92,1
```

The columns can go in arbitrary order.

There can be any other columns in file but these three are mandatory:
* `hours` is number of hours (positive integer)
* `marks` is Ukrainian mark (positive integer between 0 and 100)
* `exam` is 1 if it was exam (any ECTS letter except P) and 0 otherwise (ECTS letter P)

The program will compute 4 GPA values and you can choose the one that better fits your needs:
* Using Ukrainian marks:
    * Using only exams
    * Using all marks
* Converting to US marks:
    * Using only exams
    * Using all marks

The resulting numbers are rounded to 2 decimal places.
