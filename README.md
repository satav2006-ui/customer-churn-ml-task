# Task 3: Supervised Classification / Regression Modeling & Tuning

This notebook addresses the task requirements shown on the learning desk:
- at least 4 distinct model architectures
- GridSearchCV with stratified K-fold cross-validation
- Precision, Recall, F1, ROC-AUC and confusion matrix
- ROC-AUC curves
- validation-based champion model selection
- serialized champion model (`champion_model.joblib`)

The task page does not show an official dataset file. The notebook therefore reuses the public Titanic tabular dataset from OpenML, consistent with Task 2.

Run the notebook in Jupyter/Colab/VS Code with internet access. After execution, the notebook will generate `champion_model.joblib`.
