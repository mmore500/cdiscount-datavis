import json
import matplotlib.pyplot as plt
import os

dat = json.load(open("data/training-accuracy.json"))

training_accuracies = [d['training-accuracy'] for d in dat]
training_losses = [d['training-loss'] for d in dat]
iterations = [d['iteration'] for d in dat]

plt.plot(iterations, training_accuracies)
plt.ylabel("Training Set Accuracy")
plt.xlabel("Minibatch Iteration")

if not os.path.exists('out'):
    os.makedirs('out')
plt.savefig('out/accuracy.pdf', format='pdf')
plt.clf()

plt.plot(iterations, training_losses)
plt.ylabel("Training Set Loss")
plt.xlabel("Minibatch Iteration")

if not os.path.exists('out'):
    os.makedirs('out')
plt.savefig('out/loss.pdf', format='pdf')
