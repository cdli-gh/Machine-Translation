# Translation for Sumerian and English
Project aims to build and train a neural network-based encode-decoder architecture for English-Sumerian and Sumerian-English Machine Translation in order to support experts in cuneiform studies with automated translations.

## Project Update
Project is completed with implementing 3 different Neural Network architecture for Machine Translation task.

## Installation
Clone the repository

All dependencies can be installed via:

```bash
pip install -r requirements.txt
```

Note that OpenNMT currently support PyTorch 1.0.1 only.

## Quickstart
Please refer to [Full Documentation](http://opennmt.net/OpenNMT-py/) of OpenNMT once before starting.

### Translation Results

Translation results are available in translation_results folder for all Neural Network Archicture.

### Translating new Data

Please use the below command to translate new Sumerian phrase to English phrase.

```bash
python translate.py -model trained_model/baseline_model.pt -src data/sumerian_test.txt -output pred.txt -replace_unk -verbose
```

Now you have a model which you can use to predict on new data. We do this by running beam search. This will output predictions into `pred.txt`.

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/cdli-gh/Machine-Translation/blob/master/LICENSE.md) file for details.
