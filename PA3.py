# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 09:04:49 2024

@author: DWNeumann
"""
import random
import time
import tabulate

def part_move_1D(moves):
    x=0
    counter=0
    for i in range(moves):
        direction=random.choice(["Left","Right"])
        if direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1
        if x==0:
            counter += 1
            break
    return counter

def part_move_2D(moves):
    x=0
    y=0
    counter=0
    for i in range(moves):
        direction=random.choice(["Left","Right","Up","Down"])
        if direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1
        elif direction == "Up":
            y += 1
        elif direction == "Down":
            y -= 1
        if x==0 and y==0:
            counter += 1
            break
    return counter

def part_move_3D(moves):
    x=0
    y=0
    z=0
    counter=0
    for i in range(moves):
        direction=random.choice(["Left","Right","Up","Down","Z_up","Z_down"])
        if direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1
        elif direction == "Up":
            y += 1
        elif direction == "Down":
            y -= 1
        elif direction == "Z_up":
            z += 1
        elif direction == "Z_down":
            z -= 1
        if x==0 and y==0 and z==0:
            counter += 1
            break
    return counter

def main():
    move_values=[20,200,2000,20000,200000,2000000]

    results_1=[]
    results_2=[]
    results_3=[]
    data=[results_1,
          results_2,
          results_3]
#1 dim
    for moves in move_values:
        final_count=0
        for i in range (100):
            final_count += part_move_1D(moves)
        results_1.append(final_count)
    
    # for item in results_1:
    #     print(item)
        
    print(results_1)
    

    # for i, moves in enumerate(move_values):
    #     print(f"Total number of 1 dimension particles that reached 0 for {moves} moves: {results_1[i]}")

#2 dim
    for moves in move_values:
        final_count=0
        for i in range (100):
            final_count += part_move_2D(moves)
        results_2.append(final_count)
    
    print(results_2)

    # for i, moves in enumerate(move_values):
    #     print(f"Total number of 2 dimension particles that reached 0 for {moves} moves: {results_2[i]}")
        
#3 dim

    # Record the start time
    start_time = time.time()
    for moves in move_values:
        final_count=0
        for i in range (100):
            final_count += part_move_3D(moves)
        results_3.append(final_count)
    # Record the end time
    end_time = time.time()
    
    # Calculate and print the elapsed time and total
    elapsed_time = end_time - start_time
    #print(f"Elapsed Time: {elapsed_time} seconds")
    
    print(results_3)

    # for i, moves in enumerate(move_values):
    #     print(f"Total number of 3 dimension particles that reached 0 for {moves} moves: {results_3[i]}")
    print(f" Time is took to run the 3D code: {elapsed_time} seconds")
    
    # headers = ["Name", "Rank", "Specialty"]
    # table = tabulate(data, headers, tablefmt="grid")
    # print(table)

    
main()
