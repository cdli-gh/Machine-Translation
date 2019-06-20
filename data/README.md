## Data Summary
Total 21,496 prallel phrases were provided by organizatation. [Link for Orginal Data](https://github.com/cdli-gh/mtaac_cdli_ur3_corpus/blob/master/ur3_corpus_data/translated_parallel_data/english_train).

Preprocessing the data, Steps:
1. Removing duplicate phrases
2. Removing empty lines in data files.
3. Removing missing data marked by "xxx" in data files.

After preprocessing total 10,147 phrases are extracted, these phrases are divided into test, train and develop files. Rejected phrases are stored (Missing translation and duplicate phrases) for further calculation in Data_Rejected folder
1. Training files contain 8,117 phrases (80%).
2. Testing files contain 1,015 phrases (10%).
3. Develop files contain 1,015 phrases (10%). Will work as validation files.


## Note for developers:
1. You may face Windows Latin Encoding errors with data, use Linux system for preprocessing.
2. Don't use '\n' for appending new lines with given data while writing data files into .txt files. Sumerian has data is not compatible with it, you will end with uneven parallel phrases. To handle this situation, use dataframe and write data into .csv files.
