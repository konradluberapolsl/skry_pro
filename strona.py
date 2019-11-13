html = open("strona.html", 'w')
words = open("input\\tekst.txt",'r')
encrypted = open("input\\szyfr.txt", 'r')
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
while (line_1 := words.readline()) and (line_2 := encrypted.readline()) :
            html.write('                 <tr>\n                     <td>')
            html.write(line_1.replace('\n',''))
            html.write('</td>\n                     <td>')
            html.write(line_2.replace('\n',''))
            html.write('</td> \n                 </tr>\n')
html.write('             </table>\n'
           '             </div>\n'
           '        </div> \n'
           '           <div id="footer"> \n'
           '            &copy Konrad Lubera, RMS POLSL \n'
           '           </div> \n'
           '    </div> \n'
           '</body> \n'
           )
html.close()
words.close()
encrypted.close()
