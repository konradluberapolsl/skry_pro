import glob

html = open("strona.html", 'w')

path_1 = "input/*.txt"
path_2 = "output/szyfr*.txt"
path_3 = "output/odszyfrowane*.txt"
files_1 = glob.glob(path_1)
files_2 = glob.glob(path_2)
files_3 = glob.glob(path_3)

words = []
encrypted = []
decrypted = []

for name in files_1:
    with open(name) as f:
        word = f.readlines()
        words += word
        f.close()


for name in files_2:
    with open(name) as f:
        word = f.readlines()
        encrypted += word
        f.close()

for name in files_3:
    with open(name) as f:
        word = f.readlines()
        decrypted += word
        f.close()

# words = open("input/tekst.txt",'r')
# encrypted = open("output/szyfr.txt", 'r')
# decrypted = open("output/odszyfrowane.txt", 'r')

html.write('<!DOCTYPE HTML>\n'
           '<html lang="pl">\n<head>'
           '    <meta charset="utf-8" />\n'
           '    <title>Jezyki Skryptowe Projekt</title>\n'
           '    <meta name="descripton" content="Projekt semestralny Języki Skryptowe Konrad Lubera"/>\n'
           '    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/> \n'
           '    <link rel="stylesheet" href="style.css" type="text/css" /> \n'
           '    <link href="https://fonts.googleapis.com/css?family=Lato&display=swap" rel="stylesheet"> \n'
           '</head> \n'
           '<body> \n'
           '    <div id="container"> \n'
           '        <div id="header"> \n'
           '         "Szyfrowanie wiadomosci" - Algorytmion 2015 \n         </div> \n'
           '        <div id="content"> \n'
           '            <div id="tab">\n'
           '            <table>\n'
           '                 <tr>\n'
           '                     <th>tekst.txt</th>\n'
           '                     <th>szyfr.txt</th>\n'
           '                     <th>odszyfrowane.txt</th>\n'
           '                 </tr>\n')
i = 0
j = 0
n = 0
while (i != len(words)) and (j != len(encrypted)) and (n != len(decrypted)):
            html.write('                 <tr>\n                     <td>')
            html.write(words[i].replace('\n',''))
            html.write('</td>\n                     <td>')
            html.write(encrypted[j].replace('\n',''))
            html.write('</td>\n                     <td>')
            html.write(decrypted[n].replace('\n', ''))
            html.write('</td> \n                 </tr>\n')
            i+=1
            j+=1
            n+=1
html.write('             </table>\n'
           '             </div>\n'
           '            <div id="txt">Ponizej zestwaienie czestowliwosci wystepowania danych systemow liczbowych </div> \n'
           '            <img src="images\plot.png"/>\n'           
           '        </div> \n'
           '           <div id="footer"> \n'
           '            &copy Konrad Lubera, RMS POLSL \n'
           '           </div> \n'
           '    </div> \n'
           '</body> \n'
           )
html.close()
