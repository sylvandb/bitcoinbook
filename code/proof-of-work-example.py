#!/usr/bin/env python
# example of proof-of-work algorithm

from hashlib import sha256
from time import time
from random import randint,seed

max_nonce = 2 ** 32 # 4 billion


def proof_of_work(header, difficulty_bits):

    target = 2 ** (256-difficulty_bits)
    header = str(header)

    # for random nonce's, replace the "nonce = ..." line with:
        #nonce = randint(0, max_nonce)
    # use ^^^ to replace the line "nonce = ..." inside the loop
    # (putting a comment inside the loop slows it down)
    for tries in xrange(max_nonce):
        nonce = tries
        hash_result = sha256(header+str(nonce)).hexdigest()

        if long(hash_result, 16) < target:
            print "Success with nonce %s" % nonce
            return (hash_result,tries)

    return ('',tries)


if __name__ == '__main__':
    
    nonce = 0
    hash_result = ''
    seed(42)
        
    for difficulty_bits in xrange(32):
        
        difficulty = 2 ** difficulty_bits
        print "\nDifficulty: %ld (%d bits)" % (difficulty, difficulty_bits)
    
        print "Starting search..."
        start_time = time()
        new_block = 'test block with transactions' + hash_result # make a new block which includes the hash from the previous block
        (hash_result, tries) = proof_of_work(new_block, difficulty_bits) # find a nonce for the new block
        end_time = time()
        if hash_result:
            print "Hash is %s" % hash_result
        else:
            print "Failed after %d tries" % tries
        elapsed_time = end_time - start_time
        print "Elapsed Time: %.4f seconds" % elapsed_time
    
        if elapsed_time > 0:
            hash_power = float(long(tries)/elapsed_time)
            print "Hashing Power: %ld hashes per second" % hash_power

        if not hash_result:
            print "Giving up."
            break
    
    
    
