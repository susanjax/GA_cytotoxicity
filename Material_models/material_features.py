from pymatgen.core.periodic_table import Specie
from pymatgen.core.composition import Element, Composition
import re
import numpy
import pandas as pd

eddb = pd.read_csv('const.csv')
#print(df)
db = pd.read_csv('Cytotoxicity.csv')
db_material = db['material']
#compounds = numpy.ndarray.tolist(db_material.unique())
compds = ['SiO2', 'Fe3O4', 'Ag', 'TiO2', 'Au', 'ZnO', 'Pt', 'CuO', 'CeO2', 'Co3O4', 'MgO', 'Ni', 'Al2O3', 'ZrO2', 'NiO', 'Cu', 'Bi2O3', 'C']

#print(compounds)
def composite(formula):
    regex = re.compile(
        r'([A-Z][a-z]?)(\s+)?(\d+(?:\.\d+)?)?(\s+)?([A-Z][a-z]?)?(\s+)?(\d+(?:\.\d+)?)?(\s+)?([A-Z][a-z]?)?(\s+)?(\d+(?:\.\d+)?)?')
    find = regex.search(formula)
    el_1, el_2 = find.group(1), find.group(5)
    el_1_coef, el_2_coef = find.group(3), find.group(7)

    if el_1_coef == None:
        el_1_coef = 1
    if el_2_coef == None:
        el_2_coef = 1
    if el_2 == None:
        el_2_coef = 0

    return el_1, el_1_coef, el_2, el_2_coef



def ed(formula):
    el_1, el_1_coef, el_2, el_2_coef = composite(formula)
    comp = Composition(formula)
    el1 = Element(el_1)
    mx = comp.average_electroneg
    radii = el1.atomic_radius
    if el_2 != None:
        os = list(comp.oxi_state_guesses())[0][el_1]
        if 3 > os > 2:
            os = 2.5
            rad_3 = float(el1.ionic_radii[3])
            rad_2 = float(el1.ionic_radii[2])
            rad = (rad_3+rad_2)/2
        elif el_1 == 'Ni':
            rad = float(el1.ionic_radii[int(3.0)])
        elif el_1 == 'Ca':
            rad = float(el1.ionic_radii[int(list(comp.oxi_state_guesses())[0]['Ca'])])
            print(rad)

        else:
            os = os
            rad = float(el1.ionic_radii[int(os)])
        mcd = (os / rad)
            #mrox = rox
    else:
        os = 0
        mcd = 0
    rox = eddb.loc[eddb['element'] == el_1][eddb['OS'] == os]['ROx'].values[0]
    return mcd,  mx, rox, radii

# compounds = [ "SiO2", "Au"]
def transform(compounds):
    cdecs = []
    for comp in compounds:
        mcd, mx, rox, radii = ed(comp)
        #print(cdecs)
        cdecs.append([comp, mcd, mx, rox, radii])
    return  cdecs

data_list = transform(compds)
data_list.append(['CaHCO3', 2.193, 2.678333, 0, 1.8]) # the zero here should be modified
print(data_list)
db1 = pd.DataFrame(data_list, columns=['material', 'mcd', 'x', 'rox', 'radii'])

db1.to_csv('output/out_new.csv')

#print(transform(not_working))
