import data
from data import procedure_data
prod = procedure_data(path_data = "DSHS.xlsx")
x = prod.get_out(100,100,200,200)
print(x)
print(prod.data)