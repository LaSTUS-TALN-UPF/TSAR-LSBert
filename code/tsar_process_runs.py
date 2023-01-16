# -*- coding: utf-8 -*-

# Official evaluation script for TSAR-2022 Shared Task on Lexical Simplification for English, Portuguese and Spanish.
# site: https://taln.upf.edu/pages/tsar2022-st/



import sys
from optparse import OptionParser
import math
from tsar_eval_lib import TSAR2022_SharedTask_Evaluator
from os import listdir
from os.path import isfile, join
import pandas as pd


def normalize(val):
    factor=10000
    return math.floor(val * factor) / factor   
    
    #return round(val, 4)

class TSAR2022_ProcessRuns(object):

    def __init__(self,output_file,verbose):
        self.verbose=verbose
        self.output_file=output_file
        self.evaluator=TSAR2022_SharedTask_Evaluator(verbose)
        
    
    def eval_a_file(self,gold_filepath,filepath,language):
        
        
        
        lang = language
        run = filepath.split('_')[-1]
        run = run.split('.')[0]
        team_name=filepath.split('_')[-2]
        
        
        result = {'Team': team_name , 'Lang': lang, 'Run': run}
        
        self.evaluator.read_files(gold_filepath, filepath)
        
        result[f'ACC@1'] = normalize(self.evaluator.computeAccuracy_at_1())
        # compute accuracy
        for k in [1, 2, 3 ,4, 5,6,7,8,9,10]:
            result[f'ACC@{k}@Top1'] = normalize(self.evaluator.computeAccuracy_at_N_at_top_gold_1(k))
            
        # compute MAP
        for k in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            result[f'MAP@{k}'] = normalize(self.evaluator.computeMAP_at_K(k))
        
        # compute potential, precision, Reecall, ... 
        tmp_result = {'potential': [], 'precision': [], 'recall': []} 
        for k in [1, 2, 3, 4, 5, 6, 7,8, 9, 10]:
            # macro_avg_precision, macro_avg_recall, macro_avg_F1, micro_avg_precision, micro_avg_recall, micro_avg_f1, potential = evaluator.computePrecisionMetrics_at_K(k)
            macro_avg_precision, macro_avg_recall, _, _, _, _, potential = self.evaluator.computePrecisionMetrics_at_K(k)
            tmp_result['potential'].append((f'Potential@{k}', normalize(potential)))
            tmp_result['precision'].append((f'Precision@{k}', normalize(macro_avg_precision)))
            tmp_result['recall'].append((f'Recall@{k}', normalize(macro_avg_recall)))
                                        
        for key in tmp_result:
            for metric, value in tmp_result[key]:
                result[metric] = value
                
        return result 


def main():

    
    # arg parsing
    parser = OptionParser(usage='Evaluation Script for the TSAR-2022 Lexical Simplification Shared Task\n\nUsage: %prog <options>')

    parser.add_option('--dir_runs', help='path to all runs in a certain language', metavar='<PATH>', action='store', type='string', dest='dir_runs', default='' )
    parser.add_option('--file_gold', help='path to the file with the gold annotations', metavar='<PATH>', action='store', type='string', dest='file_gold', default='' )    
    parser.add_option('--language', help='language to process (en,es, or pt)',  action='store', type='string', dest='language', default='')
    parser.add_option('--output_file', metavar='<PATH>', action='store', type='string',dest='output_file', default='', help='path to the output file')
    parser.add_option('--verbose', help='Verbose output mode',  action='store_true')
    
    

    
    (options, args) = parser.parse_args(sys.argv) 
    
    if (options.dir_runs==''):
        print("Error: runs path missing!")
        print(parser.print_help())
        sys.exit(1)


    if (options.file_gold==''):
        print("Error: file gold missing!")
        print(parser.print_help())
        sys.exit(1)

    if (options.language==''):
        print("Error: language option is missing!")
        print(parser.print_help())
        sys.exit(1)


    if (options.output_file==''):
        print("Error: path to the output file is missing!")
        print(parser.print_help())
        sys.exit(1)


    
    

    runs_evaluator=TSAR2022_ProcessRuns(options.output_file,options.verbose)

    files_runs_language = [ f for f in listdir(options.dir_runs) if isfile(join(options.dir_runs,f)) ]

    
    
    all_results=[]
    
    for run_file in files_runs_language:
        print(run_file)
        result=runs_evaluator.eval_a_file(options.file_gold,options.dir_runs+"/"+run_file,options.language)
        print(result)
        all_results.append(result)
    

    all_results_df = pd.DataFrame(all_results)
    all_results_df_sorted = all_results_df.sort_values('ACC@1', ascending=False)
    all_results_df_sorted.to_csv(options.output_file)




if __name__ == '__main__':
    main()

