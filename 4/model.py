from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
model = BayesianNetwork([('A', 'C'), ('B', 'C'), ('C', 'D')])
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.3], [0.7]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.6], [0.4]])
cpd_c = TabularCPD(variable='C', variable_card=2,
                   values=[[0.8, 0.9, 0.4, 0.6],
                           [0.2, 0.1, 0.6, 0.4]],
                   evidence=['A', 'B'], evidence_card=[2, 2])
cpd_d = TabularCPD(variable='D', variable_card=2,
                   values=[[0.9, 0.6],
                           [0.1, 0.4]],
                   evidence=['C'], evidence_card=[2])
model.add_cpds(cpd_a, cpd_b, cpd_c, cpd_d)
print("Model is valid:", model.check_model())
print("CPD A:")
print(cpd_a)
print("CPD B:")
print(cpd_b)
print("CPD C:")
print(cpd_c)
print("CPD D:")
print(cpd_d)
infer = VariableElimination(model)
posterior_d = infer.query(variables=['D'], evidence={'A': 0, 'B': 1})
print("Posterior probability of D given evidence A=0, B=1:")
print(posterior_d)
