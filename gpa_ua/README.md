# GPA calculator for Ukrainian diplomas

## Introduction

GPA (Grade Point Average) is a weighted average of diploma's marks.

The formula is simple: (w[1]\*m[1] + ... + w[n]\*m[n]) / (w[1] + ... + w[n]) where
* each summand corresponds to one course taken
* w[i] is number of hours (or credits)\
    It's assumed that hours is some multiple of credits thus the result doesn't change.\
    For example 1 credit might correspond to 36 hours.
* m[i] is mark\
    It can be Ukrainian mark (between 0 and 100) or US mark (between 0 and 4).

## Usage

TO BE DONE