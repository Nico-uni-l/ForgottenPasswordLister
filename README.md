# Forgot your own password?
## Create your own password-bruteforce-list based on known letters.


Simple, small project that calculates all permutations using all already known letters. It builds all combinations with other printable ascii characters. Only reasonable for short passwords or a high number of known letters. It also provides the possibility to remove characters that are definitly not a part of the password, f.ex. `&,%,?,..`

Possible situations: "aah damn I know my password was like 5 characters long and contained a k 1". 
This script calculates all possible passwords and writes them to a file, easy to use for bruteforcing.

### Usage:

`git clone https://github.com/Nico-uni-l/ForgottenPasswordLister.git`

`python3 lister.py <known-letters> <password-length> <output-filename>`

Expample: python3 lister.py ak1 5 pwList.txt





