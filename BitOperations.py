# getBit() returns false if bit at offset is 0 and true if 1
def getBit(int_type, offset):
    mask = 1 << offset
    return not(int_type & mask == 0)

# setBit() returns an integer with the bit at 'offset' set to 1.
def setBit(int_type, offset):
    mask = 1 << offset
    return int_type | mask

# clearBit() returns an integer with the bit at 'offset' set to 0.
def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return int_type & mask

# updateBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.
def updateBit(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)