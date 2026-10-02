<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1B33,100:2EC4B6&height=220&section=header&text=Deep%20Learning%20Complete&fontSize=42&fontColor=FFFFFF&animation=fadeIn&fontAlignY=38&desc=Neural%20Networks%20%7C%20CNNs%20%7C%20Real-World%20Applications&descAlignY=58&descSize=18" width="100%"/>

<br/>

<a href="https://github.com/mawiya-47">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=800&color=2EC4B6&center=true&vCenter=true&width=600&lines=Learning+Deep+Learning+one+model+at+a+time;CNNs+%7C+ANN+%7C+Computer+Vision;Built+with+TensorFlow+%26+Keras" alt="Typing SVG" />
</a>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

![GitHub last commit](https://img.shields.io/github/last-commit/mawiya-47/Deep-Learning-Complete?style=flat-square&color=2EC4B6)
![GitHub repo size](https://img.shields.io/github/repo-size/mawiya-47/Deep-Learning-Complete?style=flat-square&color=FF6B6B)
![GitHub stars](https://img.shields.io/github/stars/mawiya-47/Deep-Learning-Complete?style=flat-square&color=FFB703)

</div>

---

## 📖 About This Repository

This repository is a complete, hands-on journey through **Deep Learning** — from the basics of neural networks to building and training Convolutional Neural Networks (CNNs) on real datasets like **Fashion MNIST** and **CIFAR-100**.

It documents weekly progress, assignments, notes, and experiments as part of my Deep Learning coursework.

---

## 🗂️ Repository Structure

```
Deep-Learning-Complete/
│
├── Week 1 and 2/    
├── Week 3
├── Week 4
├── Week 5
├── Week 6
├── Week 7
├── Week 8
└── README.md
```

---

## 🚀 Topics Covered

<table>
<tr>
<td width="50%" valign="top">

### 🧠 Foundations
- Machine Learning vs Deep Learning
- Biological Neuron → Artificial Neuron
- Perceptron & Perceptron Trick
- Multi-Layer Perceptron (MLP)
- Forward & Backward Propagation

</td>
<td width="50%" valign="top">

### 🖼️ Computer Vision
- CNN Architecture Design
- Regularization (Dropout, BatchNorm)
- Fashion MNIST Classification
- CIFAR-100 Classification (100 classes)
- Confusion Matrix & Class-wise Accuracy

</td>
</tr>
</table>

---

## 🔥 Featured Project: CIFAR-100 CNN Classifier

A deeper Convolutional Neural Network built to classify images across **100 categories**, complete with:

- ✅ Data preprocessing & normalization
- ✅ Deep CNN with Batch Normalization + Dropout
- ✅ Data augmentation for better generalization
- ✅ Learning curve visualization
- ✅ Confusion matrix & per-class accuracy analysis

```python
model = models.Sequential([
    layers.Conv2D(64, (3,3), padding='same', activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2,2)),
    layers.Dropout(0.25),
    # ... deeper blocks
    layers.Dense(100, activation='softmax')
])
```

---

## 🛠️ Tech Stack

<div align="center">

| Category | Tools |
|---|---|
| **Language** | Python |
| **Deep Learning** | TensorFlow, Keras |
| **Data Handling** | NumPy, Pandas |
| **Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebook, Google Colab, VS Code |

</div>

---

## ⚡ Getting Started

```bash
# Clone the repository
git clone https://github.com/mawiya-47/Deep-Learning-Complete.git

# Navigate into the folder
cd Deep-Learning-Complete

# Install dependencies
pip install tensorflow numpy matplotlib seaborn scikit-learn ipywidgets

# Launch Jupyter Notebook
jupyter notebook
```

---

## 📊 Progress Tracker

- [x] Week 1 & 2 — Introduction to Deep Learning, Perceptron, MLP
- [x] Fashion MNIST Image Classification
- [x] CIFAR-100 CNN Classification
- [ ] Transfer Learning (Coming Soon)
- [ ] RNNs / LSTMs (Coming Soon)

---

<div align="center">

## 👤 Author

**Muhammad Mawiya**

[![GitHub](https://img.shields.io/badge/GitHub-mawiya--47-181717?style=for-the-badge&logo=github)](https://github.com/mawiya-47)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2EC4B6,100:0B1B33&height=120&section=footer" width="100%"/>

</div>
