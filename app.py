from flask import Flask, render_template
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Données d'exemple
    data = [5, 7, 2, 4, 9, 10, 1, 5]
    
    # Créer le graphique
    sns.set(style="whitegrid")
    plt.figure(figsize=(6,4))
    plt.plot(data, marker='o')
    plt.title("Exemple de graphique")
    
    # Sauvegarder l'image dans le dossier static
    graph_path = os.path.join('static', 'graph.png')
    plt.savefig(graph_path)
    plt.close()
    
    return render_template('index.html', graph_url=graph_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
