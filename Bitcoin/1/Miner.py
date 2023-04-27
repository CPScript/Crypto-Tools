# ||==========================================||
# || DarkMater by: Disease, known as CPScript ||
# ||==========================================||

# ============================Start================================

import binascii # By Disease
import hashlib # By Disease
import json # By Disease
import logging # By Disease
import random # By Disease
import socket # By Disease
import threading # By Disease
import time # By Disease
import traceback # By Disease
from datetime import datetime # By Disease
from signal import SIGINT , signal # By Disease
 # By Disease
import requests # By Disease
from colorama import Back , Fore , Style # By Disease
 # By Disease
import context as ctx # By Disease
 # By Disease
import os # By Disease
from os  import system # By Disease
from subprocess import call # By Disease
from platform import platform # By Disease
 # By Disease
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6] # By Disease
 # By Disease
if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'): # By Disease
    delet = 'cls' # By Disease
    dr = '\\' # By Disease
else: # By Disease
    delet = 'clear' # By Disease
    dr = '/' # By Disease
 # By Disease
os.system(delet) # By Disease
 # By Disease
 # By Disease
sock = None # By Disease
 # By Disease
def timer() : # By Disease
    tcx = datetime.now().time() # By Disease
    return tcx # By Disease
 # By Disease
# Changed this Address And Insert Your BTC Wallet
 # By Disease
address = 'bc1q4uuexl9p2tkgdzpzpmtu8wtrckyt5lq95wqy4n'  # By Disease
 # By Disease
print(Back.BLUE , Fore.WHITE , 'BTC WALLET:' , Fore.BLACK , str(address) , Style.RESET_ALL) # By Disease
 # By Disease
 # By Disease
def handler(signal_received , frame) : # By Disease
    # Handle any cleanup here # By Disease
    ctx.fShutdown = True # By Disease
    print(Fore.MAGENTA , '[' , timer() , ']' , Fore.YELLOW , 'Terminating, Please Wait..') # By Disease
 # By Disease
 # By Disease
def logg(msg) : # By Disease
    # basic logging # By Disease
    logging.basicConfig(level = logging.INFO , filename = "miner.log" , # By Disease
                        format = '%(asctime)s %(message)s')  # include timestamp # By Disease
    logging.info(msg) # By Disease
 # By Disease
 # By Disease
def get_current_block_height() : # By Disease
    # returns the current network height # By Disease
    r = requests.get('https://blockchain.info/latestblock') # By Disease
    return int(r.json()['height']) # By Disease
 # By Disease
 # By Disease
def check_for_shutdown(t) : # By Disease
    # handle shutdown # By Disease
    n = t.n # By Disease
    if ctx.fShutdown : # By Disease
        if n != -1 : # By Disease
            ctx.listfThreadRunning[n] = False # By Disease
            t.exit = True # By Disease
 # By Disease
 # By Disease
class ExitedThread(threading.Thread) : # By Disease
    def __init__(self , arg , n) : # By Disease
        super(ExitedThread , self).__init__() # By Disease
        self.exit = False # By Disease
        self.arg = arg # By Disease
        self.n = n # By Disease
 # By Disease
    def run(self) : # By Disease
        self.thread_handler(self.arg , self.n) # By Disease
        pass # By Disease
 # By Disease
    def thread_handler(self , arg , n) : # By Disease
        while True : # By Disease
            check_for_shutdown(self) # By Disease
            if self.exit : # By Disease
                break # By Disease
            ctx.listfThreadRunning[n] = True # By Disease
            try : # By Disease
                self.thread_handler2(arg) # By Disease
            except Exception as e : # By Disease
                logg("ThreadHandler()") # By Disease
                print(Fore.MAGENTA , '[' , timer() , ']' , Fore.WHITE , 'ThreadHandler()') # By Disease
                logg(e) # By Disease
                print(Fore.RED , e) # By Disease
            ctx.listfThreadRunning[n] = False # By Disease
 # By Disease
            time.sleep(2) # By Disease
            pass # By Disease
 # By Disease
    def thread_handler2(self , arg) : # By Disease
        raise NotImplementedError("must impl this func") # By Disease
 # By Disease
    def check_self_shutdown(self) : # By Disease
        check_for_shutdown(self) # By Disease
 # By Disease
    def try_exit(self) : # By Disease
        self.exit = True # By Disease
        ctx.listfThreadRunning[self.n] = False # By Disease
        pass # By Disease
 # By Disease
 # By Disease
def bitcoin_miner(t , restarted = False) : # By Disease
    if restarted : # By Disease
        logg('\n[*] Restarted') # By Disease
        print(Fore.MAGENTA , '[' , timer() , ']' , Fore.BLUE , '[*] Restarted') # By Disease
        time.sleep(5) # By Disease

    target = (ctx.nbits[2 :] + '00' * (int(ctx.nbits[:2] , 16) - 3)).zfill(64) # By Disease
    extranonce2 = hex(random.randint(0 , 2 ** 32 - 1))[2 :].zfill(2 * ctx.extranonce2_size)  # create random # By Disease
 # By Disease # By Disease
    coinbase = ctx.coinb1 + ctx.extranonce1 + extranonce2 + ctx.coinb2 # By Disease
    coinbase_hash_bin = hashlib.sha256(hashlib.sha256(binascii.unhexlify(coinbase)).digest()).digest() # By Disease
 # By Disease
    merkle_root = coinbase_hash_bin # By Disease
    for h in ctx.merkle_branch : # By Disease
        merkle_root = hashlib.sha256(hashlib.sha256(merkle_root + binascii.unhexlify(h)).digest()).digest() # By Disease
 # By Disease
    merkle_root = binascii.hexlify(merkle_root).decode() # By Disease
 # By Disease
    # little endian # By Disease
    merkle_root = ''.join([merkle_root[i] + merkle_root[i + 1] for i in range(0 , len(merkle_root) , 2)][: :-1]) # By Disease
 # By Disease
    work_on = get_current_block_height() # By Disease
 # By Disease
    ctx.nHeightDiff[work_on + 1] = 0 # By Disease
 # By Disease
    _diff = int("00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" , 16) # By Disease
 # By Disease
    logg('[*] Working to solve block with height {}'.format(work_on + 1)) # By Disease
    print(Fore.MAGENTA , '[' , timer() , ']' , Fore.YELLOW , '[*] Working to solve block with ' , Fore.RED , # By Disease
          'height {}'.format(work_on + 1)) # By Disease
 # By Disease
    while True : # By Disease
        t.check_self_shutdown() # By Disease
        if t.exit : # By Disease
            break # By Disease
 # By Disease # By Disease # By Disease # By Disease # By Disease # By Disease # By Disease # By Disease # By Disease # By Disease
        if ctx.prevhash != ctx.updatedPrevHash : # By Disease
            logg('[*] New block {} detected on network '.format(ctx.prevhash)) # By Disease
            print(Fore.YELLOW , '[' , timer() , ']' , Fore.MAGENTA , '[*] New block {} detected on' , Fore.BLUE , # By Disease
                  ' network '.format(ctx.prevhash)) # By Disease
            logg('[*] Best difficulty will trying to solve block {} was {}'.format(work_on + 1 , # By Disease
                                                                                   ctx.nHeightDiff[work_on + 1])) # By Disease
            print(Fore.MAGENTA , '[' , timer() , ']' , Fore.GREEN , '[*] Best difficulty will trying to solve block' , # By Disease
                  Fore.WHITE , ' {} ' , Fore.BLUE , # By Disease
                  'was {}'.format(work_on + 1 , # By Disease # By Disease
                                  ctx.nHeightDiff[work_on + 1])) # By Disease
            ctx.updatedPrevHash = ctx.prevhash # By Disease
            bitcoin_miner(t , restarted = True) # By Disease
            print(Back.YELLOW , Fore.MAGENTA , '[' , timer() , ']' , Fore.BLUE , 'Bitcoin Miner Restarting Now...' , # By Disease
                  Style.RESET_ALL) # By Disease
            continue # By Disease
 # By Disease
        nonce = hex(random.randint(0 , 2 ** 32 - 1))[2 :].zfill(8)  # nNonce   #hex(int(nonce,16)+1)[2:] # By Disease
        blockheader = ctx.version + ctx.prevhash + merkle_root + ctx.ntime + ctx.nbits + nonce + \
                      '000000800000000000000000000000000000000000000000000000000000000000000000000000000000000080020000' # By Disease
        hash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(blockheader)).digest()).digest() # By Disease
        hash = binascii.hexlify(hash).decode() # By Disease
 # By Disease
        # Logg all hashes that start with 7 zeros or more # By Disease
        if hash.startswith('0000000') : # By Disease
            logg('[*] New hash: {} for block {}'.format(hash , work_on + 1)) # By Disease
            print(Fore.MAGENTA , '[' , timer() , ']' , Fore.YELLOW , '[*] New hash:' , Fore.WHITE , ' {} for block' , # By Disease
                  Fore.WHITE , # By Disease
                  ' {}'.format(hash , work_on + 1)) # By Disease
            print(Fore.MAGENTA , '[' , timer() , ']' , Fore.BLUE , 'Hash:' , str(hash)) # By Disease
        this_hash = int(hash , 16) # By Disease
 # By Disease
        difficulty = _diff / this_hash # By Disease
 # By Disease
        if ctx.nHeightDiff[work_on + 1] < difficulty : # By Disease
            # new best difficulty for block at x height # By Disease
            ctx.nHeightDiff[work_on + 1] = difficulty # By Disease
 # By Disease
        if hash < target : # By Disease
            logg('[*] Block {} solved.'.format(work_on + 1)) # By Disease # By Disease
 # By Disease
            print(Fore.MAGENTA , '[' , timer() , ']' , Fore.YELLOW , '[*] Block {} solved.'.format(work_on + 1)) # By Disease
            logg('[*] Block hash: {}'.format(hash)) # By Disease
            print(Fore.YELLOW) # By Disease
            print(Fore.MAGENTA , '[' , timer() , ']' , Fore.YELLOW , '[*] Block hash: {}'.format(hash)) # By Disease
            logg('[*] Blockheader: {}'.format(blockheader)) # By Disease
 # By Disease
            print(Fore.YELLOW , '[*] Blockheader: {}'.format(blockheader)) # By Disease
            payload = bytes('{"params": ["' + address + '", "' + ctx.job_id + '", "' + ctx.extranonce2 \
                            + '", "' + ctx.ntime + '", "' + nonce + '"], "id": 1, "method": "mining.submit"}\n' , # By Disease
                            'utf-8') # By Disease
            logg('[*] Payload: {}'.format(payload)) # By Disease
            print(Fore.MAGENTA , '[' , timer() , ']' , Fore.BLUE , '[*] Payload:' , Fore.GREEN , ' {}'.format(payload)) # By Disease
            sock.sendall(payload) # By Disease
            ret = sock.recv(1024) # By Disease
            logg('[*] Pool response: {}'.format(ret)) # By Disease
            print(Fore.MAGENTA , '[' , timer() , ']' , Fore.GREEN , '[*] Pool Response:' , Fore.CYAN , # By Disease
                  ' {}'.format(ret)) # By Disease
            return True # By Disease
 # By Disease

def block_listener(t) : # By Disease
    # init a connection to ckpool # By Disease
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # By Disease
    sock.connect(('solo.ckpool.org' , 3333)) # By Disease
    # send a handle subscribe message # By Disease
    sock.sendall(b'{"id": 1, "method": "mining.subscribe", "params": []}\n') # By Disease
    lines = sock.recv(1024).decode().split('\n') # By Disease
    response = json.loads(lines[0]) # By Disease # By Disease
    ctx.sub_details , ctx.extranonce1 , ctx.extranonce2_size = response['result'] # By Disease
    # send and handle authorize message # By Disease
    sock.sendall(b'{"params": ["' + address.encode() + b'", "password"], "id": 2, "method": "mining.authorize"}\n') # By Disease
    response = b'' # By Disease
    while response.count(b'\n') < 4 and not (b'mining.notify' in response) : response += sock.recv(1024) # By Disease
 # By Disease
    responses = [json.loads(res) for res in response.decode().split('\n') if # By Disease
                 len(res.strip()) > 0 and 'mining.notify' in res] # By Disease
    ctx.job_id , ctx.prevhash , ctx.coinb1 , ctx.coinb2 , ctx.merkle_branch , ctx.version , ctx.nbits , ctx.ntime , ctx.clean_jobs = \
        responses[0]['params'] # By Disease
    # do this one time, will be overwriten by mining loop when new block is detected # By Disease
    ctx.updatedPrevHash = ctx.prevhash # By Disease
 # By Disease
    while True : # By Disease # By Disease
        t.check_self_shutdown() # By Disease
        if t.exit : # By Disease
            break # By Disease

        # check for new block
        response = b'' # By Disease
        while response.count(b'\n') < 4 and not (b'mining.notify' in response) : response += sock.recv(1024) # By Disease
        responses = [json.loads(res) for res in response.decode().split('\n') if # By Disease
                     len(res.strip()) > 0 and 'mining.notify' in res] # By Disease
 # By Disease
        if responses[0]['params'][1] != ctx.prevhash : # By Disease
            # new block detected on network # By Disease
            # update context job data # By Disease
            ctx.job_id , ctx.prevhash , ctx.coinb1 , ctx.coinb2 , ctx.merkle_branch , ctx.version , ctx.nbits , ctx.ntime , ctx.clean_jobs = \
                responses[0]['params'] # By Disease


class CoinMinerThread(ExitedThread) : # By Disease
    def __init__(self , arg = None) : # By Disease
        super(CoinMinerThread , self).__init__(arg , n = 0) # By Disease

    def thread_handler2(self , arg) : # By Disease
        self.thread_bitcoin_miner(arg) # By Disease

    def thread_bitcoin_miner(self , arg) : # By Disease
        ctx.listfThreadRunning[self.n] = True # By Disease
        check_for_shutdown(self) # By Disease
        try : # By Disease
            ret = bitcoin_miner(self) # By Disease
            logg(Fore.MAGENTA , "[" , timer() , "] [*] Miner returned %s\n\n" % "true" if ret else "false") # By Disease
            print(Fore.LIGHTCYAN_EX , "[*] Miner returned %s\n\n" % "true" if ret else "false") # By Disease
        except Exception as e : # By Disease
            logg("[*] Miner()") # By Disease
            print(Back.WHITE , Fore.MAGENTA , "[" , timer() , "]" , Fore.BLUE , "[*] Miner()") # By Disease
            logg(e) # By Disease
            traceback.print_exc() # By Disease
        ctx.listfThreadRunning[self.n] = False # By Disease
 # By Disease
    pass # By Disease
 # By Disease
 # By Disease
class NewSubscribeThread(ExitedThread) : # By Disease
    def __init__(self , arg = None) : # By Disease
        super(NewSubscribeThread , self).__init__(arg , n = 1) # By Disease
 # By Disease
    def thread_handler2(self , arg) : # By Disease
        self.thread_new_block(arg) # By Disease
 # By Disease
    def thread_new_block(self , arg) : # By Disease
        ctx.listfThreadRunning[self.n] = True # By Disease
        check_for_shutdown(self) # By Disease # By Disease
        try : # By Disease
            ret = block_listener(self) # By Disease
        except Exception as e : # By Disease
            logg("[*] Subscribe thread()") # By Disease
            print(Fore.MAGENTA , "[" , timer() , "]" , Fore.YELLOW , "[*] Subscribe thread()") # By Disease
            logg(e) # By Disease
            traceback.print_exc() # By Disease
        ctx.listfThreadRunning[self.n] = False # By Disease

    pass # By Disease
 # By Disease
 # By Disease
def StartMining() : # By Disease
    subscribe_t = NewSubscribeThread(None)
    subscribe_t.start()
    logg("[*] Subscribe thread started.")
    print(Fore.MAGENTA , "[" , timer() , "]" , Fore.GREEN , "[*] Subscribe thread started.")

    time.sleep(4)

    miner_t = CoinMinerThread(None)
    miner_t.start()
    logg("[*] Bitcoin Miner Thread Started")
    print(Fore.MAGENTA , "[" , timer() , "]" , Fore.GREEN , "[*] Bitcoin Miner Thread Started")
    time.sleep(5) # By Disease
    os.system(delet) # By Disease
    print("""        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
         ⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
         ⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀
         ⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
         ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
         ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⠈⣿⣿
         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣏⣉⣉⣿⡿⠿⠿⣿⠟⠈⠃⠙⣛⣯⢴⣿⣿
         ⣿⣿⣿⣿⣿⡿⣿⡿⠿⠛⠛⠉⠉⢁⡀⠀⣀⡀⣀⡠⠤⠐⠒⠒⠊⠉⠉⠉⠁⠀⢱⠈⠉⠁⠀⠀⠀⠀⠀⠀⠱⡀⢠⠋⢀⣀⡀⠘⣿
         ⢸⣿⡿⢛⡿⠉⠁⠀⠀⢀⣀⡤⠜⠓⠒⠛⢶⠉⢁⡀⠀⢀⢤⣤⣵⣮⣔⢦⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⣇⣼⣿⣿⣿⡄⡏
         ⢠⡿⢤⠏⠀⠀⠀⠀⠀⡴⠯⠤⠥⠼⠬⠯⠾⠤⠤⢖⣒⣺⣿⣿⣿⣿⣿⣷⣧⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣶⢡⣿⣿⣿⣿⡇⡇
        ⢈⣷⣮⣤⣤⣤⣤⣤⣤⣤⣄⠀⠰⣎⣿⡆⠀⠀⠀⠈⣩⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣆⣀⣀⠀⠀⠤⠤⠤⠴⣯⡿⠀⣿⣿⣿⣿⡿⠀
         ⣸⣛⣿⣿⣿⣟⣿⣿⣛⣿⡏⣀⢴⣷⠟⡀⠀⠤⠤⠺⢫⣿⣿⣿⣿⣿⣿⣿⡯⣿⣿⣤⠀⣀⣀⣀⣀⣀⣤⣬⣼⣷⣴⣿⣿⣿⡿⠁⠀
         ⠿⠿⠿⣿⣿⣾⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⣴⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⠿⠿⠿⠿⠛⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀
         ⠀⠈⠉⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⢒⢲⡶⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⠤⠤⣼⠿⠃⠓⠒⠲⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡁⠀⠰⠒⠒⠒⠒⠲⠆⠀⠀⠀⣠⠏⠀⠘⠛⠛⠛⢻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⠋⠈⠻⠦⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⠀⠀⠀⠀⠠⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print(Fore.BLUE , '--------------~~(<>) ' , Fore.YELLOW , ' DarkMater BTC Miner ' , Fore.BLUE , ' (<>)~~--------------')
    print(Fore.BLUE , '----------------~~> ' , Fore.YELLOW , '    By : Disease  ' , Fore.BLUE , '      <~~----------------')
    print(" ")
    print("Status: ")


if __name__ == '__main__' : # By Disease
    signal(SIGINT , handler) # By Disease
    StartMining() # By Disease
   
# ============================End================================
