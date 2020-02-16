from btctools.HD import check, WORDS
from btctools import Xprv
import json


phrases = [
    "{x} rent giraffe gold assist cricket face clip soul bicycle surface rebel",
    "rent {x} giraffe gold assist cricket face clip soul bicycle surface rebel",
    "rent giraffe {x} gold assist cricket face clip soul bicycle surface rebel",
    "rent giraffe gold {x} assist cricket face clip soul bicycle surface rebel",
    "rent giraffe gold assist {x} cricket face clip soul bicycle surface rebel",
    "rent giraffe gold assist cricket {x} face clip soul bicycle surface rebel",
    "rent giraffe gold assist cricket face {x} clip soul bicycle surface rebel",
    "rent giraffe gold assist cricket face clip soul {x} bicycle surface rebel",
    "rent giraffe gold assist cricket face clip soul bicycle {x} surface rebel",
    "rent giraffe gold assist cricket face clip soul bicycle surface {x} rebel",
    "rent giraffe gold assist cricket face clip soul bicycle surface rebel {x}"
]

total_phrases = []
for phrase in phrases:
    for word in WORDS:
        mnemonic = phrase.format(x=word)
        if check(mnemonic):
            total_phrases.append(mnemonic)

print(f'total number of phrases generated for analysis:', len(total_phrases))


master_address_list = []

for phrase in total_phrases:

    m = Xprv.from_mnemonic(phrase)

    for i in range(0, 5):
        addr = (m/44./0./0./0/i).address('P2PKH')
        if addr == '1C26mdyEsNpe4fpkYtuHzH4Y378wez8mxP':
            master_address_list.append({addr: phrase})
        elif addr == '1BjoCJhvRCx9nVLPaKhg4qQ2YYps8mDgY4':
            master_address_list.append({addr: phrase})


print(f'Address match(s) found: ', len(master_address_list))
print(json.dumps(master_address_list, indent=4, sort_keys=True))
