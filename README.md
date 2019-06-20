# Translation for Sumerian and English
Project aims to build and train a neural network-based encode-decoder architecture for English-Sumerian and Sumerian-English Machine Translation in order to support experts in cuneiform studies with automated translations.

## Project Update 
Currently pipeline for Machine Translataion has been established using [OpenNMT](http://opennmt.net/) toolkit. Model is trained with 5000 and 10000 epoches.

## Installation
Clone the repository

All dependencies can be installed via:

```bash
pip install -r requirements.txt
```

Note that OpenNMT currently support PyTorch 1.0.0 only.

## Quickstart
Please refer to [Full Documentation](http://opennmt.net/OpenNMT-py/) of OpenNMT once before starting.


### Step 1: Preprocess the data

```bash
python preprocess.py -train_src data/src-train.txt -train_tgt data/tgt-train.txt -valid_src data/src-val.txt -valid_tgt data/tgt-val.txt -save_data data/demo
```


After running the preprocessing, the following files are generated:

* `demo.train.pt`: serialized PyTorch file containing training data
* `demo.valid.pt`: serialized PyTorch file containing validation data
* `demo.vocab.pt`: serialized PyTorch file containing vocabulary data


### Step 2: Train the model

```bash
python train.py -data data/demo -save_model demo-model
```

If you wants to train model using GPU please refer to [OpenNMT](http://opennmt.net/OpenNMT-py/) documentation.

Currently project is trained with 5000 and 10000 epoches. Due to file size limitation of Github, trained model files are uploaded on Google Drive, Download with below link for testing current developed model.
1. Model with [5000 Epoch](https://drive.google.com/file/d/1DX65_Z-T5gItVOsyCZCoyDgZtNhduTHF/view?usp=sharing)
2. Model with [10000 Epoch](https://drive.google.com/file/d/1CVVzcF1HkChQnC0E2nVHSe-nQyqZB8XE/view?usp=sharing)

### Step 3: Translate

```bash
python translate.py -model demo-model_step_XYZ.pt -src data/src-test.txt -output pred.txt -replace_unk -verbose
```

Now you have a model which you can use to predict on new data. We do this by running beam search. This will output predictions into `pred.txt`.

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/cdli-gh/Machine-Translation/blob/master/LICENSE.md) file for details.

