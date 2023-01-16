# TSAR-LSBert for English, Spanish and Portuguese 

The TSAR-LSBert code is an adaptation of the LSBert (Qiang et al. 2020b) Lexical Simplifier for English.
This adaptation was used for the evaluation of Lexical Simplification baselines for English, Spanish and Portuguese at the Štajner et al. 2022 paper (see [references section]()) and it also has been used  at the [TSAR-2022 Shared Task in Multilingual Lexical Simplification](https://github.com/LaSTUS-TALN-UPF/TSAR-2022-Shared-Task) as a baseline for Lexical Simplification (Saggion et al. 2022). 

Complex word identification is not used in this version.

The TSAR-LSBert code adaptation for English uses the same LSBert algorithm but is able to perform a variation of the returned outputs.
For English the TSAR-LSBert uses the same resources over a dataset with marked complex works. 

The Spanish and Portuguese versions have this specific differences with respect the English version: 1) Snowball stemmer, 2) PPDB is not used, 3) language-specific resources (see the resources section). 
 
The code has been modified to return the following sets of 12 output files:


- output of the original LSBert algorithm . The top candidate is selected only if it has a higher frequency (Frequency feature) or lower loss (Language model feature) than the original word. (extension: .out.final )   
- output of all candidates after the Candidate Generation phase.   (extension:  .candidates  )
- output of all candidates after the Substitution Ranking phase.  (extension:  .ranking)
- output of all candidates after the Substitution Ranking phase but with the LSBERT final filter.  (extension:  .ranking_filtered)

- output of the K (user input parameter) top-ranked candidates after the Substitution Ranking phase (no filtering).    (extension:  .final_topk)
- output of the K (user input parameter) top-ranked candidates after the Substitution Ranking phase applying the LSBERT final filter:   The candidates are selected only if they have a higher frequency (Frequency feature) or lower loss (Language model feature) than the original word. (final extension:  .final_topk_filtered)

- output of the 5 (fixed parameter) top-ranked candidates after the Substitution Ranking phase (no filtering).    (extension:  .final_topk5)
- output of the 5 (fixed parameter) top-ranked candidates after the Substitution Ranking phase applying the LSBERT final filter:   The candidates are selected only if they have a higher frequency (Frequency feature) or lower loss (Language model feature) than the original word. (final extension:  .final_topk5_filtered)

- output of the 10 (fixed parameter) top-ranked candidates after the Substitution Ranking phase (no filtering).    (extension:  .final_topk10)
- output of the 10 (fixed parameter) top-ranked candidates after the Substitution Ranking phase applying the LSBERT final filter:   The candidates are selected only if they have a higher frequency (Frequency feature) or lower loss (Language model feature) than the original word. (final extension:  .final_topk10_filtered)

- output of the 50 (fixed parameter) top-ranked candidates after the Substitution Ranking phase (no filtering).    (extension:  .final_topk50)
- output of the 50 (fixed parameter) top-ranked candidates after the Substitution Ranking phase applying the LSBERT final filter:   The candidates are selected only if they have a higher frequency (Frequency feature) or lower loss (Language model feature) than the original word. (final extension:  .final_topk50_filtered)

        
      
Moreover each file has also been generated with a different format, the .debug file format, in which a list of answers/scores for each instance is returned.
So having a total of 24 output files (12 original outputs  + 12 .debug version outputs)




# Evaluation

## Frontiers paper (Štajner et al. 2022 )
  
    In this experiments the TSAR-LSBert returns the top-5 with the LSBert final filter.
    top-5   
    
## TSAR-2022 Shared-Task in Lexical Simplification.
    
    In this experiments the TSAR-LS returns the top-10 results with the LSBert final filter.
    
  
  

## Pre-trained models and other resources

- [BERT based on Pytorch-transformers 1.0](https://github.com/huggingface/pytorch-transformers)
    
    - 
    - 
    - 
    
- [FastText](https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M-subword.zip) (word embeddings trained using FastText)
    
    - English 
    - Spanish
    - Portuguese
    
    https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.es.300.vec.gz
    https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pt.300.vec.gz

- [Frequency databases]
    
    - English - SUBTLEX
    - Spanish - SUBTLEX-ESP
    - Portuguese - SUBTLEX-PT


   
                    
    
    
## How to run this code
    
    
# requirements
    
python modules:     
   - openpyxl
   - transformers
   - torch
   - sklearn
   - numpy
   - scipy
   - pandas
   - nltk
   - nltk packages: average_perceptron_tagger 
    
    
OS commands:
    wget    

# install/run

(1) Use the install_resources.sh script to install some required libraries and download the pre-trained fasttext word embeddings for EN, ES, PT  and the English PPDB
    
(2) Modify the run_LSBert2_<lang>.sh scripts to select the pre-trained transformer and the parameters.
       
    Add the information about the pre-trained model and their tokenizer in the following files:    
     - ./pytorch_pretrained_bert/modeling.py   
     - ./pytorch_pretrained_bert/tokenizer.py   
    
    
(3) run "./run_LSBert2_<lang>.sh"

(4) run "python tsar_eval.py"  with its necessary parameters  to get the evaluation results.


```
Usage: Evaluation Script for the TSAR-2022 Lexical Simplification Shared Task

Usage: tsar_eval.py <options>

Options:
  -h, --help            show this help message and exit
  --gold_file=<PATH>    The path to the file with the gold annotated instances
  --predictions_file=<PATH>
                        The path to file with the predictions
  --output_file=<PATH>  path to the output file
  --verbose             Verbose output mode
    
```
    
(5) run "python tsar_process_runs.py" with its necessary parameters  to get the extended evaluation results.

```
Usage: Evaluation Script for the TSAR-2022 Lexical Simplification Shared Task

Usage: tsar_process_runs.py <options>

Options:
  -h, --help            show this help message and exit
  --dir_runs=<PATH>     path to all runs in a certain language
  --file_gold=<PATH>    path to the file with the gold annotations
  --language=LANGUAGE   language to process (en,es, or pt)
  --output_file=<PATH>  path to the output file
  --verbose             Verbose output mode
```
   

## Citation

1) You can see the specific details of our LSBert adaptation and the resources used in Section 4.2 of this  paper.

Lexical Simplification Benchmarks for English, Portuguese, and Spanish.<br/>
Sanja Štajner, Daniel Ferrés, Matthew Shardlow, Kai North, Marcos Zampieri and Horacio Saggion.<br/>
Front. Artif. Intell. Sec. Natural Language Processing.<br/>
doi: 10.3389/frai.2022.991242<br/>
https://www.frontiersin.org/articles/10.3389/frai.2022.991242/full<br/>



2) The TSAR-LSBert for English was used as a baseline for the TSAR-2022 Shared Task in Lexical Simplification.

Horacio Saggion, Sanja Štajner, Daniel Ferrés, Kim Cheng Sheang, Matthew Shardlow, Kai North,and Marcos Zampieri. 2022. <br/>
Findings of the TSAR-2022 Shared Task on Multilingual Lexical Simplification. <br/>
In Proceedings of the EMNLP Workshop on Text Simplification, Accessibility, and Readability (TSAR-2022). (to appear)<br/>

TSAR-2022 Shared Task github:

https://github.com/LaSTUS-TALN-UPF/TSAR-2022-Shared-Task



3) The original LSBert papers:

Qiang, J., Li, Y., Yi, Z., Yuan, Y., and Wu, X. (2020a). <br/>
“Lexical simplification with pretrained encoders” in Thirty-Fourth AAAI Conference on Artificial Intelligence (New York, NY), 8649–8656. <br/>
doi: 10.1609/aaai.v34i05.6389<br/>


Qiang, J., Li, Y., Zhu, Y., Yuan, Y., and Wu, X. (2020b). <br/>
LSBert: a simple framework for lexical simplification. <br/>
arXiv preprint arXiv:2006.14939. <br/>
doi: 10.48550/arXiv.2006.14939<br/>
https://arxiv.org/abs/2006.14939<br/>


4) The original LSBert code repository:  

https://github.com/qiang2100/BERT-LS

    

## Contact

LaSTUS lab - TALN  @  UPF.
    
