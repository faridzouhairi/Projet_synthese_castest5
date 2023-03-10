Feature: Voir dans le navigateur

  Scenario: Permettre a l'utilisateur de voir un fichier dans le navigateur Web
    Given Je suis connecté a l'application avec un compte utilisateur
    And   Je clique sur le lien 'Fichiers partagés'
    And   Je clique sur le fichier "FichierTest 11.jpg"
    And   Je clique sur 'Voir dans le navigateur'
    Then  je vais etre rederige vers une page du navigateur et Verifier le contenu
    Then  Je dois me deconnecter et fermer tous les navigateurs
