from flask import Flask, request, render_template
import datetime, string
from typing import List, Dict

app = Flask(__name__)

class PasswordGuesser:
    def __init__(self, password):
        self.password = password
    
    def to_lower(self):
        lower = self.password
        lower = lower.lower()
        return lower; 
        
    def to_upper(self):
        upper = self.password
        upper = upper.upper()
        return upper; 
        
    def capitalize(self):
        cap = self.password
        cap = cap.capitalize()
        return cap; 

    def capitalize_one(self):
        specials = []
        for i in range(len(self.password)):
            variant = self.password[:i] + self.password[i].capitalize() + self.password[i:+1]
            specials.append(variant)
        return specials

    def minimize_one(self):
        specials = []
        for i in range(len(self.password)):
            variant = self.password[:i] + self.password[i].lower() + self.password[i:+1]
            specials.append(variant)
        return specials


class PasswordGuesserAdvanced(PasswordGuesser):
    def __init__(self, password):
        self.password = password

    l33t_dict = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    special_chars = ['!','.', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', '=', '_', '[', ']', '{', '}', ':', ';', '?']
    common_special_chars = ['!', '$', '*', '?','.']


    @staticmethod
    def get_l33t_dict():
        return PasswordGuesserAdvanced.l33t_dict

    def l33t(self):
        l33ted = ''.join(self.l33t_dict.get(c, c) for c in self.password)
        return l33ted
    
    def l33t_progressive(self):
        variants = []
        for i in range(len(self.password)):
            leet_letter = self.l33t_dict.get(self.password[i], self.password[i])  # Utilise la lettre d'origine si pas d'équivalent l33t
            if leet_letter != self.password[i]:  # Vérifier si la lettre doit être remplacée
                variant = self.password[:i] + leet_letter + self.password[i+1:]
                variants.append(variant)
        return variants
    
    def remove_accents(self):
        import unicodedata
        acc_less = ''.join(c for c in unicodedata.normalize('NFD', self.password)
                                if unicodedata.category(c) != 'Mn')
        return acc_less; 

    def add_special_chars(self):
        specials = []
        for i in range(len(self.password)+1):
            for special in self.common_special_chars:
                variant = self.password[:i] + special + self.password[i:]
                specials.append(variant)
        return specials
    

class PasswordGuesserDate(PasswordGuesser):
    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def date_to_french(self, date_str):
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d %B %Y')
    
    def date_to_two_digits_year(self, date_str):
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%y')
    
    def date_to_four_digits_year(self, date_str):
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    
    def add_all_special_chars(self):
        specar = self.password
        specar += string.punctuation
        return specar; 
        


#Pour l'implémentation de la composition
class PasswordModifier:
    def __init__(self, password):
        self.password = password
    
    def to_lower(self):
        lower = self.password
        lower = lower.lower()
        return lower; 
        
    def to_upper(self):
        upper = self.password
        upper = upper.upper()
        return upper; 
        
    def capitalize(self):
        cap = self.password
        cap = cap.capitalize()
        return cap; 


class PasswordModifierAdvanced:
    def __init__(self, password_modifier):
        self.password_modifier = password_modifier
    
    def l33t(self):
        l33t_dict = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
        l33ted = ''.join(l33t_dict.get(c, c) for c in self.password_modifier.password)
        return l33ted
    
    def remove_accents(self):
        import unicodedata
        acc_less = ''.join(c for c in unicodedata.normalize('NFD', self.password_modifier.password)
                                if unicodedata.category(c) != 'Mn')
        return acc_less; 




# tests
def generate_password_variants(password: str, date: str = None) -> List[str]:

    variants = []

    # tester chaque variation d'un mot
    base_pg = PasswordGuesser(password)
    base_pga = PasswordGuesserAdvanced(password)
    
    password_variations = [ base_pg.to_lower(), base_pg.to_upper(), base_pg.capitalize(), base_pga.remove_accents()]
    password_variations.extend(base_pg.capitalize_one())
    password_variations.extend(base_pg.minimize_one())

    for i in range(len(password_variations)):

        pg = PasswordGuesser(password_variations[i])
        pga = PasswordGuesserAdvanced(password_variations[i])
        # Base variations
        variants.extend([
            pg.to_lower(),
            pg.to_upper(),
            pg.capitalize(),
        ])
        # Advanced variations
        variants.extend([
            pga.l33t(),
            pga.remove_accents(),
        ])
        # Progressive l33t variations
        variants.extend(pga.l33t_progressive())
        variants.extend(pga.add_special_chars())



    # tester chaque variation d'une date
    pgd = PasswordGuesserDate("password")
    all_dates = []

    # Appel des méthodes de la classe PasswordGuesserDate
    all_dates.append(pgd.date_to_french(date))
    all_dates.append(pgd.date_to_two_digits_year(date))
    all_dates.append(pgd.date_to_four_digits_year(date))

    for k in range(len(all_dates)):
        for j in range(len(password_variations)):
            pg = PasswordGuesser(password_variations[j]+all_dates[k])
            pga = PasswordGuesserAdvanced(password_variations[j]+all_dates[k])
            # Base variations
            variants.extend([
                pg.to_lower(),
                pg.to_upper(),
                pg.capitalize(),
            ])
            # Advanced variations
            variants.extend([
                pga.l33t(),
                pga.remove_accents(),
            ])
            # Progressive l33t variations
            variants.extend(pga.l33t_progressive())
            variants.extend(pga.add_special_chars())

    for k in range(len(all_dates)):
        for j in range(len(password_variations)):
            pg = PasswordGuesser(all_dates[k]+password_variations[j])
            pga = PasswordGuesserAdvanced(all_dates[k]+password_variations[j])
            # Base variations
            variants.extend([
                pg.to_lower(),
                pg.to_upper(),
                pg.capitalize(),
            ])
            # Advanced variations
            variants.extend([
                pga.l33t(),
                pga.remove_accents(),
            ])
            # Progressive l33t variations
            variants.extend(pga.l33t_progressive())
            variants.extend(pga.add_special_chars())




    return variants



# password = "bonjour"
# date = "2023-06-30"
# combinations = generate_password_variants(password, date)
# print(combinations)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.values['text-field-1']
        date = "2023-06-30"
        combinations = generate_password_variants(password, date)
        print(combinations)
        return render_template('index.html', mdp=combinations)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)