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


    def __repr__(self):
        return "Father identifier:\n" + str(self.father) + "\nMother Indentifier:\n" + str(self.mother) + "\nChildrens:\n" + str(self.children) + str('\n')