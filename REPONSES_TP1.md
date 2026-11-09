# Réponses aux Questions de Réflexion - TP N° 1 : Git & Gestion du Code

**Module** : DevOps  
**Établissement** : Université Abderrahmane Mira – Béjaïa  
**Étudiant** : Rabah DJOUED  
**Dépôt GitHub** : https://github.com/Rabahdjd/TP_DevOps  

---

### Exercice 1.1 — Différence entre `git diff` et `git diff --staged`

* **`git diff`** : Affiche les différences entre le **répertoire de travail (Working Directory)** et la **zone de préparation (Staging Area / Index)**. Autrement dit, il montre toutes les modifications apportées aux fichiers suivis qui n'ont **pas encore** été ajoutées avec `git add`.
* **`git diff --staged`** (ou `git diff --cached`) : Affiche les différences entre la **zone de préparation (Staging Area)** et le **dernier commit (`HEAD`)**. Il permet d'inspecter précisément ce qui fera partie du prochain commit avant de lancer `git commit`.

---

### Exercice 1.2 — `git merge` vs `git rebase` & Analyse du graphe d'historique

* **Impact sur `git log --oneline --graph`** :
  * **`git merge`** : Crée un commit de fusion explicite avec deux parents. L'historique conserve l'arborescence exacte et montre la divergence puis la convergence des branches.
  * **`git rebase`** : Déplace la base de la branche de fonctionnalités au sommet de la branche cible en rejouant chaque commit un par un. Le graphe devient **strictement linéaire** (aucune branche divergente visible).
* **Quand utiliser l'un plutôt que l'autre ?** :
  * **Utiliser `git rebase`** : Sur ses branches locales de fonctionnalités avant de les intégrer, pour nettoyer l'historique et éviter les commits de fusion inutiles lors de mises à jour fréquentes avec `main`.
  * **Utiliser `git merge`** : Lors de l'intégration finale d'une fonctionnalité majeure dans une branche partagée (`main`, `develop`) ou via une Pull Request, afin de conserver la traçabilité historique et le contexte exact de l'intégration.
  * **Règle d'or** : Ne **jamais** faire de `rebase` sur une branche publique/partagée déjà poussée sur le dépôt distant.

---

### Exercice 1.3 — Pourquoi préférer une Pull Request (PR) au push direct sur `main` ?

En contexte d'équipe, passer par une Pull Request plutôt que de pousser directement sur `main` apporte plusieurs garanties fondamentales :
1. **Revue de code (Code Review)** : Permet aux pairs de relire, discuter, commenter et valider la qualité du code, la sécurité et la cohérence de l'architecture avant intégration.
2. **Automatisation CI/CD** : La PR déclenche automatiquement les tests unitaires, linters et builds (via GitHub Actions) pour vérifier qu'aucune régression n'est introduite sur `main`.
3. **Protection de la branche `main`** : Grâce aux règles de protection de branche (Branch Protection Rules), `main` reste toujours dans un état stable et déployable en production.
4. **Documentation et traçabilité** : Chaque PR documente la motivation du changement (tickets associés, discussions, captures d'écran, approbations).

---

### Exercice 1.4 — Dans quel cas `git reset --hard` est-il dangereux en environnement collaboratif ?

* `git reset --hard <hash>` supprime définitivement les commits postérieurs au commit cible et remet à zéro l'index et le répertoire de travail, avec **perte irréversible des modifications non commitées**.
* **Danger en environnement collaboratif** : Si les commits réinitialisés ont déjà été envoyés sur le dépôt distant (`git push`), l'historique local diverge de l'historique distant. Pour synchroniser, il faudrait forcer le push (`git push --force`), ce qui :
  * Écrase et réécrit l'historique partagé.
  * Casse le travail des collaborateurs qui se sont basés sur ces commits.
  * Peut causer des pertes de code massives et des conflits complexes.
* **Alternative recommandée** : Utiliser `git revert <hash>`, qui annule les modifications en créant un **nouveau commit** sans altérer l'historique partagé.

---

### Exercice 1.5 — Pourquoi le découpage en dossiers séparés (`etudiants/<nom-prenom>/`) réduit les conflits ?

* Git gère les conflits au niveau des **fichiers** et plus particulièrement des **lignes de texte**.
* Si chaque étudiant travaille exclusivement dans son propre sous-dossier (`etudiants/rabah/`), Git peut fusionner automatiquement et en toute sécurité les modifications de chacun sans jamais avoir de lignes en conflit sur un même fichier.
* Lors d'un `git pull` suivi d'un `git push`, les commits des différents étudiants sont de type "Fast-Forward" ou de simples merges automatiques sans conflit de contenu.
