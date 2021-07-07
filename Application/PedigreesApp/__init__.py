from .Models import Individual, Family
from .HTMLs import draw_rectangles, draw_circles, draw_line, draw_children_shapes, draw_pedigree
from .PDFs import PDF_Model

import os
import os.path
import sys
import shutil

from os import path

import csv
import networkx as nx

list_inidividuals_file = None

def read_pedigree_file():
    file = open("../Pedigrees/pedigree_example1.ped", "r")
    list_individuals = []

    file_extension = os.path.splitext("../Pedigrees/pedigree_example1.ped")[1]

    if file_extension == ".txt" or file_extension == ".ped":
        for line in file:
            words = line.split('\t')
            list_individuals.append(words)
    elif file_extension == ".csv":
        reader = csv.reader("../Pedigrees/pedigree_example1.ped")
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
            message = draw_pedigree(family)
            return message

for family in list_families:
    pdf_mode = PDF_Model(family, None, None, None)
    pdf_mode.draw_family()
    name_pdf_file = str(family.identifier) + ".pdf"
    shutil.move("./" + name_pdf_file, "./PedigreesApp/PDF Pedigrees/" + name_pdf_file)