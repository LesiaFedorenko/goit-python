from address_book_alchemy import Session, engine, Base
from address_book_alchemy import Contact, Phone, Email, Address
from datetime import date

session = Session()

contacts = session.query(Contact).all()

print('All Contact:', '\n')

for contact in contacts:
    print(contact.name, contact.surname)

contact_phone = session.query(Phone).all()

for phone in contact_phone:
    print(phone)

query_1=session.query(Contact).filter(Contact.name == 'Jennifer').all()
for i in query_1:
    print(i.name, i.birth_date)

query_2=session.query(Contact).filter(Contact.birth_date > date(1976, 3, 24)).all()
for i in query_2:
    print(i.name, i.birth_date)


# q=session.query(Contact).select_from(contact_phone).join(Contact, contact_phone.contact_id == Contact.id).join(Phone, contact_phone.phone_id==Phone.id).filter(Contact.name == 'Jennifer').all()
# for i in q:
#     print(i.name)

# printer_makers = session.query(Product.maker).filter(Product.product_type == 'Printer').all()
# print('All printer makers:' '\n')
# print(printer_makers)
#
# pc_specific_date = session.query(PC).filter(PC.added_at > date(2021, 11, 5))
# print(pc_specific_date)
#
# pc_data = session.query(PC).join(Product).filter(Product.maker == 'Apple').all()
#
# for computer in pc_data:
#     print(f'PC speed is {computer.speed}')
#
#
# max_pc_price = session.query(func.max(PC.speed)).all()
# print(max_pc_price)

session.close()