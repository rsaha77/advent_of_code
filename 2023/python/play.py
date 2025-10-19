def generate_patterns(s):
    if not s:
        return ['']
    # Recurse for the rest of the string
    subpatterns = generate_patterns(s[1:])
    # Generate patterns for the current character
    print(s, subpatterns)
    if s[0] == '?':
        return ['.' + p for p in subpatterns] + ['#' + p for p in subpatterns]
    else:
        return [s[0] + p for p in subpatterns]

# Given string
s = "???"
patterns = generate_patterns(s)

# Print the patterns
print()
# for pattern in patterns:
#     print(pattern)