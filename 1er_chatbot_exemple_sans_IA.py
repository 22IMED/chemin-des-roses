# Chatbot simple pour l'autodiagnostic du cancer du sein

def poser_questions():
    questions = [
        "Avez-vous remarqué une bosse ou un nodule dans votre sein ? (oui/non) ",
        "Ressentez-vous des douleurs dans votre sein ? (oui/non) ",
        "Avez-vous des changements dans la forme ou la taille de votre sein ? (oui/non) ",
        "Y a-t-il un écoulement du mamelon ? (oui/non) ",
        "Avez-vous des rougeurs ou des changements de texture de la peau ? (oui/non) ",
        "Avez-vous des ganglions lymphatiques enflés sous le bras ? (oui/non) ",
        "Avez-vous des antécédents familiaux de cancer du sein ? (oui/non) "
    ]

    réponses_positives = 0

    for question in questions:
        while True:  # Boucle pour demander à l'utilisateur de répondre jusqu'à ce qu'une réponse valide soit donnée
            réponse = input(question).strip().lower()
            # Normalisation des réponses
            if "oui" in réponse:
                réponses_positives += 1
                break
            elif "non" in réponse:
                break
            elif "je crois" in réponse or "il me semble" in réponse or "peut-être" in réponse or "je pense" in réponse:
                réponses_positives += 1  # Considérer comme positif
                break
            elif "je ne crois pas" in réponse or "il me semble que non" in réponse or "pas vraiment" in réponse or "je ne pense pas" in réponse:
                break
            else:
                print("Réponse non reconnue. Veuillez répondre par oui ou non.")

    return réponses_positives

def évaluer_consultation(réponses_positives, total_questions):
    seuil = total_questions / 2  # 50% des réponses positives
    return réponses_positives > seuil

def proposer_médecin(departement):
    # Liste fictive de médecins par département
    médecins = {
        "75": "Dr. Martin Dupont, Oncologue à Paris",
        "69": "Dr. Sophie Leblanc, Oncologue à Lyon",
        "13": "Dr. Julien Mercier, Oncologue à Marseille",
        "31": "Dr. Claire Boucher, Oncologue à Toulouse",
        "33": "Dr. Pierre Renault, Oncologue à Bordeaux"
    }
    
    return médecins.get(departement, "Aucun spécialiste trouvé dans votre département.")

def main():
    print("Bienvenue dans le chatbot d'autodiagnostic du cancer du sein.")
    total_questions = 7
    réponses_positives = poser_questions()
    
    if évaluer_consultation(réponses_positives, total_questions):
        print("Il est recommandé de consulter un médecin.")
        département = input("Veuillez entrer votre département (numéro, ex: 75 pour Paris) : ").strip()
        médecin = proposer_médecin(département)
        print(f"Recommandation : {médecin}")
    else:
        print("Aucune inquiétude majeure signalée. Cependant, si vous ressentez des symptômes persistants, n'hésitez pas à consulter.")

if __name__ == "__main__":
    main()
