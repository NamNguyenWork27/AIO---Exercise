
def exercise1(tp, fp, fn):
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        if not isinstance(tp, int):
            print("to must be int")
        if not isinstance(fp, int):
            print("to must be int")
        if not isinstance(fn, int):
            print("to must be int")
        return 
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp anf fn must be greater than zero")
        return
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f'Precision:{precision}')
    print(f'Recall: {recall}')
    print(f'F1-score: {f1_score}')
    
   

if __name__ == "__main__":
    tp = int(input("Enter true positives: "))
    fp = int(input("Enter false positives: "))
    fn = int(input("Enter false negatives: "))
    
    exercise1(tp, fp, fn)
    