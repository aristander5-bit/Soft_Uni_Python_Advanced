txt = input()

# symbols = set()
#
# for ch in txt:
#     symbols.add(ch)
#
# for ch in sorted(symbols):
#     print(f"{ch}: {txt.count(ch)} time/s")

[print(f"{ch}: {txt.count(ch)} time/s") for ch in sorted(set(txt))]