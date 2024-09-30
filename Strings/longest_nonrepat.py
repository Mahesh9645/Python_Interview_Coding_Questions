a = "abcabcab"
b = ""
longest = ""

for i in a:
    if i not in b:
        b += i  # Add unique characters to 'b'
    else:
        if len(b) > len(longest):
            longest = b  # Update the longest substring if 'b' is longer
        # b = b[b.index(i)+1:] + i  # Remove characters up to the repeated one and start fresh
        b = b.replace(b,'') + i

if len(b) > len(longest):
    longest = b  # Final check for the last substring

print(f"Longest non-repeating substring: '{longest}'")
