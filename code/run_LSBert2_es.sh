export TSAR_LSBERT_PATH=/notebooks/FRONTIERS_TSAR2022/TSAR-LSBert/
export TSAR_LSBERT_CODE_PATH=$TSAR_LSBERT_PATH/code/
export RESULTS_PATH=$TSAR_LSBERT_CODE_PATH/results/es/


if [ ! -d $RESULTS_PATH ] 
then
    mkdir $RESULTS_PATH    
fi

DATASET_FILE=$TSAR_LSBERT_PATH/datasets/tsar2022_es_test_none.tsv
HUGGINGFACE_BERT_BASED_MODEL=dccuchile/bert-base-spanish-wwm-uncased
TOP_K_SUBSTITUTION_GENERATION=50
TOP_K_OUTPUT_RESULTS=3
PROBABILITY_MASKING_RATIO=0.5
WORD_EMBEDDINGS_FILE=$TSAR_LSBERT_CODE_PATH/resources/es/fasttext/cc.es.300.vec
WORD_FREQUENCY_FILE=$TSAR_LSBERT_CODE_PATH/resources/es/SUBTLEX-ESP/SUBTLEX-ESP_form_zipf.txt 


python3 LSBert2_es.py \
  --do_lower_case \
  --num_selections_SG $TOP_K_SUBSTITUTION_GENERATION \
  --num_selections_output $TOP_K_OUTPUT_RESULTS \
  --prob_mask $PROBABILITY_MASKING_RATIO \
  --eval_dir $DATASET_FILE \
  --bert_model $HUGGINGFACE_BERT_BASED_MODEL \
  --max_seq_length 350 \
  --word_embeddings $WORD_EMBEDDINGS_FILE  \
  --word_frequency $WORD_FREQUENCY_FILE \
  --output_SR_file $RESULTS_PATH/tsar_es_test_none_BETO_CC300d_SUBTLEX-ES_formzipf.out \
  #--do_eval
  #--nocuda

  

 
