#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    r = []
    while True:
        comand = input().lower()
        match comand:
            case "exit":
                break
            case "add":
                to = input("To where? ")
                n = input("Flight id? ")
                t = input("Type of plain? ")
                rn = {
                    "to": to,
                    "n": n,
                    "t": t
                }
                r.append(rn)
                if len(r) > 0:
                    r.sort(key=lambda item: item.get("to"))
            case "search":
                t1 = input("Type of plain? ")
                d = 0
                for rn in r:
                    if rn.get("t") == t1:
                        print("Going to " + rn.get("to") + " With flight id " + rn.get("n"))
                        d += 1
                if d == 0:
                    print("Not a type of plain or that type dosn`t servicing a flight")
            case "delete":
                fi = input("Flight id to delete? ")
                e = len(r)
                r = [rn for rn in r if rn.get("n") != fi]
                removed = e - len(r)
            case "list":
                if not r:
                    print("No flights in the list.")
                else:
                    print(f"{'No.':<4} {'To':<15} {'Flight id':<10} {'Type'}")
                    for i, rn in enumerate(r, 1):
                        print(f"{i:<4} {rn.get('to'):<15} {rn.get('n'):<10} {rn.get('t')}")
            case "help":
                print("Available commands:")
                print("  add     - add a new flight to the list")
                print("  search  - find flights by plane type")
                print("  delete  - delete flights by flight id")
                print("  list    - show all flights")
                print("  exit    - exit the program")
            case _:
                print("Unknown command. Type help to see available commands.")
