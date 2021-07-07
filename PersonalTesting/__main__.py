from Models import Individual, Family
from HTMLs import draw_rectangles, draw_circles, draw_line, draw_children_shapes, draw_pedigree
from PDFs import PDF_Model

import os
import sys
import csv
import networkx as nx

list_inidividuals_file = None

def read_pedigree_file():
    file = open(sys.argv[1], "r")
    list_individuals = []

    file_extension = os.path.splitext(sys.argv[1])[1]

    if file_extension == ".txt" or file_extension == ".ped":
        for line in file:
            words = line.split('\t')
            list_individuals.append(words)
    elif file_extension == ".csv":
        reader = csv.reader(sys.argv[1])
        for line in reader:
            words = line.split()
            list_individuals.append(words)

    file.close()
    return list_individuals


def different_pedigrees():
    global list_individuals_file
    list_individuals_file = read_pedigree_file()
    set_different_pedigrees = set()

    for list in list_individuals_file:
        set_different_pedigrees.add(list[0])

    return set_different_pedigrees


def different_families():
    global list_individuals_file
    set_different_families_names =  different_pedigrees()
    set_different_families = []
    list_different_individuals = []

    for family in set_different_families_names:
        new_family = Family(family, None, None)
        set_different_families.append(new_family)

    for list in list_individuals_file:
        individual = Individual(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7])
        list_different_individuals.append(individual)

    for individual in list_different_individuals:
        if individual.father == "0" and individual.mother == "0":
            for pedigree in set_different_families:
                if pedigree.identifier == individual.identifier_family:
                    if individual.sex == "1":
                        pedigree.set_father(individual)
                    else:
                        pedigree.set_mother(individual)
                    break
        else:
            for pedigree in set_different_families:
                if pedigree.identifier == individual.identifier_family:
                    pedigree.add_child(individual)
                    break

    return set_different_families




list_families = different_families()

for family in list_families:
    family.add_to_graphs()
    print(family, '\n')

def draw_specific_family(specific_family):
    global list_families

    for family in list_families:
        if specific_family == str(family.identifier):
            name_html_file = str(family.identifier) + ".html"
            new_html_file = open(name_html_file, "w")
            message = draw_pedigree(family)
            new_html_file.write(message)
            new_html_file.close()
            break

"""
for family in list_families:
    name_html_file = str(family.identifier) + ".html"
    new_html_file = open(name_html_file, "w")
    message = draw_pedigree(family)
    new_html_file.write(message)
    new_html_file.close()
"""

draw_specific_family("ped1")
draw_specific_family("ped3")

for family in list_families:
    pdf_mode = PDF_Model(family, None, None, None)
    pdf_mode.draw_family()

"""
print("The mating vertices are:\n")

for vertex in Family.vertices_matings:
    print(vertex)
    
print("The subships vertices are:\n")

for vertex in Family.vertices_subships:
    print(vertex)


print("The individuals vertices are:\n")
for vertex in Individual.vertices_individuals:
    print(vertex)
"""