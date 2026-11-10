
import streamlit as st

st.set_page_config(
    page_title="Analyseur d'offres IA",
    page_icon="📊"
)

st.title("Analyseur d'appels d'offres IA")
st.write("Analyse financière des marchés publics")

st.subheader("Saisir les offres")

alpha = st.number_input("Entreprise Alpha (€)", value=120000)
beta = st.number_input("Entreprise Beta (€)", value=95000)
gamma = st.number_input("Entreprise Gamma (€)", value=78000)

if st.button("Analyser les offres"):
    offres = {
        "Entreprise Alpha": alpha,
        "Entreprise Beta": beta,
        "Entreprise Gamma": gamma
    }

    moyenne = sum(offres.values()) / len(offres)

    st.success(f"Prix moyen : {moyenne:,.2f} €")

    for entreprise, prix in sorted(
        offres.items(), key=lambda x: x[1]
    ):
        ecart = (prix - moyenne) / moyenne * 100
        st.write(f"{entreprise} : {prix:,} € ({ecart:+.1f} %)")

        if ecart < -20:
            st.warning(
                f"{entreprise} : écart important à examiner"
            )

st.caption(
    "Un écart de prix ne suffit pas à qualifier "
    "une offre d'anormalement basse. "
    "Une analyse et une procédure contradictoire "
    "sont nécessaires."
)
