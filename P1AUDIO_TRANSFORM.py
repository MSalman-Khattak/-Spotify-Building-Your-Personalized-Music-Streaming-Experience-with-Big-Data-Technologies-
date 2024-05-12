# # import os
# # import numpy as np

# # from sklearn.preprocessing import StandardScaler
# # from sklearn.decomposition import PCA
# # from sklearn.manifold import TSNE
# # import matplotlib.pyplot as plt
# # import librosa
# # # Step 1: Loading Audio Files
# # def load_audio(audio_path, duration=30):
# #     audio, sr = librosa.load(audio_path, duration=duration, sr=None)
# #     return audio, sr

# # # Step 2: Feature Extraction
# # def extract_features(audio):
# #     mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)  # Mel-Frequency Cepstral Coefficients
# #     spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)[0]
# #     zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio)[0]
# #     return mfccs, spectral_centroid, zero_crossing_rate

# # # Step 3: Normalization or Standardization
# # def scale_features(features):
# #     scaler = StandardScaler()
# #     scaled_features = scaler.fit_transform(features)
# #     return scaled_features

# # # Step 4: Dimensionality Reduction
# # def apply_pca(features, n_components=2):
# #     pca = PCA(n_components=n_components)
# #     pca_features = pca.fit_transform(features)
# #     return pca_features

# # def apply_tsne(features, n_components=2):
# #     tsne = TSNE(n_components=n_components)
# #     tsne_features = tsne.fit_transform(features)
# #     return tsne_features

# # # Example usage
# # audio_path = "/home/khattak/Downloads/A3/project_BDA/songs"
# # audio, sr = load_audio(audio_path)
# # mfccs, spectral_centroid, zero_crossing_rate = extract_features(audio)
# # features = np.concatenate((mfccs.T, spectral_centroid.reshape(-1,1), zero_crossing_rate.reshape(-1,1)), axis=1)
# # scaled_features = scale_features(features)
# # pca_features = apply_pca(scaled_features)
# # tsne_features = apply_tsne(scaled_features)

# # # Visualization (for t-SNE)
# # plt.scatter(tsne_features[:,0], tsne_features[:,1], s=5)
# # plt.title('t-SNE Visualization of Audio Features')
# # plt.xlabel('t-SNE Component 1')
# # plt.ylabel('t-SNE Component 2')
# # plt.show()
# import os
# import numpy as np
# import librosa
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# from sklearn.manifold import TSNE

# # Step 1: Loading Audio Files
# def load_audio(audio_path, duration=30):
#     try:
#         audio, sr = librosa.load(audio_path, duration=duration, sr=None)
#         return audio, sr
#     except Exception as e:
#         print(f"Error loading {audio_path}: {e}")
#         return None, None

# # Step 2: Feature Extraction
# def extract_features(audio, sr):
#     mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)  # Mel-Frequency Cepstral Coefficients
#     spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)[0]
#     zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio)[0]
#     return mfccs.T, spectral_centroid, zero_crossing_rate

# # Step 3: Normalization or Standardization
# def scale_features(features):
#     scaler = StandardScaler()
#     scaled_features = scaler.fit_transform(features)
#     return scaled_features

# # Step 4: Dimensionality Reduction
# def apply_pca(features, n_components=2):
#     pca = PCA(n_components=n_components)
#     pca_features = pca.fit_transform(features)
#     return pca_features

# def apply_tsne(features, n_components=2):
#     tsne = TSNE(n_components=n_components)
#     tsne_features = tsne.fit_transform(features)
#     return tsne_features

# # Define the directory containing the songs
# songs_dir = "/home/khattak/Downloads/A3/project_BDA/songs/"

# # List all files in the directory
# song_files = os.listdir(songs_dir)

# # Initialize dictionary to store features for each audio file
# all_features = {}

# # Iterate over each file
# for i, song_file in enumerate(song_files, 1):
#     # Construct the full path to the audio file
#     audio_path = os.path.join(songs_dir, song_file)
    
#     # Load audio
#     audio, sr = load_audio(audio_path)
    
#     if audio is None or sr is None:
#         continue
    
#     # Extract features
#     mfccs, spectral_centroid, zero_crossing_rate = extract_features(audio, sr)
#     features = np.concatenate((mfccs, spectral_centroid.reshape(-1,1), zero_crossing_rate.reshape(-1,1)), axis=1)
    
#     # Scale features
#     scaled_features = scale_features(features)
    
#     # Apply PCA
#     pca_features = apply_pca(scaled_features)
    
#     # Apply t-SNE
#     tsne_features = apply_tsne(scaled_features)
    
#     # Store features in dictionary
#     all_features[song_file] = {
#         'mfccs': mfccs,
#         'spectral_centroid': spectral_centroid,
#         'zero_crossing_rate': zero_crossing_rate,
#         'scaled_features': scaled_features,
#         'pca_features': pca_features,
#         'tsne_features': tsne_features
#     }

#     print(f"Processed {i}/{len(song_files)} audios")

import os
import numpy as np
import pandas as pd
import librosa
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Step 1: Loading Audio Files
def load_audio(audio_path, duration=30):
    try:
        audio, sr = librosa.load(audio_path, duration=duration, sr=None)
        return audio, sr
    except Exception as e:
        print(f"Error loading {audio_path}: {e}")
        return None, None

# Step 2: Feature Extraction
def extract_features(audio, sr):
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)  # Mel-Frequency Cepstral Coefficients
    spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)[0]
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio)[0]
    return mfccs.T, spectral_centroid, zero_crossing_rate

# Step 3: Normalization or Standardization
def scale_features(features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features

# Step 4: Dimensionality Reduction
def apply_pca(features, n_components=2):
    pca = PCA(n_components=n_components)
    pca_features = pca.fit_transform(features)
    return pca_features

def apply_tsne(features, n_components=2):
    tsne = TSNE(n_components=n_components)
    tsne_features = tsne.fit_transform(features)
    return tsne_features

# Define the directory containing the songs
songs_dir = "/home/khattak/Downloads/A3/project_BDA/songs/"

# Path to store the CSV file
output_csv = 'audio_features.csv'

# Check if the CSV file already exists
if not os.path.exists(output_csv):
    # Create a new CSV file with headers
    pd.DataFrame(columns=['File_Name', 'MFCCs', 'Spectral_Centroid', 'Zero_Crossing_Rate', 'Scaled_Features', 'PCA_Features', 'tSNE_Features']).to_csv(output_csv, index=False)

# Iterate over each file
for i, song_file in enumerate(os.listdir(songs_dir), 1):
    # Construct the full path to the audio file
    audio_path = os.path.join(songs_dir, song_file)
    
    # Load audio
    audio, sr = load_audio(audio_path)
    
    if audio is None or sr is None:
        continue
    
    # Extract features
    mfccs, spectral_centroid, zero_crossing_rate = extract_features(audio, sr)
    features = np.concatenate((mfccs, spectral_centroid.reshape(-1,1), zero_crossing_rate.reshape(-1,1)), axis=1)
    
    # Scale features
    scaled_features = scale_features(features)
    
    # Apply PCA
    pca_features = apply_pca(scaled_features)
    
    # Apply t-SNE
    tsne_features = apply_tsne(scaled_features)
    
    # Append features to CSV file
    df = pd.DataFrame({
        'File_Name': [song_file],
        'MFCCs': [mfccs.tolist()],
        'Spectral_Centroid': [spectral_centroid.tolist()],
        'Zero_Crossing_Rate': [zero_crossing_rate.tolist()],
        'Scaled_Features': [scaled_features.tolist()],
        'PCA_Features': [pca_features.tolist()],
        'tSNE_Features': [tsne_features.tolist()]
    })
    
    # Append data to CSV file
    df.to_csv(output_csv, mode='a', header=not os.path.exists(output_csv), index=False)
    
    print(f"Processed {i}/{len(os.listdir(songs_dir))} audios")

print("Features saved to 'audio_features.csv'")
