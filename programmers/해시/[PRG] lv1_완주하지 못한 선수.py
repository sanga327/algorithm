def solution(participant, completion):
    answer = ''
    participant_dict = dict(zip(participant, [0]*len(participant)))
    
    for p in participant:
        participant_dict[p] += 1
        
    for c in completion:
        if participant_dict[c] == 1:
            del participant_dict[c]
        else: 
            participant_dict[c] -= 1
    answer =list(participant_dict.keys())[0]
    return answer