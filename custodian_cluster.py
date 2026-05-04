import random
import math

def kmeans_clustering_game():
    # 1. Dataset: (Spending Score 1-10, Visit Frequency 1-10)
    # In real ML, we don't know the labels; we find the patterns.
    customers = [
        {"id": "A", "spend": 2, "visit": 2}, # Low/Low
        {"id": "B", "spend": 3, "visit": 1}, # Low/Low
        {"id": "C", "spend": 8, "visit": 9}, # High/High
        {"id": "D", "spend": 9, "visit": 8}, # High/High
        {"id": "E", "spend": 1, "visit": 9}, # Low/High (Window Shoppers)
    ]

    print("--- 📍 THE CLUSTER CUSTODIAN 📍 ---")
    print("Mission: Group these 5 customers into 2 clusters using K-Means logic.")
    print("Goal: Minimize the distance between customers and their assigned 'Centroid'.")

    # 2. Initialize Centroids (User picks two starting points)
    print("\n--- STEP 1: INITIALIZE CENTROIDS ---")
    print("Pick two coordinates (x,y) to start your clusters (Values 1-10):")
    c1 = (int(input("Centroid 1 Spend: ")), int(input("Centroid 1 Visit: ")))
    c2 = (int(input("Centroid 2 Spend: ")), int(input("Centroid 2 Visit: ")))

    # 3. Assignment Phase (Distance Calculation)
    cluster_1, cluster_2 = [], []
    total_variance = 0

    print("\n--- STEP 2: ASSIGNMENT PHASE (Euclidean Distance) ---")
    for cust in customers:
        # Calculate distance to C1: sqrt((x2-x1)^2 + (y2-y1)^2)
        dist1 = math.sqrt((cust['spend'] - c1[0])**2 + (cust['visit'] - c1[1])**2)
        dist2 = math.sqrt((cust['spend'] - c2[0])**2 + (cust['visit'] - c2[1])**2)

        if dist1 < dist2:
            cluster_1.append(cust['id'])
            total_variance += dist1
            print(f"Customer {cust['id']} assigned to Cluster 1 (Dist: {dist1:.2f})")
        else:
            cluster_2.append(cust['id'])
            total_variance += dist2
            print(f"Customer {cust['id']} assigned to Cluster 2 (Dist: {dist2:.2f})")

    # 4. Evaluation (Within-Cluster Sum of Squares)
    print("\n--- 📊 CLUSTERING RESULTS ---")
    print(f"Cluster 1 members: {cluster_1}")
    print(f"Cluster 2 members: {cluster_2}")
    print(f"Total Model Variance (Error): {total_variance:.2f}")

    if total_variance < 10:
        print("🏆 DATA GURU: You found the natural groupings! Your marketing will be highly effective.")
    else:
        print("📋 NOISY DATA: Your clusters are too wide. Try picking centroids closer to the data points.")

if __name__ == "__main__":
    kmeans_clustering_game()
