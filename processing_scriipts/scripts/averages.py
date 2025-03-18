import json
import numpy as np

# Data
models = [
    {
        "hoareprompt": {
            "Agreement Count": 1064,
            "Balanced Accuracy": 0.5772944560780083,
            "True Positive Rate (TPR)": 0.7004357298474946,
            "False Negative Rate (FNR)": 0.2995642701525055,
            "False Positive Rate (FPR)": 0.5458468176914779,
            "MCC": 0.15946850198779786
        },
        "0 shot COT": {
            "Agreement Count": 1001,
            "Balanced Accuracy": 0.542647587621888,
            "True Positive Rate (TPR)": 0.5631808278867102,
            "False Negative Rate (FNR)": 0.43681917211328974,
            "False Positive Rate (FPR)": 0.4778856526429342,
            "MCC": 0.08536472028721556
        },
        "vanilla_no_cot": {
            "Agreement Count": 964,
            "Balanced Accuracy": 0.520892823148677,
            "True Positive Rate (TPR)": 0.19281045751633988,
            "False Negative Rate (FNR)": 0.8071895424836601,
            "False Positive Rate (FPR)": 0.15102481121898598,
            "MCC": 0.05538562019727005
        },
        "hoareprompt_no_unroll": {
            "Agreement Count": 1041,
            "Balanced Accuracy": 0.5582348922898582,
            "True Positive Rate (TPR)": 0.6663090128755365,
            "False Negative Rate (FNR)": 0.33369098712446355,
            "False Positive Rate (FPR)": 0.5498392282958199,
            "MCC": 0.11928802123261478
        },
        "tester": {
            "Agreement Count": 1002,
            "Balanced Accuracy": 0.5190661811493072,
            "True Positive Rate (TPR)": 0.05056759545923633,
            "False Negative Rate (FNR)": 0.9494324045407637,
            "False Positive Rate (FPR)": 0.012435233160621761,
            "MCC": 0.10909012757567073
        }
    },
    {
        "hoareprompt": {
            "Agreement Count": 1159,
            "Balanced Accuracy": 0.628934191702432,
            "True Positive Rate (TPR)": 0.6666666666666666,
            "False Negative Rate (FNR)": 0.3333333333333333,
            "False Positive Rate (FPR)": 0.40879828326180256,
            "MCC": 0.25853674090610174
        },
        "0 shot COT": {
            "Agreement Count": 1092,
            "Balanced Accuracy": 0.5934958775694601,
            "True Positive Rate (TPR)": 0.7138157894736842,
            "False Negative Rate (FNR)": 0.28618421052631576,
            "False Positive Rate (FPR)": 0.526824034334764,
            "MCC": 0.19254233102381157
        },
        "vanilla_no_cot": {
            "Agreement Count": 1069,
            "Balanced Accuracy": 0.5775920487915067,
            "True Positive Rate (TPR)": 0.3815789473684211,
            "False Negative Rate (FNR)": 0.618421052631579,
            "False Positive Rate (FPR)": 0.22639484978540772,
            "MCC": 0.1688088155482501
        },
        "hoareprompt_no_ unroll": {
            "Agreement Count": 1142,
            "Balanced Accuracy": 0.6152989550420758,
            "True Positive Rate (TPR)": 0.6178686759956943,
            "False Negative Rate (FNR)": 0.3821313240043057,
            "False Positive Rate (FPR)": 0.38727076591154264,
            "MCC": 0.23060112337651859
        },
        "tester": {
            "Agreement Count": 1008,
            "Balanced Accuracy": 0.522226211079617,
            "True Positive Rate (TPR)": 0.05170630816959669,
            "False Negative Rate (FNR)": 0.9482936918304034,
            "False Positive Rate (FPR)": 0.007253886010362694,
            "MCC": 0.13135126508938486
        }
    },
    {
    "hoareprompt": {
        "Agreement Count": 1120,
        "Balanced Accuracy": 0.6156128728072827,
        "True Positive Rate (TPR)": 0.5933701657458563,
        "False Negative Rate (FNR)": 0.4066298342541437,
        "False Positive Rate (FPR)": 0.36214442013129106,
        "MCC": 0.23146400050060179
    },
    "0 shot COT": {
        "Agreement Count": 1019,
        "Balanced Accuracy": 0.5595941583954931,
        "True Positive Rate (TPR)": 0.4375690607734807,
        "False Negative Rate (FNR)": 0.5624309392265193,
        "False Positive Rate (FPR)": 0.31838074398249455,
        "MCC": 0.12292196441880099
    },
    "vanilla_no_cot": {
        "Agreement Count": 1008,
        "Balanced Accuracy": 0.5525702092677443,
        "True Positive Rate (TPR)": 0.23314917127071824,
        "False Negative Rate (FNR)": 0.7668508287292818,
        "False Positive Rate (FPR)": 0.12800875273522977,
        "MCC": 0.1367386681103356
    },
    "Hoareprompt_no_unroll": {
            "Agreement Count": 1072,
            "Balanced Accuracy": 0.5794683178592466,
            "True Positive Rate (TPR)": 0.5712742980561555,
            "False Negative Rate (FNR)": 0.4287257019438445,
            "False Positive Rate (FPR)": 0.41233766233766234,
            "MCC": 0.15895744439044912
        
    },
    "tester": {
        "Agreement Count": 1001,
        "Balanced Accuracy": 0.5180592628715158,
        "True Positive Rate (TPR)": 0.05475206611570248,
        "False Negative Rate (FNR)": 0.9452479338842975,
        "False Positive Rate (FPR)": 0.018633540372670808,
        "MCC": 0.09603303521616013
    }

}
]

# Compute averages
averages = {}
for model in models:
    for classifier, metrics in model.items():
        if classifier not in averages:
            averages[classifier] = {metric: [] for metric in metrics}
        for metric, value in metrics.items():
            averages[classifier][metric].append(value)

# Take mean for each metric
for classifier in averages:
    for metric in averages[classifier]:
        averages[classifier][metric] = np.mean(averages[classifier][metric])

# Print results
print(json.dumps(averages, indent=4))
