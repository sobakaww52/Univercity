import re
import urllib.request
import csv


url = 'https://msk.spravker.ru/avtoservisy-avtotehcentry/'
response = urllib.request.urlopen(url)
html_code = response.read().decode('utf-8')


regular = r"(?:-link\">)(?P<Name>[^<]+)"\
    r"(?:[^o]*[^l]*.*\n *(?P<Address>[^\n]+))"\
    r"(?:\s*.*>\s*.*>\s*.*>(?:\s*<d[^>]*>(?:\s*.*\s*.*>(?P<Phone_Number>[^<]+))?.*>\s*</dl>)"\
    r"(?:\s*<.*>(?:\s*<.*\s*<.*>(?P<WorkHours>[^<]+))?</dd>)?)?"


matches = re.findall(regular, html_code)


output_file = 'database.csv'
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Address', 'Phone', 'Hours'])
    writer.writerows(matches)

print(f"Данные успешно сохранены в файл {output_file}.")