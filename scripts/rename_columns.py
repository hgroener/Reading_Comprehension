import pandas as pd 
import re 

c_dic = {"article_batch": "batch", 
         "onestopqa_question_id": "q_ind",
         "difficulty_level": "level", 
         "list_number": "list", 
         "answer_1": "a",
         "answer_2": "b", 
         "answer_3": "c",
         "answer_4": "d",
         "question_preview": "has_preview",
         "participant_id": "subject_id",
         "selected_answer_position": "FINAL_ANSWER", 
         "repeated_reading_trial": "reread", 
         "practice_trial": "practice",
         "selected_answer": "abcd_answer"}

letter_dic = {"A":"0", "B":"1", "C":"2", "D":"3"}

def rename_ao(ao):
    for letter in letter_dic.keys():
        ao = re.sub(f'\"\'{letter}\',?\"', letter_dic[letter], ao)
    return ao

#c_dic = {"article_batch": "batch", "practice_trial": "practice", "question_preview": "has_preview"}

path = "/srv/storage/hgroener/reading_comprehension/OneStop/onestop/"
#files = ["fixation_reports/fixation_data_enriched_360_19092025.csv", "ia_reports/ia_data_enriched_360_18092025.csv"]
files = ["fixation_reports/fixations_Paragraph.csv",
         "ia_reports/ia_Paragraph.csv"]

for f in files: 
    df = pd.read_csv(path + f).fillna(0)
    df = df.rename(columns=c_dic)
    df["answers_order"] = df["answers_order"].apply(rename_ao)
    df.to_csv(path + "renamed/" + f.split(".")[0]+"_renamed.csv")