class Individual():
    def __init__(self, identifier_family, identifier_human, father, mother, sex, treat, marker1, marker2):
        self.identifier_family = identifier_family
        self.identifier_human = identifier_human
        self.father = father
        self.mother = mother
        self.sex = sex
        self.treat = treat
        self.marker1 = marker1
        self.marker2 = marker2

    def __repr__(self):
        return "Identifer Family " + str(self.identifier_family) + "\nIdentifier Human " + str(self.identifier_human) + "\nFather " + str(self.father) + "\nMother " + str(self.mother) + "\nSex " + str(self.sex) + "\nTreat " + str(self.treat)


class Family():
    def __init__(self, identifier):
        self.identifier = identifier
        self.children = []

    def set_father(self, father):
        self.father = father

    def set_mother(self, mother):
        self.mother = mother

    def add_child(self, child):
        self.children.append(child)

    def print_children(self):
        children_string = str()

        for child in self.children:
            children_string.append(str(child))
            children_string.append('\n')

        return children_string


    def __repr__(self):
        return "Father identifier:\n" + str(self.father) + "\nMother Indentifier:\n" + str(self.mother) + "\nChildrens:\n" + str(self.children)


def read_pedigree_file(file_path):
    file = open(file_path, "r")
    list_individuals = list()

    for line in file:
        words = line.split()
        list_individuals.append(words)

    file.close()
    return list_individuals


def different_pedigrees():
    list_individuals = read_pedigree_file("../Pedigrees/pedigree_example1.ped")
    set_different_pedigrees = set()

    for list in list_individuals:
        set_different_pedigrees.add(list[0])

    return set_different_pedigrees


def different_families():
    list_individuals = read_pedigree_file("../Pedigrees/pedigree_example1.ped")
    set_different_families_names =  different_pedigrees()
    set_different_families = []
    list_different_individuals = []

    for family in set_different_families_names:
        new_family = Family(family)
        set_different_families.append(new_family)

    for list in list_individuals:
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


    


set_individuals = different_families()


for family in set_individuals:
  print(family, '\n')