def solution(text, ending):
    if len(ending)>len(text):
        return False
    text_r = "".join(reversed(text))
    ending_r = "".join(reversed(ending))
    cut_text_r = text_r[0:len(ending)]
    return cut_text_r == ending_r
    
    # for count, element in enumerate(ending_r):
    #     if element == text_r[count]:
    #         continue
    #     else:
    #         return False
    # return True

print(solution("samurai", "ai"))

# print(solution("ninja",   "ja" ))
# print(solution ( "sensei",  "i"     ))
# print(solution ( "abc",     "abc"   ))
# print(solution ( "abcabc",  "bc"    ))
# print(solution  ( "fails",   "ails"  ))


# print(solution  ( "sumo",    "omo"   ))
# print(solution  ( "samurai", "ra"    ))
# print(solution    ( "abc",     "abcd"  ))
# print(solution    ( "ails",    "fails" ))
# print(solution     ( "this",    "fails" ))
# print(solution     ( "spam",    "eggs"  ))