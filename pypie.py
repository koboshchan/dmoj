solution_code = b"print(*b'\x03\x01\x04\x01\x05\x09',' ',*b'\x02\x07\x01\x08\x02\x08',sep='')"

with open("pie.py", "wb") as f:
    f.write(solution_code)