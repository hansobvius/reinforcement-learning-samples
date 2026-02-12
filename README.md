# Q-Table Project

A reinforcement learning project focused on Q-learning algorithms and table-based approaches.

## Project Structure

```
reinforcement_learning/
├── src/              # Source code files
├── data/             # Training and test data
├── models/           # Saved models and Q-tables
├── notebooks/        # Jupyter notebooks for experiments
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Setup Instructions

### 1. Create Conda Environment

```bash
conda create -n q_table_project python=3.12 -y
```

### 2. Activate Environment

```bash
conda activate q_table_project
```

### 3. Install Dependencies

```bash
conda install numpy -y
```

Or using pip with requirements.txt:

```bash
pip install -r requirements.txt
```

## Usage

1. Activate the conda environment:
   ```bash
   conda activate q_table_project
   ```

2. Run your Python scripts from the `src/` directory:
   ```bash
   python src/your_script.py
   ```

3. For Jupyter notebooks:
   ```bash
   jupyter notebook
   ```

## Dependencies

- Python 3.12
- numpy 2.4.1

## Notes

- Add your Q-learning implementation files to the `src/` directory
- Save trained Q-tables and models to the `models/` directory
- Store datasets in the `data/` directory
- Use `notebooks/` for exploratory analysis and experiments
