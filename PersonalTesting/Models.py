import networkx as nx

class Individual():
    def __init__(self, identifier_pedigree, identifier_human, father, mother, sex, treat, marker1, marker2):
        self.identifier_pedigree = identifier_pedigree
        self.identifier_human = identifier_human
        self.father = father
        self.mother = mother
        self.sex = sex
        self.treat = treat
        self.marker1 = marker1
        self.marker2 = marker2

    def __repr__(self):
        return "Identifer Family " + str(self.identifier_pedigree) + "\nIdentifier Human " + str(self.identifier_human) + "\nFather " + str(self.father) + "\nMother " + str(self.mother) + "\nSex " + str(self.sex) + "\nTreat " + str(self.treat)


class Family():
    def __init__(self, identifier, father, mother):
        self.identifier = identifier
        self.father = None
        self.mother = None
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

    def add_to_graphs(self):
        names_father_mother_concatenation = str(self.father.identifier_human) + " " + str(self.mother.identifier_human)
        names_children_concatenation = str()

        for child in self.children:
            names_children_concatenation += (str(child.identifier_human) + " ")
        

    def __repr__(self):
        return "Father identifier:\n" + str(self.father) + "\nMother Indentifier:\n" + str(self.mother) + "\nChildrens:\n" + str(self.children) + str('\n')

class Graph():
    def __init__(self, identifier_pedigree):
        self.identifier_pedigree = identifier_pedigree
        self.graph = nx.interval_graph([])
        self.vertices_individuals = set()
        self.vertices_matings = set()
        self.vertices_sibships = set()

    def add_individual(self, individual):
        self.vertices_individuals.append(individual)
        
    def add_mating(self, mating):
        self.vertices_matings.append(mating)

    def add_sibship(self, sibship):
        self.vertices_sibshi