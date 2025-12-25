#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def check_brackets(s, balance=0):
    if balance < 0:
        return False
    if not s:
        return balance == 0
    ch = s[0]
    if ch == '(':
        return check_brackets(s[1:], balance + 1)
    elif ch == ')':
        return check_brackets(s[1:], balance - 1)
    else:
        return check_brackets(s[1:], balance)
if __name__ == '__main__':
    print(check_brackets(input()))
