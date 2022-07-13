""" Match regex patterns to unarxiv CS-Paper fulltext. Write arxiv-id and the found pattern in a output txt-file
"""

import re
import os


regex_pattern = {
      "hasFPO": r'[0-9]*[\.\,]?[0-9]+ ?(.{0,5})? ?(floating-point operations|floating point operations|Floating Point Operations|FPO|fpos|FLOPS|FPOs|FPOS|flops|pflops|tflops)',
      "hasKgOfCo2eq": r'([0-9]*[\.\,]?[0-9]+ ?(metric)? ?(tons|kilogram|gram|t|T|kg|g) ?(of)? ?(CO2|co2|Co2|co 2|carbon)[^\/])',
      "haskWh1": r'energy .{0,15} [0-9]*[\.\,]?[0-9]+ ?(Wh|kWh|MWh|GWh)',
      "haskWh2" : r'[0-9]*[\.\,]?[0-9]+ ?(Wh|kWh|MWh|GWh) (of )?energy',
      "hasJoul1": r'energy .{0,15} [0-9]*[\.\,]?[0-9]+ ?(Joule|joule|joules|J|kJ|MJ|GJ|TJ)[^a-z]',
      "hasJoul2": r'[0-9]*[\.\,]?[0-9]+ ?(Joule|joule|joules|J|kJ|MJ|GJ|TJ)[^a-z](of )?energy',
      "hasWatt1": r'(energy|power) .{0,15} [0-9]*[\.\,]?[0-9]+ ?(Watt|W|kW|MW|GW|TW)[^a-z]',
      "hasWatt2": r'[0-9]*[\.\,]?[0-9]+ ?(Watt|W|kW|MW|GW|TW)[^a-z](of )?energy',
      "hasSocialCost": r'social cost(.{0,10})? ?of \$[0-9]*[\.\,]?[0-9]+',
      "runTime": r'[0-9]+( GPU)? hours( of)? training'
}

i = 0

#Path where the output txt file will be saved 
with open(".../regex_results.txt", "w") as g:
    #Path where the unarXive dataset is located
    for subdir, dirs, files in os.walk(".../unarXive/papers"):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".txt"):
                with open(filepath, 'r') as file_read:
                    
                    data = file_read.read().replace('\n', '')
                    arxiv_id =  "arXiv:" + file.replace(".txt", "")
                    
                    for key, value in regex_pattern.items():
                        matches = re.finditer(value, data)
                        for matchNum, match in enumerate(matches, start=1):
                            g.write('{arxiv_id} matches: {match} \n'.format(arxiv_id= arxiv_id, match = match.group()))

            i += 1
            if i % 100 == 0:
                print('Processed {} papers'.format(i))

          
print("DONE")
print('Processed {} papers in total'.format(i))
