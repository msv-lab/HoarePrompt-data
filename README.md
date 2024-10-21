
<table>
  <tr>
    <td style="width: 20%; text-align: center;">
      <img src="./assets/HoarePrompt_logo.png" alt="HoarePrompt Logo" width="100"/>
    </td>
    <td style="width: 80%; text-align: left;">
      <h1>HoarePrompt-data: Data generation and Results for HoarePrompt experiments</h1>
    </td>
  </tr>
</table>


## Introduction

This repository is designed to create data for running experiments with the HoarePrompt tool and to store the results of these experiments. HoarePrompt is a tool that assesses whether large language models can accurately understand and verify program correctness based solely on natural language descriptions of specifications.

## Repository Structure

This repository contains two key directories:

- **[PilotData](./PilotData)**: This folder contains scripts and instructions for generating pilot datasets using different LLMs (e.g., GPT-4, LLaMA3) for benchmarks such as APPS and MBPP. These datasets are used as input data to test the HoarePrompt tool.
  
- **Results**: This folder stores the results of previous experiments where the HoarePrompt tool was used to assess the correctness of the generated programs. Each result contains logs of the HoarePrompt experiment, including the program code, description, and postconditions generated by the tool.

### PilotData

The **[PilotData](./PilotData)** folder includes the tools necessary to generate datasets based on the APPS and MBPP benchmarks, using models such as GPT-4 and LLaMA. This data is used for assessing the ability of HoarePrompt to verify whether a program follows the provided specification. 

For detailed instructions on how to generate the datasets and test them, refer to the [PilotData README](./PilotData/README.md).

**Note**: The `APPS` dataset is not included in this repository due to its size but can be downloaded from [here](https://github.com/hendrycks/apps).

### Results

The **Results** folder contains the output of running HoarePrompt experiments, which include the postconditions and correctness checks performed by the tool based on the generated pilot datasets. We propose using this folder to store the logs of your own experimental runs when using the [HoarePrompt-experiments repository](https://github.com/msv-lab/HoarePrompt-experiments). 

We recommend setting the log directory to the **Results** folder during your experiment runs:
```bash
--log ../HoarePrompt-data/Results
```
This ensures that your logs and experiment outputs are organized and stored for future analysis.

Each experiment is stored in a subdirectory of the Results folder named by the datetime it was executed and contains log files, configuration files, versioning information potential failed_tasks files and CSVs with the tasks and the results of the experiment.

### Using HoarePrompt for Experiments

To run experiments with the HoarePrompt tool, you can clone and use the functionality from the [HoarePrompt-experiments repository](https://github.com/msv-lab/HoarePrompt-experiments). That repository contains the necessary code to assess if generated programs meet their respective specifications using the HoarePrompt tool. By linking it to the **Results** folder in this repository, you can manage both your data and experiment outcomes efficiently.

## Installation and Setup

Follow these steps to set up and start using the data and scripts in this repository:

1. Clone this repository:
   ```bash
   git clone https://github.com/msv-lab/HoarePrompt-data.git
   cd HoarePrompt-data
   ```
2. To generate datasets, follow the instructions in the **[PilotData README](./PilotData/README.md)** to generate new pilot data using LLMs and test them.

3. Use the `Results` folder to store the logs and outputs of your experiments, following the recommendations provided in the  **[PilotData README](./PilotData/README.md)** .
  
## Contributions
This is a joint project collaboration of Peking Univeristy and University College London.
Feel free to contribute to HoarePrompt-data by opening issues or submitting pull requests on GitHub. Your contributions are highly appreciated!

<table>
  <tr>
    <td style="text-align: center;">
      <img src="./assets/PKU.png" alt="Image 1" width="300"/>
    </td>
    <td style="text-align: center;">
      <img src="./assets/HoarePrompt_logo.png" alt="Image 2" width="300"/>
    </td>
    <td style="text-align: center;">
      <img src="./assets/UCL.png" alt="Image 3" width="300"/>
    </td>
  </tr>
</table>
