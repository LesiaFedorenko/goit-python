import csv

class Contacts:

    def __init__(self, path):
        self.path = path
        self.list_contact = []

    def open_fun(self):
        with open(self.path, 'r') as fh:
            while True:
                line = fh.readline()
                for_contact = line.split(';')
                if len(for_contact) > 3 and for_contact[3].removesuffix('\n').isdigit():
                    self.list_contact.append(for_contact[3].removesuffix('\n'))
                if not line:
                    break
            return self.list_contact

    def sanitize_phone_38(self):
        for i in range(len(self.list_contact)):
            if self.list_contact[i].removeprefix("38"):
                self.list_contact[i] = self.list_contact[i].removeprefix("38")
        return f"Clean of '38' {self.list_contact}"

    def sanitize_phone_00(self):
        for i in range(len(self.list_contact)):
            if self.list_contact[i].removeprefix("00"):
                self.list_contact[i] = self.list_contact[i].removeprefix("00")
        return f"Clean of '00' {self.list_contact}"

    def delete_duplicate(self):
        self.list_contact = set(self.list_contact)
        self.list_contact = list(self.list_contact)
        return f" List without duplicate {self.list_contact}"

    def invalid_list(self):
        list_invalid = []
        for phone in self.list_contact:
            if len(phone) < 10:
                list_invalid.append(phone)
        return f" Invalid list (len<10) {list_invalid}"

    def intersection_func(self, other):
        return f" Intersection {list(set(self.list_contact).intersection(set(other.list_contact)))}"

    def int_difference_func(self, other):
        with open('int_contact.csv', 'w', newline='\n') as file:
            for phone in range(len(list(set(self.list_contact).difference(set(other.list_contact))))):
                writer = csv.writer(file, delimiter=';')
                writer.writerow([list(set(self.list_contact).difference(set(other.list_contact)))])
        return f" Internal difference {list(set(self.list_contact).difference(set(other.list_contact)))}"

    def ext_difference_func(self, other):
        with open('ext_contact.csv', 'w', newline='\n') as file:
            for phone in range(len(list(set(other.list_contact).difference(set(self.list_contact))))):
                writer = csv.writer(file, delimiter=';')
                writer.writerow([list(set(other.list_contact).difference(set(self.list_contact)))])
        return f" External difference {list(set(other.list_contact).difference(set(self.list_contact)))}"

    def operator(self, other):
        new_list= self.list_contact+other.list_contact
        vodafon_list=["050", "095", "099", "066"]
        kyivstar_list = ["067", "096", "097", "098", "039"]
        lifecell_list = ["063", "073", "091", "092", "094"]
        Vodafon =[]
        Kyivstar=[]
        LifeCell=[]
        for phone in new_list:
            if phone[:3] in kyivstar_list:
                Kyivstar.append(phone)
            elif phone[:3] in vodafon_list:
                Vodafon.append(phone)
            elif phone[:3] in lifecell_list:
                LifeCell.append(phone)
        with open('C:\Old D\GO IT\Kyivstar.csv', 'w+', newline='') as file:
            for phone in range(len(Kyivstar)):
                writer = csv.writer(file, delimiter=';')
                writer.writerow([Kyivstar[phone]])

        with open('Vodafon.csv', 'w', newline='\n') as file:
            for phone in range(len(Vodafon)):
                writer = csv.writer(file, delimiter=';')
                writer.writerow([Vodafon[phone]])

        with open('LifeCell.csv', 'w', newline='\n') as file:
            for phone in range(len(LifeCell)):
                writer = csv.writer(file, delimiter=';')
                writer.writerow([LifeCell[phone]])

        return f" Vodafon{Vodafon}\n Kyivstar{Kyivstar}\n LifeCell{LifeCell}"

    def save_file(self, path_for_save, data):
        with open(path_for_save, 'w', newline='\n') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([data])
        print('File was written successfully')

ivent = Contacts('in_zohot.csv')

print(ivent.open_fun())
print(ivent.sanitize_phone_38())
print(ivent.sanitize_phone_00())
print(ivent.delete_duplicate())
print(ivent.invalid_list())

bot = Contacts('bot.csv')

bot.open_fun()
bot.sanitize_phone_38()
bot.sanitize_phone_00()
bot.delete_duplicate()
print(bot.invalid_list())

print(ivent.intersection_func(bot))
print(ivent.int_difference_func(bot))
print(ivent.ext_difference_func(bot))

print(ivent.operator(bot))

ivent.save_file("test.csv", ivent.invalid_list())
