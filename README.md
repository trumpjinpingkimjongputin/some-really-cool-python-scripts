# some-really-cool-python-scripts

### Cryptography Fernet/cryptography_fernet.py
install these dependencies
`pip install cryptography argparse`

in the directory where the script is located - make a myfile.txt and write some info

Open ur terminal

To encrypt myfile.txt , run - 
`python3 cryptography_fernet.py myfile.txt encrypt`
(python incase of windows )

To decrypt the file , run - 
`python3 cryptography_fernet.py myfile.txt decrypt`

You would notice, that a secret.key file is created. This file contains ur encryption key. Your encrypted data can only be decrypted if this file exists. 
To really safegaurd the info - move this encryption key somewhere else.