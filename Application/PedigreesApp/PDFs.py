from matplotlib.patches import Rectangle, Circle

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class PDF_Model():
    colors_affected = ["grey", "white", "red"]

    def __init__(self, family, vertices, codes, current_filling_color):
        self.family = family
        self.vertices = []
        self.codes = []
        self.current_filling_color = None

    def draw_father(self, start_x, start_y, length, width):
        self.current_filling_color = self.colors_affected[int(self.family.father.treat)]
        return Rectangle((start_x, start_y), length, width, linewidth = 1, facecolor = self.current_filling_color, edgecolor = 'black')

    def draw_mother(self, center_x, center_y, radius):
        self.current_filling_color = self.colors_affected[int(self.family.mother.treat)]
        return Circle((center_x, center_y), radius, linewidth = 1, facecolor = self.current_filling_color, edgecolor = 'black')

    def draw_family(self):
        fig, axis = plt.subplots()

        axis.add_patch(self.draw_father(50, 70, 6, 6))
        axis.add_patch(self.draw_mother(75, 73, 3.5))


        axis.plot([56, 71.5], [73, 73], 'black')

        if len(self.family.children) > 0 :
            axis.plot([63.75, 63.75], [73, 60], 'black')
            len_sections = (len(self.family.children) - 1) * 10
            axis.plot([63.75 - len_sections / 2, 63.75 + len_sections / 2], [60, 60], 'black')

            counter_offset = 63.75 - len_sections / 2

            for child in self.family.children:
                axis.plot([counter_offset, counter_offset], [60, 47], 'black')
                

                self.current_filling_color = self.colors_affected[int(child.treat)]

                if child.sex == "0":
                    pass
                elif child.sex == "1":
                    axis.add_patch(Rectangle((counter_offset - 3, 41), 6, 6, linewidth = 1, facecolor = self.current_filling_color, edgecolor = 'black'))

                else:
                    axis.add_patch(Circle((counter_offset, 43.5), 3.5, linewidth = 1, facecolor = self.current_filling_color, edgecolor = 'black'))


                counter_offset = counter_offset + 10
        

        axis.set_title('Name of the pedigree: ' + self.family.identifier)

        plt.xlim(0, 170)
        plt.ylim(0, 100)

        plt.axis('off')

        name_html_file = './' + str(self.family.identifier) + '.pdf'
        plt.savefig(name_html_file, format="pdf")