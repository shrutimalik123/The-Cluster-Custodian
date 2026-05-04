# 📍 The Cluster Custodian - K-Means Clustering Sim

A hands-on simulation of Unsupervised Learning and Customer Segmentation. You play as a Marketing Director tasked with grouping a diverse customer base into distinct "Personas." By manually initializing centroids and calculating Euclidean distances, you will learn the mechanics behind how algorithms like K-Means organize unlabeled data into meaningful clusters.

This project focuses on teaching:
* **Unsupervised Learning Logic:** Discovering patterns in data without pre-defined labels or "ground truth."
* **Euclidean Distance:** Applying the Pythagorean theorem to measure similarity between multi-dimensional data points.
* **Centroid Initialization:** Understanding how the starting position of a model influences the final convergence and accuracy.
* **Variance & Inertia:** Evaluating model performance by measuring the "Within-Cluster Sum of Squares" (WCSS).

---

## ✨ Features

* **Manual Centroid Mapping:** Users input starting coordinates to simulate the "Initialization" phase of the K-Means algorithm.
* **Mathematical Inference:** The script automatically calculates distances to assign every customer to their mathematically "nearest" group.
* **Model Error Tracking:** Calculates a "Total Variance" score, demonstrating how "tight" or "loose" your identified clusters are.
* **Segmentation Analytics:** Categorizes behavioral data (Spending vs. Visit Frequency) into actionable marketing segments.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `cluster_custodian.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python cluster_custodian.py
    ```

### 3. Gameplay Instructions
1.  **Observe the Data:** Note the spending and visit habits of the 5 customers.
2.  **Initialize Centroids:** Pick two "centers" (x, y) that you think represent the middle of two different groups.
3.  **Audit the Assignments:** See which customers were pulled into which "gravity well."
4.  **Check Your Variance:** Aim for a **Total Variance below 10** to prove you found the most natural groupings.



---

## 🧠 Code Structure Highlights

### The Distance Engine
In K-Means, "similarity" is just a math problem. This code implements Euclidean distance, which treats the data points as coordinates on a grid to find the shortest path between them.

```python
# Calculating Euclidean Distance: sqrt((x2-x1)^2 + (y2-y1)^2)
dist1 = math.sqrt((cust['spend'] - c1[0])**2 + (cust['visit'] - c1[1])**2)

