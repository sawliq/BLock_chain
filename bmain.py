from Block import Block

blockchain=[]
genesis_block= Block("welcome to block chain",["raul sent 1 bt to ravi",
                                               "sam sent 5 bt to pal"])
second_block=Block(genesis_block.block_hash,["Simran sent 11 bt to raam"])
third_block=Block(second_block.block_hash,['brianss sent 5 bt to paul'])

print("Block_hash: genesis_block")
print(genesis_block.block_hash)

print('Block_hash:Second_block')
print(second_block.block_hash)

print('Block_hash:Third_block')
print(third_block.block_hash)