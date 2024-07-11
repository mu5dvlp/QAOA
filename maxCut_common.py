from qiskit import *
from qiskit.quantum_info import Operator
import numpy as np

# //＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
I = np.eye(2)
Z = np.array([[1,0],
              [0,-1]])

# //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
def get_Z_list(num):
    z_list = []
    # Z[i]を作成
    for i in range(num):
        # テンソル積を計算
        z_i = 1
        for j in range(num):
            if i==j: z_i=np.kron(z_i,Z)
            else: z_i=np.kron(z_i,I)
        z_list.append(z_i)
    return z_list

# //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
# コストハミルトニアン
def get_operator_costHamiltonian(num,edges,weights):
    z_list = get_Z_list(num)
    dim = 2**num
    matrix = np.zeros((dim,dim), dtype=complex)
    for k in range(len(edges)):
        i,j = edges[k]
        w = weights[k]
        matrix+=w*(np.eye(dim) - np.dot(z_list[i],z_list[j]))
    matrix*=-1/2
    return Operator(matrix)

# //ーーーーーーーーーーーーーーーーーーーーー
# コストハミルトニアンの回路
def get_operator_cost(num,edges,weights,gamma):
    qc = QuantumCircuit(num)
    for k in range(len(edges)):
        i,j = edges[k]
        w = weights[k]
        qc.cx(i, j)
        qc.rz(-2*gamma*w, j)
        qc.cx(i, j)
    return Operator(qc)

# //ーーーーーーーーーーーーーーーーーーーーー
# ミキサーハミルトニアンの回路
def get_operator_mixer(num,beta):
    qc = QuantumCircuit(num)
    for i in range(num):
        qc.rx(-2*beta, i)
    return Operator(qc)

# //ーーーーーーーーーーーーーーーーーーーーー
# メイン回路
def get_mainCircuit(num,edges,weights,args):
    qc_main = QuantumCircuit(num,num)
    qc_main.h(range(num))
    for i in range(len(args)//2):
        qc_main.append(get_operator_cost(num,edges,weights,args[i*2]),range(num))
        qc_main.append(get_operator_mixer(num,args[i*2+1]),range(num))
    return qc_main