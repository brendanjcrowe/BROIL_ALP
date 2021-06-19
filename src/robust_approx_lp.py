import numpy as np
import gurobipy as gp
from gurobipy import GRB
from csv_loader import load_marek_csv

p, r, state_space, action_space = load_marek_csv('marek_test_mdp.csv')

print(p.shape, r.shape, state_space.shape, action_space.shape)