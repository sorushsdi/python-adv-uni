import requests as a
class Fetcher:
   
    def __init__(self):
        L = a.get("https://cdn.ituring.ir/ex/users.json")
        self.student = a
        sum_score = 0
   
   
    def nurds(self):
        for b in self.students:
            if b["score"] > 18.5:
                return {b["name"], b["last_name"]}
   
   
    def mean(self):
        for b in self.students:
            sum_score += b["score"] 
        return(sum_score/ len(self.students))
   
   
    def get_student(self):
     	for b in self.students:
 	        if b["city","state","location"]==0:
 	            return [{b["nsme"],b["last_name"]}]
   
   
    def sultans(self):
        for b in self.students:                   
 	         max_score==max (b ["score"])
        return tuple ((b["name"],b["last_name"]))
 	