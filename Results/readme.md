# Results Directory Overview

This README provides guidance on where to find the latest results for each **model/dataset combination** in the `results` folder. The results are categorized into two main types:

1. **HoarePrompt Results**: For comparing classifier performance across models and datasets.
2. **Confidence Results**: For evaluating the consistency of LLM responses for each dataset.

---

## Models and Datasets

- **Models**:
  - GPT-4omini
  - GPT-3.5
  - Qwen-7B-Instruct
  - Qwen-72B-Instruct
  - Meta-LLaMA/Llama-3.3-70B-Instruct

- **Datasets**:
  - Apps
  - MBPP
  - Code Contests

---

## Results Structure

### 1. HoarePrompt Results
- **Purpose**: Compare the performance of various classifiers (e.g., naive, simple tree, complex tree) for each model on each dataset.
- **Path Format**: Results/HoarePrompt_Results/<specific experiment>

-
### 2. Confidence Results
- **Purpose**: Measure the consistency of each model's responses to examples in the dataset.
- **Path Format**: Results/Confidence_Results/<specific experiment>

## **Current latest**:
### Confidence
- GPT-4o_mini on Apps: `Results/Confidence_Results/Pilot_confidence_simple_pilot9/apps_4_mini_1`
- GPT-4o_mini on Mbpp: `Results/Confidence_Results/Pilot_confidence_simple_pilot9/mbpp_4_mini_1`
- Qwen-7B-Instruct on Apps: `Results/Confidence_Results/Pilot_confidence_simple_pilot9/apps_qwne2point5`
- Qwen-7B-Instruct on Mbpp: `Results/Confidence_Results/Pilot_confidence_simple_pilot9/mbpp_qwen_2_point5`
- Llama-3.3-70B-Instruct on Apps: `Results/Confidence_Results/Pilot_confidence_simple_pilot9/apps_llama_1`
- Llama-3.3-70B-Instruct on Mbpp: `Results/Confidence_Results/Pilot_confidence_simple_pilot9/mbpp_llama_1`
- Qwen-72B-Instruct on Code Contests: `Results/Confidence_Results/Confidence_code_contests_1000_qwen7b`
- Qwen-7B-Instruct on Code Contests: `Results/Confidence_Results/Confidence_code_contests_1000_qwen72b`


### HoarePrompt Experiments
- GPT-4o_mini on Apps: `Results/HoarePrompt_Results/Pilot_new11/APPS_4mini_FINAL`
- GPT-4o_mini on Mbpp: `Results/HoarePrompt_Results/Pilot_new11/MBPP_4mini_FINAL`
- Qwen-7B-Instruct on Apps: `Results/HoarePrompt_Results/Pilot_new11/APPS_qwen_FINAL`
- Qwen-7B-Instruct on Mbpp: `Results/HoarePrompt_Results/Pilot_new11/MBPP_qwen_FINAL`
- Llama-3.3-70B-Instruct on Apps: `Results/HoarePrompt_Results/Pilot_new11/APPS_llama_FINAL`
- Llama-3.3-70B-Instruct on Mbpp: `Results/HoarePrompt_Results/Pilot_new11/MBPP_llama_FINAL`
- Qwen-72B-Instruct on Code Contests: `Results/HoarePrompt_Results/remote_qwen_code_contest`
- Qwen-7B-Instruct on Code Contests: `Results/HoarePrompt_Results/remote_qwen_code_contest`
---

