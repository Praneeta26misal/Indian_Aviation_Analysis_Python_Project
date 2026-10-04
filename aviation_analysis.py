import pandas as pd
import matplotlib.pyplot as plt

# Load raw data
df = pd.read_csv("Air_full-Raw.csv")

# -----------------------------
# 1. DATA INSPECTION
# -----------------------------

print("Original shape:", df.shape)
print("Columns:", list(df.columns))

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


# -----------------------------
# 2. DATA CLEANING
# -----------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Convert validity dates to datetime
df["validFrom"] = pd.to_datetime(df["validFrom"], errors="coerce")
df["validTo"] = pd.to_datetime(df["validTo"], errors="coerce")

# Remove rows missing important flight information
df = df.dropna(
    subset=["airline", "flightNumber", "origin", "destination"]
)

# Convert scheduled times
df["scheduledDepartureTime"] = pd.to_datetime(
    df["scheduledDepartureTime"],
    errors="coerce"
)

df["scheduledArrivalTime"] = pd.to_datetime(
    df["scheduledArrivalTime"],
    errors="coerce"
)

# Remove rows where flight times could not be converted
df = df.dropna(
    subset=["scheduledDepartureTime", "scheduledArrivalTime"]
)

# Extract departure and arrival hours
df["departure_hour"] = df["scheduledDepartureTime"].dt.hour
df["arrival_hour"] = df["scheduledArrivalTime"].dt.hour

print("\nRows after cleaning:", len(df))


# -----------------------------
# 3. BASIC ANALYSIS
# -----------------------------

print("\nNumber of airlines:", df["airline"].nunique())
print("Number of origin airports:", df["origin"].nunique())
print("Number of destination airports:", df["destination"].nunique())


# -----------------------------
# 4. AIRLINE ANALYSIS
# -----------------------------

airline_summary = df.groupby("airline").agg(
    flights=("flightNumber", "count"),
    origins=("origin", "nunique"),
    destinations=("destination", "nunique")
).sort_values("flights", ascending=False)

print("\nAirline Summary:")
print(airline_summary)


# -----------------------------
# 5. AIRPORT ANALYSIS
# -----------------------------

top_origins = df["origin"].value_counts().head(10)
top_destinations = df["destination"].value_counts().head(10)

print("\nTop 10 Origin Airports:")
print(top_origins)

print("\nTop 10 Destination Airports:")
print(top_destinations)


# -----------------------------
# 6. ROUTE ANALYSIS
# -----------------------------

route_summary = (
    df.groupby(["origin", "destination"])
    .size()
    .sort_values(ascending=False)
    .head(20)
)

print("\nTop 20 Routes:")
print(route_summary)


# -----------------------------
# 7. SCHEDULING ANALYSIS
# -----------------------------

departure_summary = (
    df["departure_hour"]
    .value_counts()
    .sort_index()
)

print("\nFlights by Departure Hour:")
print(departure_summary)


# -----------------------------
# 8. SAVE CLEANED DATA
# -----------------------------

df.to_csv("Air_cleaned.csv", index=False)

airline_summary.to_csv("airline_summary.csv")
departure_summary.to_csv("departure_summary.csv")
route_summary.to_csv("top_routes.csv")

print("\nAnalysis files saved successfully.")


# -----------------------------
# 9. VISUALIZATIONS
# -----------------------------

# Top 10 airlines
plt.figure(figsize=(10, 6))

airline_summary["flights"].head(10).sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Airlines by Number of Flights")
plt.xlabel("Number of Flights")
plt.ylabel("Airline")
plt.tight_layout()
plt.savefig("top_airlines.png")
plt.close()


# Top 10 departure airports
plt.figure(figsize=(10, 6))

top_origins.sort_values().plot(kind="barh")

plt.title("Top 10 Departure Airports")
plt.xlabel("Number of Flights")
plt.ylabel("Airport")
plt.tight_layout()
plt.savefig("top_departure_airports.png")
plt.close()


# Flights by departure hour
plt.figure(figsize=(10, 6))

departure_summary.plot(
    kind="line",
    marker="o"
)

plt.title("Flights by Departure Hour")
plt.xlabel("Departure Hour")
plt.ylabel("Number of Flights")
plt.tight_layout()
plt.savefig("flights_by_departure_hour.png")
plt.close()


print("Visualizations saved successfully.")