# Enter your code here
#hi!

# 1-byte: 0xxxxxxx
# 2-byte: 110xxxxx 10xxxxxx
# 3-byte: 1110xxxx 10xxxxxx 10xxxxxx
# 01010101 -> valid 1 byte
# 1100000010111111 -> valid 2 byte
# 11010101 -> invalid 1 byte
# "110000001011111111000000101111111100000010111111010101011100000010111111" -> valid utf 8 string, entirely of valid utf-8 characters

# return true if made of correct utf8 chars and false if not

ONE_BYTE = "0"
TWO_BYTE = "110"
THREE_BYTE = "1110"
CONTINUATION_BYTE = '10'

def check_utf8(input_string):
    utf8_chars = []
    
    count = 0
    utf_char = ""
    for i in range(0, len(input_string)):
        count += 1
        utf_char += input_string[i]

        if count >= 8:
            utf8_chars.append(utf_char)
            count = 0
            utf_char = ""
    # 010
    if not utf_char == "":
        return False
        
    utf8_chars.reverse()
    
    try:
        while True:
            valid = False
            current = utf8_chars.pop()
            if current.startswith(ONE_BYTE):
                valid = True
            elif current.startswith(TWO_BYTE):
                next_char = utf8_chars.pop()
                if not next_char.startswith(CONTINUATION_BYTE):
                    return False
                valid = True
            elif current.startswith(THREE_BYTE):
                for i in range(0, 2):
                    next_char = utf8_chars.pop()
                    if not next_char.startswith(CONTINUATION_BYTE):
                        return False
                    valid = True
            else:
                return False
                
    except Exception:
        pass
    
    return valid
        

print(check_utf8("11000000"))