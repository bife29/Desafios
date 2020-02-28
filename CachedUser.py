import requests
from sys import argv
import csv,os




def dados(email,website,hemisphere):
    if os.stat('dados.csv').st_size == 0:

        with open('dados.csv', 'w') as csvfile:
            columns = ['Email', 'Website', 'Hemisphere']
            writing = csv.DictWriter(csvfile, fieldnames=columns, delimiter=',', lineterminator='\n')

            writing.writeheader()
            writing.writerow({'Email': email, 'Website': website, 'Hemisphere': hemisphere})
    else:
        with open('dados.csv', 'r') as csvfile:
           leitor = csv.DictReader(csvfile)
           for row in leitor:
               if email in row['Email']:
                   print("Dados ja existente")
               else:
                   with open('/Users/michel.bueno/Documents/Work/Desafio_Globo/dados.csv', 'w') as csvfile:
                       columns = ['Email','Website','Hemisphere']
                       writing = csv.DictWriter(csvfile, fieldnames=columns, delimiter=',' , lineterminator ='\n')

                       writing.writeheader()
                       writing.writerow({'Email':email, 'Website': website, 'Hemisphere': hemisphere})





if __name__ == '__main__':
    user = argv[1]

    try:
        requests = requests.get('https://jsonplaceholder.typicode.com/{}'.format(user))
        address_data = requests.json()

        email = address_data[0]['email']
        website = address_data[0]['website']
        hemisphere = address_data[0]['email']
        dados(email, website, hemisphere)
    except requests.exceptions.RequestException as e:
        print (e)