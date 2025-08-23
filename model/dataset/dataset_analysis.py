import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_dataset_relationships(filename="dataset_scores.json"):
    """Procesa dataset plano y genera gráficos de relación input vs heurística."""
    
    # Cargar dataset
    with open(filename, "r") as f:
        dataset = json.load(f)
    
    all_rows = []
    for entry in dataset:
        # Features ya están preprocesadas
        features = entry["input"]
        for h_name, score in entry["output"].items():
            row = features.copy()
            row["heuristic"] = h_name
            row["score"] = score
            all_rows.append(row)
    
    df = pd.DataFrame(all_rows)
    
    # Obtener todas las columnas de features (excluyendo heurística y score)
    feature_names = [col for col in df.columns if col not in ["heuristic", "score"]]
    
    # Graficar cada feature contra score
    for feature in feature_names:
      plt.figure(figsize=(12, 6))
      for h_name in df["heuristic"].unique():
          subset = df[df["heuristic"] == h_name]
          # Agrupar por valor de la feature y calcular promedio
          avg_scores = subset.groupby(feature)["score"].mean()
          plt.plot(avg_scores.index, avg_scores.values, marker='o', label=h_name)
      plt.xlabel(feature)
      plt.ylabel("Score promedio")
      plt.title(f"Promedio de score vs {feature} por heurística")
      plt.legend()
      plt.grid(True)
      plt.show()
