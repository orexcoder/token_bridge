import json

source_chains = ['bsc','linea', 'opbnb', 'combo']
dest_chains = ['combo','mantle', 'opbnb', 'bsc']


rpcs = {
    "bsc": "https://rpc.ankr.com/bsc",
    "linea": "https://rpc.linea.build",
    "combo": "https://rpc.combonetwork.io",
    "opbnb": "https://opbnb-rpc.publicnode.com"
}

destchain_ids = {
    'mantle': 20,
    'combo' : 27,
    'opbnb': 23,
    'bsc': 3
}


contracts = {
    "bsc": "0x51187757342914E7d94FFFD95cCCa4f440FE0E06",
    "linea": "0x366C1B89aA0783d0886B9EF817d10c8729783dCb",
    "combo": "0x254010e880e04a27c98cbb8d241f8c3554d3784d",
    "opbnb": "0x953a578c7ce8f3a1bf625d182a8caf7181fd4beb"

}

pools = {
    "bsc" : 10,
    "linea": 1,
    "opbnb": 10,
    "combo":10

}

scans = {
    "combo": "https://combotrace.nodereal.io/tx/",
    "bsc": "https://bscscan.com/tx/",
    "opbnb": "https://opbnbscan.com/tx/",
    "linea": "https://lineascan.build/tx/"
}

#
# with open('abis/lineaABI.json') as f:
#     linea_abi = json.load(f)
#
# with open('abis/bscABI.json') as f:
#     bsc_abi = json.load(f)

with open('abis/zkbridgeABI.json') as f:
    zkb_abi = json.load(f)

abis = {
    "bsc": zkb_abi,
    "linea": zkb_abi,
    "zkbridge": zkb_abi
}

with open("accounts.txt") as f:
    private_keys = [r.strip() for r in f.readlines()]