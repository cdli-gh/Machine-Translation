# Translation for Sumerian and English
The project aims to build and train a neural network-based encode-decoder architecture for English-Sumerian and Sumerian-English Machine Translation to support experts in cuneiform studies with automated translations. For more details, please check our published [paper](https://www.aclweb.org/anthology/2020.coling-main.308/).

## Project Update
The project carries out English<-->Sumerian Translation using parallel corpora. Presently we have only about 50K sentences for both languages as the parallel corpora. In contrast, around 1.47M sentences in the Sumerian monolingual corpus are also available.
Please check out our current work, where we improve the NMT system by combining it with techniques like Back Translation, Transfer Learning, and Dual Learning that leverages the monolingual data.

[**Semi-Supervised NMT for Sumerian<-->English**](https://github.com/cdli-gh/Semi-Supervised-NMT-for-Sumerian-English)

## Installation
Clone the repository. (We are assuming you have python version 3.6.x and pip is installed on your linux system)

(Optional)If not, please use the below command, this will create a new environment using conda.
```bash
conda create -n cdli python=3.6
conda activate cdli
```

All dependencies can be installed via:

```bash
pip install -r requirements.txt
```
NOTE: If you have MemoryError in the install try to use:

```bash
pip install -r requirements.txt --no-cache-dir
```

Note that Project currently support PyTorch >= 1.1 (should be work with 1.0)

By this point, your system should be ready with all dependencies. Please use below command to check PyTorch verion.
```bash
python -c "import torch; print(torch.__version__)"
```
Output should be your PyTorch version >= 1.1.0

If you still face any issues while installing dependencies for the project, feel free to ping us at our [Communication channel](https://cdli-gsoc.slack.com/).

## Quickstart
Please refer to [Full Documentation](http://opennmt.net/OpenNMT-py/) of OpenNMT once before starting.

### Translation Results

Translation results are available in translation_results folder for all Neural Network Architecture. For more details about Neural Network architecture and details, feel free to contact us on CDLI [Communication Channel](https://cdli-gsoc.slack.com/).


### Translating new Data

Please use the below command to translate new Sumerian phrase to English phrase. We are assuming you have a text file placed in data folder as **sumerian_test.txt**.

```bash
python3 translate.py -model trained_models/baseline_model.pt -src data/sumerian_test.txt -output pred.txt -replace_unk -verbose
```

Now you have a model which you can use to predict on new data. We do this by running beam search. This will output predictions into `pred.txt`.

### Results
The best results obtained are shown in the second column of table below.

| Model Architecture     | BLEU  |
| ---------------------- | ----- |
| Base Translator        | 19.6  |
| Extended Translatator  | 21.6  |
| Transformer Translator | 20.9  |


## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/cdli-gh/Machine-Translation/blob/master/LICENSE.md) file for details.

## Citation

```bibtex
@inproceedings{punia-etal-2020-towards,
    title = "Towards the First Machine Translation System for {S}umerian Transliterations",
    author = "Punia, Ravneet  and
      Schenk, Niko  and
      Chiarcos, Christian  and
      Pag{\'e}-Perron, {\'E}milie",
    booktitle = "Proceedings of the 28th International Conference on Computational Linguistics",
    month = dec,
    year = "2020",
    address = "Barcelona, Spain (Online)",
    publisher = "International Committee on Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.coling-main.308",
    pages = "3454--3460",
    abstract = "The Sumerian cuneiform script was invented more than 5,000 years ago and represents one of the oldest in history. We present the first attempt to translate Sumerian texts into English automatically. We publicly release high-quality corpora for standardized training and evaluation and report results on experiments with supervised, phrase-based, and transfer learning techniques for machine translation. Quantitative and qualitative evaluations indicate the usefulness of the translations. Our proposed methodology provides a broader audience of researchers with novel access to the data, accelerates the costly and time-consuming manual translation process, and helps them better explore the relationships between Sumerian cuneiform and Mesopotamian culture.",
}
```
