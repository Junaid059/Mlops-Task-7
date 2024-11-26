import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data():
    df = pd.read_csv("data/raw_data.csv")
    df.dropna(inplace=True)

    # Normalize numerical fields
    scaler = MinMaxScaler()
    df[['temperature', 'humidity', 'wind_speed']] = scaler.fit_transform(
        df[['temperature', 'humidity', 'wind_speed']]
    )

    df.to_csv("data/processed_data.csv", index=False)
    print("Processed data saved to data/processed_data.csv")

if __name__ == "__main__":
    preprocess_data()
