# Stratégie de test

Ce projet utilise une approche de test automatisé pour garantir la qualité et la fiabilité du code Python modernisé.

## Types de tests

- **Tests unitaires** : Chaque fonction et module est testé individuellement avec `pytest`.
- **Tests end-to-end (E2E)** : Les scénarios complets sont vérifiés, simulant le comportement réel de l’application.

## Organisation des tests

- Les tests sont placés dans le dossier `tests/`.
- Chaque module du dossier `src/` possède un fichier de test dédié dans `tests/`.

## Outils et configuration

- **pytest** : Framework principal pour l’exécution des tests.
- **pytest-cov** : Extension pour mesurer la couverture de code.
- **coverage.py** : Génère des rapports détaillés sur les lignes de code exécutées par les tests.
- Fichiers de configuration : `.pytest.ini` pour les options de test, `.coveragerc` pour la configuration de la couverture.

## Couverture de code

La couverture est mesurée à chaque exécution des tests :
- Le rapport indique les lignes non couvertes et ignore les fichiers completements couvert.
- L’objectif est d’identifier les parties du code non testées et d’améliorer la couverture globale.

## Automatisation CI/CD

- Les workflows GitHub Actions (voir `.github/workflows/python-package.yml`) exécutent automatiquement les tests et la couverture à chaque commit ou pull request.

## Exécution des tests

Pour lancer les tests et obtenir un rapport de couverture :

```bash
pytest
```

## Objectifs

- Garantir la fiabilité et la robustesse du code source.
- S’assurer que les fonctionnalités principales sont couvertes par des tests.
- Maintenir une couverture de code élevée et détecter rapidement les
- Prevenir les régressions

## Compatibilité descendante

La compatibilité descendante doit être respectée, même si cela implique de conserver certains bugs historiques pour garantir le bon fonctionnement des traitements existants.

### Bugs connus et intentionnels

- Les nombres négatifs ne sont pas pris en charge (comportement hérité du code COBOL d’origine).

| Test File                | Test Name                                             | Description                                                                                  |
|--------------------------|------------------------------------------------------|----------------------------------------------------------------------------------------------|
| test_data.py             | test_starting_money                                  | Test for starting money (initial balance is 1000).                                           |
| test_data.py             | test_read_write_money                                | Test for reading and writing money.                                                          |
| test_operations.py       | test_op_total_no_changes                             | Viewing total does not change the balance.                                                   |
| test_operations.py       | test_op_credit_adds_amount                           | Crediting adds the amount to the balance.                                                    |
| test_operations.py       | test_op_credit_invalid_amount                        | Crediting with invalid input raises ValueError.                                              |
| test_operations.py       | test_op_credit_large_numbers                         | Crediting with very large numbers.                                                           |
| test_operations.py       | test_op_debit_subtracts_amount                       | Debiting subtracts the amount from the balance.                                              |
| test_operations.py       | test_op_debit_insufficient_funds                     | Debiting with insufficient funds does not change the balance.                                |
| test_operations.py       | test_op_debit_invalid_amount                         | Debiting with invalid input raises ValueError.                                               |
| test_operations.py       | test_intentional_bug_op_credit_negative_treated_as_positive | Crediting negative amount treats it as positive (intentional bug for compatibility).         |
| test_operations.py       | test_intentional_bug_op_debit_negative_treated_as_positive  | Debiting negative amount treats it as positive (intentional bug for compatibility).          |
| test_main.py             | test_exit                                            | User can exit the program (option 4).                                                        |
| test_main.py             | test_continue                                        | User can continue with non-exit options and invalid inputs.                                  |
| test_main.py             | test_integration                                     | Integration test simulating a user session.                                                  |
| test_main.py             | test_integration_eof_quitting                        | Integration test simulating session ending with EOF (should quit).                           |
| test_main.py             | test_integration_eof_back_to_menu                    | Integration test with EOF after credit (should go back to menu, then quit).                  |
| test_main.py             | test_integration_invalid_credit_input                 | Integration test with invalid credit input.                                                  |
| test_main.py             | test_integration_invalid_debit_input                  | Integration test with invalid debit input.                                                   |
| test_main.py             | test_integration_invalid_menu_input                   | Integration test

## Conclusion

Cette stratégie de test vise à assurer la qualité du code modernisé tout en respectant les contraintes de compatibilité. L’automatisation et la couverture de code permettent de détecter rapidement les anomalies et de garantir la fiabilité du projet sur le long terme.