import pandas as pd
from pymongo import MongoClient
import torch
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['MYDB']
collection = db['MTDATA']

# Retrieve data from MongoDB
df = pd.DataFrame(list(collection.find()))

# Separate features and labels
X = df[['MFCCs', 'Spectral_Centroid', 'Zero_Crossing_Rate', 'Scaled_Features', 'PCA_Features', 'tSNE_Features']].values
y = df['genre_id'].values

# Perform feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert numpy arrays to PyTorch tensors
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.long)

# Create PyTorch DataLoader
dataset = TensorDataset(X_tensor, y_tensor)
data_loader = DataLoader(dataset, batch_size=64, shuffle=True)

# Example usage of data_loader
for batch_X, batch_y in data_loader:
    # Print batch data
    print("Batch Features:")
    print(batch_X)
    print("Batch Labels:")
    print(batch_y)
    break  # break after printing the first batch

