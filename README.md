# Getting started

To download BERT, use the following command:

`git clone https://github.com/google-research/bert.git`

Download the following model:

https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip

To get the original SQuAD dataset, download these three files into a folder:

https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json
https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json
https://github.com/allenai/bi-att-flow/blob/master/squad/evaluate-v1.1.py

Run these commands:

```bash
$ export SQUAD_DIR=/Users/path/to/your/SQuAD/folder
$ export BERT_BASE_DIR=/Users/path/to/your/uncased_L-12
```

You can run BERT on the pre-trained SQuAD with this command:

```bash
$ python run_squad.py \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --do_train=True \
  --train_file=$SQUAD_DIR/train-v1.1.json \
  --do_predict=True \
  --predict_file=$SQUAD_DIR/dev-v1.1.json \
  --train_batch_size=12 \
  --learning_rate=3e-5 \
  --num_train_epochs=2.0 \
  --max_seq_length=384 \
  --doc_stride=128 \
  --output_dir=/tmp/squad_base/
  ```








