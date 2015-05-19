---
layout: default
---
This project engages with the ['infinite monkey theorem,'](https://en.wikipedia.org/wiki/Infinite_monkey_theorem) which posits that a primate mashing away at the keys of a typewriter will eventually produce a string with literary significance. Borges presents this motif compellingly in his short story "La biblioteca de Babel," which is readily available in English translation. All of the code used in this project is hosted on [GitHub](https://github.com/mgorenstein/monkeystypingfuriously).

A few worthwhile notes about my implementation include:
1) I have limited the possible 'keys' to the lowercase letters and the space character.
2) The space character has a greater likelihood of occurrence (10%), which is justified by the larger size of the space key on standard keyboards. 
3) These virtual primates produce strings between thirteen and twenty characters in length.
4) Each string is split by space and its constituent substrings are searched for in the following (English language wordlist)[http://www-01.sil.org/linguistics/wordlists/english/]. 
5) If all of the substrings occur in the wordlist, the string is made display ready (with the capitalization of the first letter and the addition of an end mark) and is posted along with its approximate position (to three decimal places in scientific notation) in the total number of candidate strings. The strings posted to this webpage are thus the 'best candidates,' those most likely to make grammatical sense. 