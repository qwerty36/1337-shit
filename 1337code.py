#################################################################
##Praktisch Tentamen Python I####################################
##Richard Jansen, HAN University of Applied Sciences, Nijmegen###
## 16-01-2015####################################################
#################################################################

def main():                                             
    d, a, s= searchSymptoms('symptomen.txt', 'userinput')
    write(d, d, s)
    
#####################################################################
#vraagt gebruiker om input en vergelijkt die met het gelezen bestand#
#####################################################################
def searchSymptoms(source, userinput):
    try:
        data = ''
        file = open(source, mode='r')
        while data == '' or userinput == '':
            userinput = str(input('Symptoom: '))
            for line in file:
                if userinput.upper() in line.upper():
                     data = line.split("\t")[2]
                     symptomen = line.split("\t")[1]
                     deviatie = line.split("\t")[0]
        print(data)
        file.close()
        return data, deviatie, symptomen
    except IOError:
        print('File not found ')
    except IndexError:
        print('IndexError ')
    except KeyboardInterrupt:
        print('Aborted ')

############################################################
#Maakt nieuwe bestanden met daarin de uitkomst van de query#
############################################################
def write(genen, deviatie, symptomen):
    try:
        filename = 'kandidaatgenen_' +(str(afwijking).upper()) +'.txt.'
        file = open(filename, mode='w')
        file.write('symptoom:' +'\t' +'kandidaatgenen:\n')
        file.write(symptomen +'\t' +genen)
        file.close
    except IOError:
        print('File not found: ')
    except KeyboardInterrupt:
        print('Aborted: ')

main()
