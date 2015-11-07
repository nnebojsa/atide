import json

class atide:
    
    description = "Keine Beschreibung"
    author = "Kein Author"
    
    def __init__(self, rev_1, rev_2, expenses):
        
        self.rev_1 = float(rev_1)
        self.rev_2 = float(rev_2)
        self.expenses = expenses

    
    def show_atide(self):
        return self.rev_1, self.rev_2, self.expenses, self.author, self.description
    
    def describe(self, text):
        self.description = text
    
    def authorName(self, text):
        self.author = text
        
    def calcAtide(self):
        # total revenues
        total_rev =  self.rev_1 + self.rev_2
        
        # revenue percent on total revenues 
        prc_rev1 = round(((self.rev_1 / total_rev) * 100), 2)
        prc_rev2 = round(((self.rev_2 / total_rev) * 100), 2)
        
        # convert prc to value on total_rev
        prc_val_rev1 = round(((self.expenses * prc_rev1) / 100), 2)
        prc_val_rev2 = round(((self.expenses * prc_rev2) / 100), 2)
        
        # diff between total_rev and expenses
        diff_tr_ex = total_rev - self.expenses 
        
        # convert prc to value on diff between total_rev and expenses
        prc_val_diff1 = round(((diff_tr_ex * prc_rev1) / 100), 2)
        prc_val_diff2 = round(((diff_tr_ex * prc_rev2) / 100), 2)
        
        result = json.dumps({'rev_1':self.rev_1,\
                             'rev_2':self.rev_2,\
                             'expenses':self.expenses,\
                             'total_rev':total_rev,\
                             'prc_rev1':prc_rev1,\
                             'prc_val_rev1':prc_val_rev1,\
                             'prc_rev2':prc_rev2,\
                             'prc_val_rev2':prc_val_rev2,\
                             'diff_tr_ex': diff_tr_ex,\
                             'prc_val_diff1':prc_val_diff1,\
                             'prc_val_diff2':prc_val_diff2
                             }, indent=3, sort_keys=False
                            )
        #return self.expenses, total_rev, prc_rev1, prc_val_rev1, prc_rev2, prc_val_rev2, diff_tr_ex, prc_val_diff1, prc_val_diff2
        return result


test = atide(1500,1500,3000)
#test.authorName("Nebojsa Nikolic")
#test.describe("Einfache Test Klasse")

# print atide.show_atide(test)
print atide.calcAtide(test)
