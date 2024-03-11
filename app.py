import requests
import streamlit as st


# Fonction pour récupérer les données sur les pays depuis l'API
def get_data():
    try:
        response = requests.get("http://localhost:5000/api/pays")
        response.raise_for_status()  # Raise an error for non-2xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la récupération des données : {e}")
        return None
    except ValueError as e:
        st.error(f"Erreur lors de la lecture de la réponse JSON : {e}")
        return None


# Application Streamlit
def main():
    st.title("Visualisation des données sur les pays")

    # Bouton pour récupérer les données
    if st.button("Obtenir des données"):
        data = get_data()
        if data:
            st.write("Nom du pays :", data.get('nom', 'N/A'))
            st.write("Population :", data.get('population', 'N/A'))
            st.write("Capitale :", data.get('capitale', 'N/A'))


if __name__ == '__main__':
    main()
