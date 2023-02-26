"""
    The aim of the program is to find all possible combinations,
    for creating a string, from a given substrings
"""

import re

particles = input().split(', ')
example = input()

particles_indexes = {}
particles_count = {}

for w in particles:
    counter = particles.count(w)
    particles_count[w] = counter
    w_indexes = [index.start() for index in re.finditer(pattern=w, string=example)]
    for ind in w_indexes:
        if ind not in particles_indexes:
            particles_indexes[ind] = []
        particles_indexes[ind].append(w)

print(particles_count)
print(particles_indexes)
