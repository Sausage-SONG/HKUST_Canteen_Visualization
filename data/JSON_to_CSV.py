import csv
import json
import sys
import codecs

target = 'ct1'

def trans(path,date,data):
    transformed_date = '2018 '+date[-9:-7]+' '+date[-7:-5]+' '+date[-4:-2]+' '+date[-2:]
    newdata = {'date':transformed_date}
    with open(path, "r") as f:
        jsonData = json.load(f)
    total = jsonData[target]
    newdata['total'] = total
    data.append(newdata)


def write(path,data):
    csvfile = open(path, 'w', newline='')
    writer = csv.writer(csvfile, dialect='excel')
    keys = ['date', 'total']
    writer.writerow(keys)
    for dic in data:
        writer.writerow([dic['date'], dic['total']])
    csvfile.close()

prefix = 'filter_user_detail_'
file_name = ''
data_total = []

for date in range(20180618, 20180631):
    file_name = prefix + str(date) + '_'

    for hour in range(0, 24):
        if hour < 10:
            file_name = file_name + '0' + str(hour)
        else:
            file_name += str(hour)

        for minute in range(0, 60, 10):
            if minute == 0:
                file_name += '00'
            else:
                file_name += str(minute)

            file_name += '.json'
            trans(file_name, file_name[23:32], data_total)
            print(file_name, ' conversion finished!')
            file_name = file_name[:-5]
            file_name = file_name[:-2]
            out_put = ''

        file_name = file_name[:-2]
    file_name = file_name[:-9]

for date in range(20180701, 20180719):
    file_name = prefix + str(date) + '_'

    for hour in range(0, 24):
        if hour < 10:
            file_name = file_name + '0' + str(hour)
        else:
            file_name += str(hour)

        for minute in range(0, 60, 10):
            if minute == 0:
                file_name += '00'
            else:
                file_name += str(minute)
            file_name += '.json'
            trans(file_name, file_name[23:32], data_total)
            print(file_name, ' conversion finished!')
            file_name = file_name[:-5]
            file_name = file_name[:-2]
            out_put = ''

        file_name = file_name[:-2]
    file_name = file_name[:-9]

path = './CSV/' + target + '.csv'
write(path, data_total)
