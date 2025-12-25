#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def normalize(*args, **kwargs):
    s = kwargs.get('scale', 1.0)
    v = []
    for a in args:
        if isinstance(a, (list, tuple, set, range)):
            v.extend(a)
        else:
            v.append(a)
    if not v:
        return []
    min_v = min(v)
    max_v = max(v)
    if min_v == max_v:
        return [0.0] * len(v)
    k = s / (max_v - min_v)
    return [(x - min_v) * k for x in v]
if __name__ == '__main__':
    print(normalize([1, 2, 3], (4, 5), scale=10))
