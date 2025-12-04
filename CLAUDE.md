# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an interactive learning project for Japanese Statistics Certification Level 2 (統計検定2級). It uses Marimo—a modern reactive notebook framework similar to Jupyter—combined with Python data science libraries to provide hands-on, exploratory learning of statistics concepts through real-world data examples.

**Key Goals:**
- Learn statistics using practical, real-world datasets (sales, web traffic, test scores, etc.)
- Understand **why** each statistical concept matters through concrete scenarios
- Build intuition through hands-on practice and visualization
- Master concepts at three levels: explanation → interactive exploration → independent practice

**Learning Approach:**
- **Theory + Examples**: Each lesson (`1.py`, `2.py`, etc.) presents theory with real-world examples
- **Interactive Exploration**: Adjust parameters and see live results (histogram, statistics update in real-time)
- **Independent Practice**: Separate exercise notebooks (`1_exercise.py`, etc.) with guided practice problems
- **Progressive Difficulty**: Start with guided hints → move to independent problem-solving

## Development Environment

### Running the Project

```bash
# Build the Docker image
docker-compose build

# Start the Marimo server
docker-compose up

# The server will be accessible at http://localhost:2718
```

After starting, Marimo opens in edit mode. You can access and edit notebooks through the web interface. Changes to `.py` notebook files are reflected immediately.

### Stopping the Environment

```bash
# Stop the running container
docker-compose down
```

### Development Workflow

The project uses Docker to ensure consistent environments across systems. The `Dockerfile` installs all dependencies and configures Marimo to run on port 2718 with authentication disabled (suitable for local development).

**Important**: Edits made in the Marimo web UI are automatically saved to the `.py` notebook files on disk. You can also edit these files directly in your editor and refresh Marimo to see changes.

## Project Architecture

### Notebook Structure

Notebooks in this project follow Marimo's reactive programming model:

- **`@app.cell` decorator**: Each function decorated with `@app.cell` represents a reactive cell. When dependencies change, only affected cells recompute.
- **Cell dependencies**: Cells depend on variables returned by other cells (via function parameters). Marimo automatically determines execution order.
- **Reactive UI**: Marimo's `mo.ui` components (sliders, buttons, etc.) trigger downstream cell recalculation when their values change.

Example pattern from `1.py`:
```python
@app.cell
def _(mo):
    # UI components return themselves; their values are accessed via `.value`
    mu_slider = mo.ui.slider(start=0, stop=100, step=1, value=50, label="平均 (Mean)")
    return mu_slider

@app.cell
def _(mu_slider, np):
    # This cell recalculates whenever mu_slider changes
    data = np.random.normal(loc=mu_slider.value, scale=10, size=100)
    return data
```

### File Organization

**Learning Notebooks (Main Content)**:
- **`1.py`**: 1-variable descriptive statistics (記述統計 - 1変数データ)
- **`2.py`**, **`3.py`**, etc.: Future lessons following the curriculum
- Each notebook covers: Theory → Real-world examples → Interactive exploration

**Exercise Notebooks (Practice)**:
- **`1_exercise.py`**: Practice problems for lesson 1
- **`2_exercise.py`**, etc.: Practice problems for future lessons
- Each exercise notebook contains 4 practice problems with:
  - Guided questions
  - Expandable hints
  - Sample answers with explanations

**Supporting Files**:
- **`__marimo__/session/`**: Marimo's internal session storage (auto-generated, safe to ignore)
- **`カリキュラム.md`**: Curriculum roadmap tracking progress across all 5 topic areas
- **`yaritaikoto.md`**: Project goals and motivation

### Current Content: Lesson 1 - 1-Variable Descriptive Statistics

**`1.py`** (Lesson): Real-world learning through scenarios

1. **Why Descriptive Statistics?** - Motivation through real data (100 numbers are meaningless; we need summaries)
2. **Example 1: EC Site Daily Sales** (90 days)
   - Central tendency measures (mean, median, mode)
   - Learning point: How external values (sales) affect mean vs. median
3. **Example 2: Web Traffic Analysis** (60 days)
   - Dispersion measures (variance, std dev, range, IQR)
   - Learning point: Understanding data stability with numbers
4. **Example 3: Student Test Scores** (50 students)
   - Data visualization (histograms, box plots)
   - Learning point: Reading distribution shapes from graphs
5. **Example 4: Comparing Multiple Datasets** (3 product categories)
   - Coefficient of variation (comparing across different scales)
   - Learning point: Relative stability analysis
6. **Example 5: Data Transformation** (Multiple subjects)
   - Standardization and percentile scores (偏差値)
   - Learning point: Comparing different measurement scales
7. **Interactive Lab** (Optional)
   - Adjust mean, std dev, sample size with sliders
   - Observe real-time changes to statistics and graphs

**`1_exercise.py`** (Practice): Hands-on problem-solving

**Problem 1**: Calculate basic statistics (coffee shop prices)
- Tasks: mean, median, std dev, range
- Scaffolding: Hints on NumPy/Pandas syntax

**Problem 2**: Create graphs (online shop order counts)
- Tasks: Draw histogram and box plot
- Scaffolding: Code skeleton showing subplot structure

**Problem 3**: Detect outliers (server response times)
- Tasks: Identify outliers using IQR method
- Scaffolding: Formula for outlier bounds provided

**Problem 4**: Real-world analysis (social media engagement)
- Tasks: Compare 3 post types using statistics
- Scaffolding: Minimal guidance; focuses on interpretation
- Complexity: Most realistic scenario—analysis → conclusion

## Working with Marimo Notebooks

### Cell Structure and Dependencies

Cells are executed based on their dependencies, not file order. A cell runs when:
1. The app initializes
2. Any of its upstream dependencies change

Keep this in mind when adding new cells—ensure they depend on the correct upstream cells by including them as function parameters.

### Interactive Components

Marimo provides UI components through `mo.ui.*`:
- Sliders: `mo.ui.slider(start=0, stop=100, step=1, value=50, label="...")`
- Buttons, text inputs, dropdowns, etc.

Components return themselves; access their current value via `.value`. When the user interacts with a component, all dependent cells automatically recompute.

### Data Flow Patterns

The `1.py` notebook follows this pattern:
1. **Input cells** define interactive controls (sliders)
2. **Processing cells** use those values to generate/transform data
3. **Display cells** visualize results or show computed statistics

Cells use markdown (`mo.md()`) to intersperse documentation with code.

### Visualization

Matplotlib and Seaborn integrate smoothly with Marimo:
```python
@app.cell
def _(plt, data):
    fig, ax = plt.subplots()
    ax.plot(data)
    fig  # Return the figure; Marimo displays it
    return
```

Return the figure object at the end of the cell for display.

## Dependencies

All dependencies are listed in `Dockerfile` and automatically installed when building:

- **marimo** (0.18.1+): Reactive notebook framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scipy**: Scientific computing functions
- **matplotlib**: Low-level plotting library
- **seaborn**: Statistical data visualization (built on matplotlib)
- **statsmodels**: Statistical modeling and testing (for future chapters)

No `requirements.txt` exists; pin versions in the `Dockerfile` if reproducibility is critical.

## Learning Workflow

### How to Use These Notebooks

**For Learning a New Topic**:
1. Open the main lesson notebook (e.g., `1.py`)
2. Read through the real-world examples and explanations
3. Observe how statistical concepts apply to concrete scenarios
4. Use the interactive lab section to adjust parameters and develop intuition

**For Practice**:
1. Open the corresponding exercise notebook (e.g., `1_exercise.py`)
2. Read each problem carefully
3. **First attempt**: Write your own solution without hints
4. **If stuck**: Click "ヒントを表示" (Show Hint) for guidance
5. **After attempting**: Click "解答例を見る" (Show Answer) to compare and learn

**Progressive Scaffolding in Exercises**:
- **Problem 1**: Basic computation with detailed hints
- **Problem 2**: Graph creation with code skeleton
- **Problem 3**: Data analysis with formula hints
- **Problem 4**: Real-world scenario with minimal guidance

This progression builds confidence and independence.

## Learning Curriculum Reference

See `カリキュラム.md` for the complete learning roadmap. It uses checkboxes to track progress across five major topic areas:

1. **記述統計** (Descriptive Statistics) - 1-variable and 2-variable data
2. **確率と確率分布** (Probability & Distributions)
3. **推測統計** (Inferential Statistics) - Estimation and hypothesis testing
4. **線形モデル** (Linear Models) - Regression and ANOVA
5. **データ収集と活用** (Data Collection Methods)

### Notebook Structure for Future Lessons

When creating lesson 2, 3, etc., follow this pattern:

**`N.py` (Main Lesson)**:
- Introduction: Why this topic matters (concrete problem/scenario)
- Multiple real-world examples (3-5 different datasets)
- Key learning points highlighted with 💡 emojis
- Interactive lab section with sliders/controls
- Progress naturally from "why?" → "how?" → "observe"

**`N_exercise.py` (Practice)**:
- 4 progressive practice problems
- Problem 1-2: Guided with detailed hints
- Problem 3: Moderate guidance
- Problem 4: Real-world scenario with minimal hints (interpretation-focused)
- All problems include expandable hints and sample answers
