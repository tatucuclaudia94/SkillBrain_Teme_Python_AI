import numpy as np


# Normalizeaza un array cu 5 coloane folosind broadcasting

data = np.random.rand(10, 5)

media = np.mean(data, axis=0)

deviatia = np.std(data, axis=0)

normalizat = (data - media) / deviatia

print("Array normalizat:")
print(normalizat)



# Rezolva un sistem de 3 ecuatii liniare

A = np.array([
    [2, -1, 3],
    [1, 0, -2],
    [3, 1, 1]
])

b = np.array([9, -4, 10])

solutie = np.linalg.solve(A, b)

print("Solutia sistemului:")
print(solutie)



# Model simplu de neuron cu activare ReLU

def relu(x):
    return np.maximum(0, x)

inputuri = np.array([1.0, -2.0, 3.0])

greutati = np.array([0.5, 0.2, -0.3])

bias = 0.1

output = relu(np.dot(inputuri, greutati) + bias)

print("Output neuron ReLU:", output)



# Functie sigmoid aplicata pe dataset

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

dataset = np.random.randn(100)

rezultat_sigmoid = sigmoid(dataset)

print("Sigmoid aplicat pe dataset:")
print(rezultat_sigmoid)



# Simulare retea cu 2 straturi complet vectorizata

X = np.random.randn(5, 3)

W1 = np.random.randn(3, 4)

b1 = np.random.randn(4)

W2 = np.random.randn(4, 2)

b2 = np.random.randn(2)

layer1 = relu(np.dot(X, W1) + b1)

output_final = sigmoid(np.dot(layer1, W2) + b2)

print("Output retea neuronala:")
print(output_final)

