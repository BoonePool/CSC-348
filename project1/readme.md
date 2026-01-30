1.1: the ceasar shift was fairly straightforward. The first step was getting the values and adding the shift, if it is in decypt mode the shift is inverted. For normalizing the shift I subtracted 32 then modded by the range of the values to do the wrap around. from there it was just putting it together to produce the result
1.2 was a bit less easy, I used the characters in the result to iterate through the keyword, then normalized the char by subtracting 32 and used it as the shift.
2.1 the work is in the PDF
2.2 the frequencey analysis is done by initilizing the dictionary to zero then adding 1/the length each time it occurs.
2.3 This took a bit of reading but I just multiplied the corresponding frequencies and summed them
2.4 for cracking the encyption I just calculated cross correlation for all possible shifts and took the max
2.5 for cracking vigenere I just took every nth char where n is the length of the key and did a ceasar crack on it