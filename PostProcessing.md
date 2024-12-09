FIrst get the consistency for your dataset in a json using test_confidence from experiments repo . this is consistency.json
then run experiments to get results. If multiple reruns concat the final csvs into one. Lets call it original.csv
now using consistency.json and original.csv use the not_consistent.py to get the augmented.json which also has unique_id and consistency in it.
you also get the filtered_1.json filtered_1_09.json, filtered_1_09_08.json filtered_1_09_08_07.json. these are subsets when you remove rows with confidence =1 , 09 ...etc
now you ave the anaylysis_reports.json with your resultsyou can also run on the augmented.csv the consistency_correlation.py to see how consistency correlates with the clssifier performance
and you can also run ther qualitative_analysis.py on the augmented.py to see which examples are the ones that work best at each classifier, average consistencies of them etc