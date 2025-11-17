# gitp_llm_project

Jupyter notebooks that analyze interview transcripts using LLMs.

## 1. 🛠 Installation

### 1.1 Install VS Code. 
VS code is an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) that you can use to run jupyter notebooks conveniently.

### 1.2 Install miniconda (Recommended).
Install the miniconda package manager based on your operating system: [mini conda installation](https://www.anaconda.com/download?utm_source=anacondadocs&utm_medium=documentation&utm_campaign=download&utm_content=installwindows)

### 1.3 Install Git
If you do not have Git installed, follow [these instructions](https://coderefinery.github.io/installation/git-in-terminal/) on CodeRefinery to download, install and configure Git.

### 1.4 Data Access
If you wish to run the script specifically for the data it was designed for please use this [link](https://gitp.sharepoint.com/:f:/s/ResearchTilburgUniversity/Eli8ke6D45VGpt7eFtv_JB0B9aVpJfFRhFtWdJwcZr044Q?email=I.Winkes%40gitp.nl&e=IadhPb). Note that only authorized personnel can access it.



## 2. 🚀 Usage: 

**Decide a place/location in your PC where you would like to store this project.** Make sure this is an easily accessible destination as you will need to use it again. Next, inside this folder, open the git terminal by right clicking and select `Open Git Bash Here` and paste the following lines of code one by one.

1. Clone the Repository
```bash
git clone https://github.com/ShekharNarayanan/gitp_llm_project.git
```
After this step, you will see a folder called `gitp_llm_project` in your file explorer with all the relevant code inside this folder.

**Note: If you receive an *authentication error*, it likely means you are a new user to Gitlab used for the university. You will have to set an Personal Access Token. Please leave the git terminal open and scroll to the bottom of this tutorial to see how you can set one.**

### 2. Create a Conda Environment and Install the requirements 
 
 Next, open the miniconda terminal by typing **"Anaconda"**  in the windows search bar navigate to the `gitp_llm_project` folder you cloned in step 1. Then, we can create a conda environment. This step will use the `environment.yml` file and also install all the dependences with the channels meant to install them properly. This can be done using the code segments below. 

``` bash
cd path/to/your/project/folder
```

**The step below only has to be done once!**

``` bash
conda env create -f environment.yml
```

### 3. 🛣 Navigating VS Code.

Next we will open VS Code. Once you are at the start page, click on **File** and then click **Open folder**. Click on the  **gitp_llm_project** folder you cloned in your chosen destination. 


#### 3.1 Choosing the environment 

In the **Explorer** tab, click on the **GITP_LLM_Jupyter_nl.ipynb** file. You should see a jupyter notebook open up. On the top right, there will be a **Select kernel** option.


Once you click on it, click on **Python environments**. Then you will see a list of environments that you have on your PC. Our environment is named after our project, so select the Python environment called **gitp_llm_project**. After you do this, the kernel option would be set as the environment.  If VS Code prompts you to install any other plugins at this point, simply click on **install** then and wait till all installations are finished.

Congrats! You can now run your code. Make sure to have your own data in the input and output folders.


## 6. 🔗 Contact

In case of questions, please shoot an email to A.Koutsoumpis@tilburguniversity.edu
