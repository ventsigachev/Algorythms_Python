"""
    The aim of the program is to find all possible combinations,
    for creating a string, from a given substrings.
        • On the first line, you will receive the strings (separated by comma and space ", ")
        • There might be repeating elements in the input
        • On the next line, you will receive the target string
        • Print each of founded ways to form the target string

"""

import re


def get_variations(e, p_i, p_c, ind=0, variations=None):
    if not variations:
        variations = []

    if ind >= len(e):
        print(' '.join(variations))
        return

    if ind not in p_i:
        return

    for p in p_i[ind]:
        if p_c[p] == 0:
            continue
        variations.append(p)
        p_c[p] -= 1

        get_variations(e, p_i, p_c, ind + len(p), variations)

        variations.pop()
        p_c[p] += 1


def main():
    particles = input().split(', ')
    example = input()

    particles_indexes_in_example = {}
    particles_count = {}

    for w in particles:
        counter = particles.count(w)
        particles_count[w] = counter
        w_indexes = [index.start() for index in re.finditer(pattern=w, string=example)]
        for ind in w_indexes:
            if ind not in particles_indexes_in_example:
                particles_indexes_in_example[ind] = []
            if w not in particles_indexes_in_example[ind]:
                particles_indexes_in_example[ind].append(w)

    # print(particles_count)
    # print(particles_indexes_in_example)

    get_variations(example, particles_indexes_in_example, particles_count)


if __name__ == "__main__":
    main()


"""
Possible Inputs:

text, me, so, do, m, ran
somerandomtext

Word, cruncher, cr, h, unch, c, r, un, ch, er
Wordcruncher

tu, stu, p, i, d, pi, pid, s, pi
stupid

"""
