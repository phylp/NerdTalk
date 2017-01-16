def longest_sequence(s):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    longest_sequence = ''
    for i in range(0, len(s)):
        current_sequence = s[i]
        alpha_index = alpha.index(s[i])
        for j in range(i+1, len(s)):
            if alpha.index(s[j]) >= alpha_index:
                current_sequence += s[j]
                alpha_index = alpha.index(s[j])
                if len(current_sequence) > len(longest_sequence):
                    longest_sequence = current_sequence
            elif alpha.index(s[j]) < alpha_index:
                break
    print('Longest substring in alphabetical order is:' + str(longest_sequence))