from typing import Generator


d = {' ': '1011', '.': '1110', 'D': '1000', 'c': '000', 'd': '001', 'e': '1001', 'i': '010', 'm': '1100', 'n': '1010', 'o': '1111', 's': '011', 'u': '1101'}
result = '100011110001001101000111111011001010011000010110011010111110'


def huffman_decode(content:str, _lookup) -> Generator[str, None, None]:
	while content:
		_options = [i for i in _lookup if content.startswith(i) and (any(content[len(i):].startswith(b) for b in _lookup) or not content[len(i):])]
		if not _options:
			raise Exception("Decoding error")
		yield _lookup[_options[0]]
		content = content[len(_options[0]):]


print(''.join(huffman_decode(result, {b:a for a, b in d.items()})))