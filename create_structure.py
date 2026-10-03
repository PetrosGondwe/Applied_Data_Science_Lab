import os

# Define the root repository name
REPO_NAME = "Applied_Data_Science_Lab"

# Define the structure: (Module Folder Name, Title for README, Description)
MODULES = [
    (
        "01_Housing_in_Latin_America",
        "Module 1: Housing in Latin America (Knowing Your Data)",
        "Exploratory Data Analysis (EDA), data cleaning, handling missing values, and visual data storytelling on real estate datasets across Mexico and Argentina.",
    ),
    (
        "02_Housing_in_Mexico_Prediction",
        "Module 2: Housing in Mexico (Predictive Modeling)",
        "Building predictive machine learning pipelines, feature engineering, and applying Ridge and Lasso regularization with bias-variance tradeoff optimization.",
    ),
    (
        "03_Air_Quality_in_Nairobi",
        "Module 3: Air Quality in Nairobi (Time Series)",
        "Time series analysis, resample processing, rolling statistics, and autoregressive forecasting models (AR/ARMA) for air pollution metrics.",
    ),
    (
        "04_Earthquake_Damage_in_Nepal",
        "Module 4: Earthquake Damage in Nepal (Classification)",
        "Supervised classification models (Logistic Regression, Decision Trees, Random Forests) to predict structural building damage following severe seismic activity.",
    ),
    (
        "05_Bankruptcy_in_Poland",
        "Module 5: Bankruptcy in Poland (Imbalanced Data & Ensembles)",
        "Handling highly imbalanced financial datasets using resampling techniques, cost-sensitive learning, and gradient boosted decision trees (XGBoost/LightGBM).",
    ),
    (
        "06_Customer_Segmentation_in_US",
        "Module 6: Customer Segmentation in the US (Unsupervised Learning)",
        "Unsupervised machine learning techniques including Principal Component Analysis (PCA) for dimensionality reduction and K-Means clustering for market segmentation.",
    ),
    (
        "07_A_B_Testing_in_E_commerce",
        "Module 7: A/B Testing in E-commerce (Statistical Inference)",
        "Designing, executing, and evaluating randomized A/B split tests using hypothesis testing, p-values, confidence intervals, and Chi-Square tests.",
    ),
    (
        "08_Data_Product_Deployment",
        "Module 8: Data Product Deployment (MLOps & API Packaging)",
        "Transitioning machine learning models into production applications by constructing RESTful APIs (FastAPI) and interactive dashboard user interfaces (Streamlit).",
    ),
]

MASTER_README = """# Applied Data Science Lab

A comprehensive, industry-grade data science repository showcasing end-to-end data pipelines, exploratory analytics, statistical modeling, machine learning, and model deployment across eight specialized domain projects.

Developed as part of the **WorldQuant University Applied Data Science Lab** program under **Chipu Data Labs**.

---

## 📂 Repository Structure & Modules

| Module | Project Focus | Core Techniques & Technologies |
| :--- | :--- | :--- |
| **01** | [Housing in Latin America](./01_Housing_in_Latin_America) | EDA, Data Wrangling, Plotly, Pandas |
| **02** | [Housing in Mexico Prediction](./02_Housing_in_Mexico_Prediction) | Linear Regression, Regularization (Ridge/Lasso), Scikit-Learn Pipelines |
| **03** | [Air Quality in Nairobi](./03_Air_Quality_in_Nairobi) | Time Series Analysis, AR/ARMA Models, Resampling |
| **04** | [Earthquake Damage in Nepal](./04_Earthquake_Damage_in_Nepal) | Classification, Decision Trees, Random Forests, Confusion Matrix |
| **05** | [Bankruptcy in Poland](./05_Bankruptcy_in_Poland) | Imbalanced Data, Resampling, XGBoost, Precision-Recall Metrics |
| **06** | [Customer Segmentation in US](./06_Customer_Segmentation_in_US) | Unsupervised Learning, PCA, K-Means Clustering |
| **07** | [A/B Testing in E-commerce](./07_A_B_Testing_in_E_commerce) | Statistical Inference, Hypothesis Testing, Z-test, Chi-Square |
| **08** | [Data Product Deployment](./08_Data_Product_Deployment) | FastAPI, Model Serialization, Docker, Streamlit Deployment |

---

## 🛠️ Environment & Tools

- **Language:** Python 3.10+
- **Environment:** Visual Studio Code / Jupyter Notebooks
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-Learn, XGBoost, Statsmodels
- **Version Control:** Git & GitHub
"""


def setup_portfolio():
    current_dir = os.getcwd()
    print(f"🚀 Initializing portfolio structure in: {current_dir}\n")

    # 1. Create Master README.md if it doesn't exist
    if not os.path.exists("README.md"):
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(MASTER_README)
        print("✅ Created master README.md")
    else:
        print("ℹ️ Master README.md already exists (skipped).")

    # 2. Iterate through each module to create directory structure
    for folder_name, title, description in MODULES:
        module_path = os.path.join(current_dir, folder_name)
        notebooks_path = os.path.join(module_path, "notebooks")
        data_path = os.path.join(module_path, "data")

        # Create directories
        os.makedirs(notebooks_path, exist_ok=True)
        os.makedirs(data_path, exist_ok=True)

        # Create module README.md
        readme_path = os.path.join(module_path, "README.md")
        if not os.path.exists(readme_path):
            module_readme = f"# {title}\n\n## Overview\n{description}\n\n## Key Learnings & Skills\n- TBD\n\n## Repository Content\n- `notebooks/`: Jupyter Notebooks documenting the workflow.\n- `data/`: Datasets or data loading scripts.\n"
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(module_readme)

        # Add a .gitkeep file inside data/ so Git tracks the empty folder
        gitkeep_path = os.path.join(data_path, ".gitkeep")
        if not os.path.exists(gitkeep_path):
            open(gitkeep_path, "w").close()

        print(f"📁 Set up: {folder_name}/")

    print(
        "\n🎉 Portfolio structure created successfully! Ready to add notebooks."
    )


if __name__ == "__main__":
    setup_portfolio()