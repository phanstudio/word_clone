import re
from Levenshtein import opcodes

class Nt(list):    
    def __add__(self, __value: int) -> list:
        if not (isinstance(__value, list)): 
            return [i+__value for i in self]
        else:
            return super().__add__(__value)
    
    def __sub__(self, __value: int) -> list:
        if not (isinstance(__value, list)): 
            return [i-__value for i in self]
        else:
            return super().__add__(__value)
    
    def __gt__(self, __value: list) -> bool:
        if (isinstance(__value, int)): 
            return [i>__value for i in self]
        else:
            return super().__gt__(__value)

    def __lt__(self, __value: list) -> bool:
        if (isinstance(__value, int)): 
            return [i<__value for i in self]
        else:
            return super().__lt__(__value)
        
    def __ge__(self, __value: list) -> bool:
        if (isinstance(__value, int)): 
            return [i>=__value for i in self]
        else:
            return super().__ge__(__value)
        
    def __le__(self, __value: list) -> bool:
        if (isinstance(__value, int)): 
            return [i<=__value for i in self]
        else:
            return super().__le__(__value)
    
    def _process_list(self, _filter= None, insert = False):
        if _filter == None: _filter = [True]*len(self)

        if len(_filter) != len(self): raise ValueError(
            "_filter list is too short")
        
        if insert:
            return Nt(self[i] + (1* _filter[i]) for i in range(len(self)))
        else:
            return Nt(self[i] - (1* _filter[i]) for i in range(len(self)))

    def overlap(self):
        return len(set(self)) != len(self)

    def __repr__(self) -> str:
        content = ",".join(str(i) for i in self)
        return f'NT({content})'

    def calculate_Nt(self, __value):
        if (isinstance(__value, list)):
            __value.sort(reverse=True)
            new_nt = self
            for i in __value:
                new_nt = new_nt._calc(i[1], i[0], i[2])
            return new_nt
            
    def _calc(self, _value:int, _operation= False, value=1):
        if _operation == 'insert':
            _operation = True 
        elif _operation == 'delete':
            _operation = False
        else:
            return Nt(self.copy())
        return self.process_set(_value, value, _operation,)#self.process_list(fliter_list, _operation)
    
    def process_set(self, _index, _value, insert = True):
        _filter = self >= _index

        if _filter == None: _filter = [True]*len(self)

        if len(_filter) != len(self): raise ValueError(
            "_filter list is too short")

        if insert:
            return Nt(self[i] + (_value* _filter[i]) for i in range(len(self)))
        else:
            return Nt(self[i] - (_value* _filter[i]) for i in range(len(self)))
    
    def process_list(self, _operation, _index, _value):
        _filter = self >= _index

        if _operation == 'insert':
            _operation = True 
        elif _operation == 'delete':
            _operation = False
        else:
            return Nt(self.copy())

        if _filter == None: _filter = [True]*len(self)

        if len(_filter) != len(self): raise ValueError(
            "_filter list is too short")

        if _operation:
            return Nt(self[i] + (_value* _filter[i]) for i in range(len(self)))
        else:
            return Nt(self[i] - (_value* _filter[i]) for i in range(len(self)))

class PropT():
    def __init__(self, it = None, sz = None, wt= None) -> None:
        self.kw = {"size": sz, "weight": wt, "italic": it}
    
    def set(self, _key, _value):
        if _key in list(self.kw.keys()):
            self.kw[_key] = _value
        else:
            # return error
            ...
    
    def get(self, _key):
        return self.kw[_key]
    
    def get_values(self):
        return list(self.kw.values())
    
    def __repr__(self) -> str:
        spc = ' '#"\n  "
        content = spc.join(f"'{k}': {v}" for k, v in self.kw.items())
        return f'\nPT({spc}{content}{spc})'
    
    def __eq__(self, __value: object) -> bool:
        return self.get_values() == __value.get_values()
    
    def copy(self):
        new_copy = PropT()
        for k,w in self.kw.items():
            new_copy.set(k,w)
        return new_copy

def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    return dp[m][n]

def find_differences(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    i, j = m, n
    differences = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j] + 1:
            differences.append(('delete', i-1, 1))
            i -= 1
        elif dp[i][j] == dp[i][j-1] + 1:
            differences.append(('insert', i, 1))
            j -= 1
        elif dp[i][j] == dp[i-1][j-1] + 1:
            differences.append(('replace', i-1, 1))
            i -= 1
            j -= 1
        else:
            i -= 1
            j -= 1
    
    while i > 0:
        differences.append(('delete', i-1, 1))
        i -= 1
    while j > 0:
        differences.append(('insert', i, 1))
        j -= 1
    
    return differences[::-1]

def history(s1,s2):
    differences = [i for i in find_differences(s1, s2)]
    return differences 

def nhistory(s1, s2):
    # Get the opcodes
    operations = opcodes(s1, s2)
    modified_operations = []
    if len(operations) > 3:
        for operation in operations[1:-1]:
            if operation[0] == 'equal':
                modified_operations.append(('replace', 
                                            operation[1], operation[4]-operation[3]))
            else:
                if operation[0] == 'delete':
                    modified_operations.append((operation[0], 
                                            operation[1], operation[2]-operation[1]))
                else:
                    modified_operations.append((operation[0], 
                                            operation[3], operation[4]-operation[3]))
    else:
        if len(operations) > 1:
            for operation in operations:
                if operation[0] != 'equal':
                    if operation[0] == 'delete':
                        modified_operations.append((operation[0], 
                                                operation[1], operation[2]-operation[1]))
                    else:
                        modified_operations.append((operation[0], 
                                                operation[3], operation[4]-operation[3]))
        else:
            for operation in operations:
                modified_operations.append((operation[0], operation[3], 1))
        
    return modified_operations

def convert_to_md(text):
    pattern = r'\((.*?)\)\((.*?)\)'
    matches = re.findall(pattern, text)
    return matches
